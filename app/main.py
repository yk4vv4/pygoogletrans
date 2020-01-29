# coding: utf-8

import glob
import os
import html
import time
from tqdm import tqdm
from googletrans import Translator

# 翻訳モジュール準備
translator = Translator()
proxies = {}
if os.environ.get("http_proxy") is not None:
    proxies["http"] = os.environ.get("http_proxy")
if os.environ.get("https_proxy") is not None:
    proxies["https"] = os.environ.get("https_proxy")
if proxies == {}:
    proxies = None
translator = Translator(proxies=proxies)

def main():
    # 対象ファイルさがし
    inFiles = glob.glob("/input/*.*")
    if len(inFiles) > 0:
        print("{} files found. Translating...".format(len(inFiles)))
    else:
        print("No files found.")
        exit(-1)

    # ファイルごとにるーぷ
    for f in tqdm(inFiles):
        time.sleep(3)
        buffer = []
        chunks = []
        for line in open(f).readlines():
            # 1行ずつ読み込みつつ、
            buffer.append(line)
            # 10000文字超えのタイミングで塊にまとめる
            if len("".join(buffer)) > 10000:
                chunks.append("".join(buffer))
                buffer = []
                continue

        # 残ったバッファを塊として追加
        chunks.append("".join(buffer))
        
        # 塊ごとに翻訳する
        chunks_translated = []
        for i, chunk in enumerate(chunks):
#            print("# {}: {}".format(i, len(chunk)))
            # html実体参照があるとエラーになるため戻しておく
            chunk = html.unescape(chunk)
            result = translator.translate(chunk, src="en", dest="ja")
            chunks_translated.append(result.text)

        # ファイルに書き出す
        outFile = f.replace("/input/", "/output/")
        try:
            open(outFile, "w").write("".join(chunks_translated))
#            print("# Wrote translated file: {}".format(outFile))
        except:
            print("# Failed to write file: {}".format(outFile))
            exit(-2)

if __name__ == '__main__':
    main()
