![Python application](https://github.com/CODE-for-GIFU/covid19-scraping/workflows/Deploy%20JSON%20Files/badge.svg)

## What is this
岐阜県が公開するオープンデータカタログサイトをスクレイピングし、jsonファイルを出力するpythonスクリプトです。
(https://data.gifu-opendata.pref.gifu.lg.jp/dataset/c11223-001)

## Specification
#### main.py
- main.pyを実行すると、
  - ①settings.pyのREMOTE_SOURCESに基づきcsvデータを取得し、
  - ②importフォルダ内のcsvを読み込んで、それら全てのデータのjsonファイルを出力します
- このスクリプトでは、1つのCSVが1つのJSONに対応します（last_updateをのぞく）
- csvのキーに「・」「_」がある場合は出力しません

## 出力されるデータ
| データ |  key  |  source  | 外部アクセス  |
| ---- | ---- | ---- | ---- |
|  陽性患者属性 |  patients  | [Link](https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/9c35ee55-a140-4cd8-a266-a74edf60aa80/download/210005gifucovid19patients.csv) |  [patients.json](https://code-for-gifu.github.io/covid19-scraping/patients.json)  |
|  検査実施件数 |  testcount  | [Link](https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/f2468ba2-efe8-483f-9b1b-ee67755dedb0/download/210005gifucovid19testcount.csv) |  [testcount.json](https://code-for-gifu.github.io/covid19-scraping/testcount.json)  |
|  健康相談窓口件数 |  callcenter  | [Link](https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/aa3ebb23-5704-470f-a41e-d834d0a51fc0/download/210005gifucovid19callcenter.csv) |  [callcenter.json](https://code-for-gifu.github.io/covid19-scraping/callcenter.json)  |
|  帰国者・接触者相談センター件数 |  advicecenter | [Link](https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/b71cdec1-b763-4b67-9ff4-24deaea65a55/download/210005gifucovid19advicecenter.csv) |  [advicecenter.json](https://code-for-gifu.github.io/covid19-scraping/advicecenter.json)  |

## Scheduling
GitHub Actionsにより10分に一度、すべてjson類をgh-pagesブランチに書き出します

## 外部からのアクセス
gh-pagesブランチにあるjsonデータに直接アクセスしてデータを読み出す事が出来ます。

