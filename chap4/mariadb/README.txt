## コンテナ内でコマンドを実行する
$ docker compose exec <コンテナ名> <コンテナ内で実行したいコマンド>

$ docker compose exec db mariadb --version

## コンテナ内でシェルを起動する
$ docker compose exec <コンテナ名> /bin/bash

$ docker compose exec db /bin/bash
# mariadb --version
# mariadb -u testuser -D testdb -p
# <パスワードを入力> testpass

# mariadbのCLIを終了するには \q を入力すればよい
