# pdf-text-adder-py

PDF にテキストを追加する CLI ツール（A4 対応のみ）

## Requirements

- Python 3.10.5（他のバージョンでも動くかも。未検証。）
- Poetry 1.3.1

## インストール

```sh
git clone git@github.com:nukopy/pdf-text-adder-py.git
cd pdf-text-adder-py
poetry install
poetry run python cli.py # help を表示
```

## 実行

```sh
$ python cli.py
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add-text-to-pdf        単一の PDF ファイルにテキストを挿入する
  add-text-to-pdf-files  複数の PDF ファイルにテキストを挿入する
```

## 例

### 単一の PDF ファイルにテキストを挿入する

```sh
python cli.py add-text-to-pdf \
  --input-filename ./sample/dummy.pdf \
  --text-position-preset top-right \
  --text "Hello World Co., Ltd."
```

### 複数の PDF ファイルにテキストを挿入する

- テキスト挿入位置をプリセットで指定する

```sh
python cli.py add-text-to-pdfs \
  --input-dir ./sample \
  --text-position-preset top-left \
  --text "株式会社ハローワールド"
```

- テキスト挿入位置を座標で指定する

```sh
python cli.py add-text-to-pdfs \
  --input-dir ./sample \
  --text-position-x 100 \
  --text-position-y 100 \
  --text "Hello World Co., Ltd."
```

- 複数の Amazon の領収書 PDF の右上の宛名欄に宛名を挿入する

そもそもこれやるために作った。

```sh
python cli.py add-text-to-pdfs \
  --input-dir path/to/receipts \
  --text-position-preset amazon-receipt \
  --text "株式会社ハローワールド 三愛太郎"
```
