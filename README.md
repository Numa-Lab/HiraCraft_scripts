# HiraCraft_scripts

## Usage

### 1.Item_Convert.py
langファイルを生成するPythonコード（pykakasi, jaconv必須、Python 3.9.4）

濁音・半濁音を変換、拗音を変換、ひらがなで表せなくて使用不可なアイテムをリネームする、伸ばし棒を変換、「おーくの」を消す(←無効化不可)...など

無効化するときは、enable_...変数に代入している部分をFalseに書き換えてください。 

実行時のカレントディレクトリにresult_jsonフォルダとja_jp_items.jsonファイルが必要、出力はresult_jsonの中に。 

### 2.CreateImg.py
50音、16*16のテクスチャを生成するPythonコード（PIL, pykakasi, Python 3.9.4）

imgフォルダをカレントディレクトリに用意しておいてください。
ファイル名はアルファベットで出力されます。