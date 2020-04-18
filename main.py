# coding:UTF-8
import settings
import json
import csv
import codecs

import datetime
import dateutil.parser
import os
import urllib.request

from typing import Dict

# 日本標準時
JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

json_list = []
json_data = {}

REMOTE_SOURCES = settings.REMOTE_SOURCES  # 外部ファイルの参照設定
CODECS = settings.CODECS  # ファイルエンコーディングリスト
UNUSE_CHARACTER = settings.UNUSE_CHARACTER

def import_csv_from(csvurl):
    request_file = urllib.request.urlopen(csvurl)
    if not request_file.getcode() == 200:
        return

    f = decode_csv(request_file.read())
    filename = os.path.splitext(os.path.basename(csvurl))[0]
    datas = csvstr_to_dicts(f)
    timestamp = (request_file.getheader('Last-Modified'))

    return {
        'data': datas,
        # 'last_update': datetime.datetime.now(JST).isoformat()
        'last_update': dateutil.parser.parse(timestamp).astimezone(JST).isoformat()
    }

def decode_csv(csv_data):
    print('csv decoding')
    for codec in CODECS:
        try:
            csv_str = csv_data.decode(codec)
            print('ok:' + codec)
            return csv_str
        except:
            print('ng:' + codec)
            continue
    print('Appropriate codec is not found.')

# CSV文字列を[dict]型に変換
def csvstr_to_dicts(csvstr):
    datas = []
    rows = [row for row in csv.reader(csvstr.splitlines())]
    header = rows[0]
    for i in range(len(header)):
        for j in range(len(UNUSE_CHARACTER)):
            header[i] = header[i].replace(UNUSE_CHARACTER[j], '')

    maindatas = rows[1:]
    for d in maindatas:
        # 空行はスキップ
        if d == []:
            continue
        data = {}
        for i in range(len(header)):
            data[header[i]] = d[i]
        datas.append(data)
    return datas

def dumps_json(file_name: str, json_data: Dict):
    # 日本語文字化け対策などを施したdump jsonキット
    with codecs.open("./data/" + file_name, "w", "utf-8") as f:
        f.write(json.dumps(json_data, ensure_ascii=False,indent=4, separators=(',', ': ')))

os.makedirs('./data', exist_ok=True)
for remotes in REMOTE_SOURCES:
    data = import_csv_from(remotes['url'])
    dumps_json(remotes['jsonname'], data)
