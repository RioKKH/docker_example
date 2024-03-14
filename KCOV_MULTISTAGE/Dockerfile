# ステージ1: libcurlのスタティックライブラリをビルドする
FROM ubuntu:22.04 as libcurl-builder

RUN apt-get update && apt-get install -y \
    build-essential \
		autoconf \
		libtool \
		pkg-config \
		libssl-dev \ 
		curl

# libcurlのソースをダウンロードしてビルドする
RUN curl -LO https://curl.se/download/curl-7.79.1.tar.gz \
	  && tar -zxvf curl-7.79.1.tar.gz \ 
		&& cd curl-7.79.1 \
		&& ./buildconf \
		&& ./configure --disable-shared --enable-static --with-pic --with-openssl --prefix=/usr/local \
		&& make \
		&& make install

# elfutisl (libdw)のスタティックライブラリをビルドする
FROM ubuntu:22.04 as elfutils-builder
# elfutilsのビルドに必要なパッケージをインストールする
RUN apt-get update && apt-get install -y \
		build-essential \
		autoconf \
		libtool \
		pkg-config \
		zlib1g-dev \
		libcurl4-openssl-dev \
		curl

# elfutilsのソースをダウンロードしてビルドする
RUN curl -LO https://sourceware.org/elfutils/ftp/0.185/elfutils-0.185.tar.bz2 \
		&& tar -jxvf elfutils-0.185.tar.bz2 \
		&& cd elfutils-0.185 \
		&& ./configure --disable-shared --enable-static --with-pic --prefix=/usr/local \
		# && ./configure --disable-shared --enable-static --with-pic --prefix=/usr/local --disable-debuginfod \
		&& make \
		&& make -C libelf install \
		&& make -C libdw install
# ステージ2: kcovのスタティックバイナリをビルドする
FROM ubuntu:22.04 as kcov-builder

COPY --from=libcurl-builder /usr/local /usr/local
COPY --from=elfutils-builder /usr/local /usr/local

# 必要なパッケージと依存ライブラリをインストールする
RUN apt-get update && apt-get install -y \
		cmake \
		g++ \
		git \
		libcurl4-openssl-dev \
		libdw-dev \
		libbfd-dev \
		libelf-dev \
		libiberty-dev \
		libssl-dev \
		pkg-config \
		python3 \
		binutils-dev \
		zlib1g-dev

# kcovのリポジトリをクローンする
RUN git clone https://github.com/SimonKagstrom/kcov.git \
    && cd kcov \
		&& mkdir build \
		&& cd build \
		&& cmake .. -DCMAKE_EXE_LINKER_FLAGS=-static \
		&& make \
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

