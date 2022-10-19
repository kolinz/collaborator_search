# 協力者データベース
企業に所属している方や個人事業主、大学など、外部協力しても良いと考えている人材の情報を公開および管理するデータベースです。

# 稼働手順
## pipを用いてライブラリをインストール
```
pip install -r requirements.txt
```

## ソースコードの取得
このリポジトリで公開しているソースコードをサーバーにダウンロードします。git clone コマンドを使いましょう。

## SQLiteを使う場合
下記のコマンドを実行します。
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## SQLite以外を使う場合
「djangoHRProject」ディレクトリ内の「settings.py」を開き、環境変数「DATABASES」を編集してください。編集後は、下記コマンドを実行します。
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## 項目追加などアプリの改修を行った場合
これらについて、項目追加などを行った場合は、各アプリの「migration」ディレクトリ内の「0001_initial.py」を削除します。
 - 認証アプリ : accounts
 - 人物情報および実績情報管理アプリ ： hrdb

下記のコマンドを実行します。
```
python manage.py makemigration accounts
python manage.py makemigration hrdb
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
