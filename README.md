# pygoogletrans

googletransモジュールを使ってファイルを一括翻訳します。

## 使い方

1. cloneする
```bash
# git clone https://github.com/yk4vv4/pygoogletrans.git
```

2. input/ 配下に翻訳したいテキストファイルを配置する
```bash
# cp <path/to/english/text/file> ./input/
```

3. 実行する
```bash
# docker run --rm -it -v $(pwd)/app":/app -v "$(pwd)/input":/input -v "$(pwd)/output":/output" yukikawashima/pygoogletrans
```

4. 確認する

output/ 配下に翻訳ファイルが元ファイルと同じファイル名でできているので確認します。

## パラメータ

- `-v $(pwd)/app`
    - COPYしつつもホスト側で編集したりしてるのでとりあえずマウントしちゃう
- `-v $(pwd)/input`
    - 翻訳したいファイルを入れておくところ
- `-v $(pwd)/output`
    - 翻訳したファイルが書き出されるところ
