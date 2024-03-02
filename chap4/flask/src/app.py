from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    # ブラウザ上に Hello Flask! と表示する
    return 'Hello Flask!'
