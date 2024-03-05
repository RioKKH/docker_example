FROM ubuntu:22.04

# 環境変数を設定
# これにより、apt-get install などで対話型の設定をスキップできる
ENV DEBIAN_FRONTEND=noninteractive

# SSH サーバーをインストール
RUN apt update && \
    apt install -y openssh-server sudo && \
		mkdir /var/run/sshd

# SSH接続用ユーザーを追加
# ここではautoautoという名前のユーザーを作成している
# -rm はユーザーが削除されたときにホームディレクトリも削除する
# -d /home/autoauto はホームディレクトリを指定している
# -g root はグループをrootに設定している
# -G sudo はsudoグループに所属させている
# -gと-Gの違いは、-gはプライマリグループを設定するのに対し、-Gはサブグループを設定する
# -u 1000 はユーザーIDを指定している
RUN useradd -rm -d /home/autoauto -s /bin/bash -g root -G sudo -u 1000 autoauto && \
    echo 'autoauto:password' | chpasswd

# SSH接続時の設定(ここではパスワード認証を有効にしている)
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# SSH接続用のポートを開放
# EXPOSE 22 は、22番ポートを開放するという意味
EXPOSE 22

# SSHサーバーを起動
# -D オプションは、デーモンとして起動するという意味
CMD ["/usr/sbin/sshd", "-D"]
