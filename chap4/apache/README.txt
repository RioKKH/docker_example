## コンテナを起動する

$ docker compose up -d # コンテナの作成と実行を行う
$ docker container ls # 実行中のコンテナを確誋
$ docker container ls -a # 全てのコンテナを確誋

$ docker compose ls # プロジェクトの一覧表示
NAME                STATUS              CONFIG FILES
apache              running(1)          /home/rio/work/git/docker_example/chap4/apache/compose.yaml

ブラウザでhttp://localhost:8080/にアクセスしてみる

## コンテナを停止する
$ docker compose stop
✔ Container apache-web-1  Stopped

## 停止していてコンテナを実行する
$ docker compose start

## コンテナを削除する (停止している場合)
$ docker container rm <CONTAINER_ID_or_NAME>

## コンテナ内へファイルをコピーする
$ docker compose cp web:/usr/local/apache2/htdocs/index.html .

## コンテナへファイルをコピーする
$ docker compose cp index.html web:/usr/local/apache2/htdocs/index.html

## コンテナを削除する
このコマンドはコンテナが実行中であっても使用可能で、コンテナを停止して削除する
紐づいているネットワークやボリュームも削除される
$ docker compose down
[+] Running 2/2
 ✔ Container apache-web-1  Removed                                                                                                           1.6s
 ✔ Network apache_default  Removed                                                                                                           0.6s
$ docker compose ls
NAME                STATUS              CONFIG FILES
$ docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

これだとコンテナは削除してくれるが、イメージは削除してくれない。
イメージも削除する場合は、--rmi allオプションを使用する


