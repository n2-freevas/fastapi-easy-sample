# Fastapi-sample-maked-by-n2-freevas

このサンプルは、
https://qiita.com/drafts/f5114ebf5846031f3c8d/edit
を一緒に見ると、参考になるかと。

## 1. ローカル環境での実行
### [1] ローカル開発環境構築
1. pythonの準備
使用しているpython version: 3.9.6
pyenvを使って切り替えるといいかもしれません。
[pyenvを使ってpythonバージョンの切り替え](https://qiita.com/Kohey222/items/19eb9b3cbcec9b176625)
```
# pyenvをインストール
$ brew install pyenv

# 3.9.6をインストールする
$ pyenv install 3.9.6

# 切り替え
$ pyenv local 3.9.6

# 確認
$ python -V
Python 3.9.6
```
※切り替わらない場合
環境変数を追加しないといけない。
[pyenvでpythonのバージョンが反映されない時](https://qiita.com/minarai/items/297aec329f2f029bee10)

2. venvを作成する
```
# 仮想環境ファイル_envがディレクトリにないなら、仮想環境を構築する
$ python -m venv _env
or
$ python3 -m venv _env (macだとこっち)
```

### [2] ローカル環境立ち上げ
1. venvを起動する
```

$ source ./_env/bin/activate

$ (_env) { user-name }@{ ... } ... #<- (_env)が左に表示されたらOK

仮想環境を抜けるなら、
$ deactivate
```

2. ライブラリをインストールする
```
$ pip install -r requirements.txt
or
$ pip3 install -r requirements.txt (こっちじゃないとだめな人もいるかも)

そして、

$pip list

で、

fastapi==0.70.0
uvicorn==0.15.0
SQLAlchemy==1.4.25
psycopg2==2.9.1
gunicorn==20.1.0

この辺が出てきたらOK
```

3. アプリの実行
```
$ uvicorn main:app --reload
```
で起動する。

4. アプリの停止
ctrl + Cで、停止。
