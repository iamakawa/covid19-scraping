# 外部リソース定義
REMOTE_SOURCES = [
    {
        'url': 'https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/9c35ee55-a140-4cd8-a266-a74edf60aa80/download/210005gifucovid19patients.csv',
        'type': 'csv',
        'jsonname': 'patients.json',
    },
    {
        'url': 'https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/f2468ba2-efe8-483f-9b1b-ee67755dedb0/download/210005gifucovid19testcount.csv',
        'type': 'csv',
        'jsonname': 'testcount.json',
    },
    {
        'url': 'https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/aa3ebb23-5704-470f-a41e-d834d0a51fc0/download/210005gifucovid19callcenter.csv',
        'type': 'csv',
        'jsonname': 'callcenter.json',
    },
    {
        'url': 'https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/b71cdec1-b763-4b67-9ff4-24deaea65a55/download/210005gifucovid19advicecenter.csv',
        'type': 'csv',
        'jsonname': 'advicecenter.json'
    },
    {
        'url': 'https://data.gifu-opendata.pref.gifu.lg.jp/dataset/4661bf9d-6f75-43fb-9d59-f02eb84bb6e3/resource/ff0a6fb9-483f-424b-9e68-5aa979af51b8/download/210005gifucovid19deceasedpatients.csv',
        'type': 'csv',
        'jsonname': 'deceasedpatients.json'
    }

]
# 先にある順にデコードされます
CODECS = ['utf-8', 'cp932', 'shift_jis', 'euc_jp',
          'euc_jis_2004', 'euc_jisx0213',
          'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
          'shift_jis_2004', 'shift_jisx0213',
          'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8_sig']

# jsonパラメータに使用不可の文字(空白文字に置き換え)
UNUSE_CHARACTER = ['・', '_']
