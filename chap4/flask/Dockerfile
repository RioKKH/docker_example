# カスタムイメージの元となるイメージの指定
FROM python:3.12
# 作業ディレクトリの指定
WORKDIR /usr/src/app
# requirements.txtをコンテナにコピー
COPY requirements.txt ./
# イメージのビルド時にコマンドを実行する
RUN pip install -r requirements.txt
# コンテナの起動時にコマンドを実行する
CMD ["flask", "run", "--host=0.0.0.0"]
