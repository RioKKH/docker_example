# ベースイメージを指定
FROM postgres:latest

# 初期設定スクリプトをコピーする
COPY init.sql /docker-entrypoint-initdb.d/
