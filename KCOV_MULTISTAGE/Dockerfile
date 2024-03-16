# ステージ1: libcurlのスタティックライブラリをビルドする
FROM ubuntu:22.04 as build-env

RUN apt-get update && apt-get install -y \
    build-essential \
		autoconf \
		libtool \
		zlib1g-dev \
		pkg-config \
		libssl-dev \ 
		libbz2-dev \
		m4 \
		libglib2.0-dev \
		libcurl4-openssl-dev \
		perl \
		curl


FROM build-env as openssl-builder
RUN curl -LO https://www.openssl.org/source/openssl-1.1.1w.tar.gz \
		&& tar -zxvf openssl-1.1.1w.tar.gz \
		&& cd openssl-1.1.1w \
		&& ./config --prefix=/usr/local --openssldir=/usr/local/ssl no-shared \
		            enable-des enable-ssl enable-ssl2 \
		# && ./config --prefix=/usr/local no-shared enable-static \
		&& make \
		&& make install


FROM build-env as libcurl-builder
RUN curl -LO https://curl.se/download/curl-7.79.1.tar.gz \
	  && tar -zxvf curl-7.79.1.tar.gz \ 
		&& cd curl-7.79.1 \
		&& ./buildconf \
		&& ./configure --disable-shared --enable-static --with-pic --with-openssl \
		               --with-ssl=/usr/local/ssl --with-crypto --with-ntlm-wb \
									 --enable-ntlm --enable-des \
									 --with-ssl-x509-bundle=/etc/ssl/certs/ca-certificates.crt \
									 --with-libssl-prefix=/usr/local/ssl \
									 # --enable-ares \
									 LDFLAGS="-L/usr/local/ssl/lib" \
									 LIBS="-lssl -lcrypto" \
									 --prefix=/usr/local \
		&& make \
		&& make install


# elfutisl (libdw)のスタティックライブラリをビルドする
FROM build-env as elfutils-builder
# elfutilsのソースをダウンロードしてビルドする
RUN curl -LO https://sourceware.org/elfutils/ftp/0.185/elfutils-0.185.tar.bz2 \
		&& tar -jxvf elfutils-0.185.tar.bz2 \
		&& cd elfutils-0.185 \
		&& ./configure --disable-shared --enable-static --with-pic \
		               --prefix=/usr/local --disable-debuginfod \
		&& make \
		&& make -C libelf install \
		&& make -C libdw install


FROM build-env as zlib-builder
RUN curl -LO https://zlib.net/zlib-1.3.1.tar.gz \
		&& tar -zxvf zlib-1.3.1.tar.gz \
		&& cd zlib-1.3.1 \
		&& ./configure --static --prefix=/usr/local \
		&& make \
		&& make install


# ステージ2: kcovのスタティックバイナリをビルドする
FROM build-env as kcov-builder

COPY --from=zlib-builder /usr/local /usr/local
COPY --from=libcurl-builder /usr/local /usr/local
COPY --from=elfutils-builder /usr/local /usr/local
COPY --from=openssl-builder /usr/local /usr/local

# 必要なパッケージと依存ライブラリをインストールする
RUN apt-get update && apt-get install -y \
		cmake \
		g++ \
		git \
		python3 \
		binutils-dev \
		libssl-dev

# kcovのリポジトリをクローンする
RUN git clone https://github.com/SimonKagstrom/kcov.git \
    && cd kcov \
		&& mkdir build \
		&& cd build \
		&& cmake .. -DKCOV_STATIC_BUILD=ON \
		            # -DSTATIC_OPENSSL=ON \
		# -DCMAKE_EXE_LINKER_FLAGS=-static \
		# & cmake .. -DCMAKE_EXE_LINKER_FLAGS=-static \
		            -DCMAKE_PREFIX_PATH=/usr/local \
		  					-DLIBDW_LIBRARY=/usr/local/lib/libdw.a \
		  					-DLIBELF_LIBRARY=/usr/local/lib/libelf.a \
								-DZLIB_ROOT=/usr/local \
								-DOPENSSL_ROOT_DIR=/usr/local/ssl \
								-DOPENSSL_INCLUDE_DIR=/usr/local/ssl/include \
								-DOPENSSL_CRYPTO_LIBRARY=/usr/local/ssl/lib/libcrypto.a \
								-DOPENSSL_SSL_LIBRARY=/usr/local/ssl/lib/libssl.a \
		&& make VERBOSE=1 \
		&& make install DESTDIR=/kcov-build

#WORKDIR /kcov/build

# スタティックリンクを指定してkcovをビルドする
#RUN cmake .. -DCMAKE_EXE_LINKER_FLAGS=-static && make

# ステージ3: Scientific Linux 7にkcovをコピーする
FROM scientificlinux/sl:7

#RUN yum update -y && yum install -y elfutils-libdw

# kcovビルドステージからビルドされたバイナリをコピーする
COPY --from=kcov-builder /kcov-build/usr/local/bin/kcov /usr/local/bin/kcov

# 作業ディレクトリを設定する
WORKDIR /app

# テストスクリプトｗ実行するためのデフォルトコマンド
CMD ["/bin/bash"]

