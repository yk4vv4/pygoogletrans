# pygoogletrans

googletransモジュールを使ってファイルを一括翻訳します。

## 使い方

1. cloneする
```
git clone https://github.com/yk4vv4/gitignore.git
```

2. input/ 配下に翻訳したいテキストファイルを配置する
```
cp <path/to/english/text/file> ./input/
```

3. 実行する
```
docker run --rm -it -v $(pwd)/app":/app -v "$(pwd)/input":/input -v "$(pwd)/output":/output" yukikawashima/pygoogletrans
```

4. 確認する

output/ 配下に翻訳ファイルが元ファイルと同じファイル名でできている。

## パラメータ

- `-v $(pwd)/app`
    - COPYで良いが、まだホスト側で編集したりするのでとりあえずマウントしちゃう
- `-v $(pwd)/input`
    - 翻訳したいファイルを入れておくところ
- `-v $(pwd)/output`
    - 翻訳したファイルが書き出されるところ
