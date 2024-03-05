FROM scientificlinux/sl:7

# 環境変数を設定してインタラクティブな入力を無効化する
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージをインストールする
# yum clean all はキャッシュを削除してイメージサイズを小さくするためのコマンド
RUN yum update -y && \
    yum install -y openssh-server sudo gcc-4.8.5 gcc-c++ make \
		git gtk2-devel gtk3-devel gnuplot xauth && \
		yum clean all

# SSH サーバーの設定
RUN mkdir /var/run/sshd

# SSHホストキーを生成する
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \
    ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' && \
		ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ''

# SSH接続用のユーザーを作成する
RUN useradd -rm -d /home/autoauto -s /bin/bash -g root -u 1000 autoauto && \
		echo 'autoauto:password' | chpasswd

# sudo 権限を付与する
RUN echo 'autoauto ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# SSSH接続時にパスワード認証を有効にする
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config && \
		sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# SSHが使用するポートを開放する
EXPOSE 22

# SSHサーバーを起動する
CMD ["/usr/sbin/sshd", "-D"]
