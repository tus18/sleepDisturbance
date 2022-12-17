# sleepDisturbance

## ファイル名
音楽ファイルがmusic.wavに設定されているため、sleep.pyでのnameを好きな音楽ファイル名に変更する。

## ライブラリのインストール
OpenCV、dlib、scipyなどが入っていない場合インストールする

## 変数の調整
プログラムを初めて実行すると、目の開閉判定に用いる数値の設定が行われます。
「目を閉じてください」と表示されるので指示に従ってください。
推奨値に従い数値を入力すると初期設定は終了です。
目を閉じたのに「sleepy」と表示されないときは、設定値を大きくしてみてください。

## How-To-Edit
1. プロジェクトをクローン
```bash
$ git clone git@github.com:tus18/sleepDisturbance.git
```

2. コンパイル
```bash
$ python sleep.py
```
3. プログラム終了
```
Escキーで終了（音楽再生中は無効）
```
