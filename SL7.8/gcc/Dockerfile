# Scientific Linux 7.8をベースイメージとして使用
FROM scientificlinux/sl:7

# 必要なパッケージをインストールする
RUN yum update  -y
RUN	yum install -y gcc-4.8.5 && \
	  yum install -y make && \
		yum install -y git && \
		yum install -y wget && \
		yum install -y vim

#RUN useradd -m autoeos
#USER autoeos

# コンテナ起動時に実行されるコマンド
#CMD ["/bin/bash"]
#CMD ["gcc", "--version"]
