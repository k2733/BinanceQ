#在豆瓣源安装 包
#pip install package -i https://pypi.douban.com/simple
#导出当前环境所有模块到requirements.txt
#pip freeze > requirements.txt

#----------------------------------------
import requests
import time
import pandas as pd
# import os
# os.environ['http_proxy'] = "http://20.205.42.253:44300"
# os.environ['https_proxy'] = "http://20.205.42.253:44300"

#代理ip和端口
proxies = {
    "https" : "http://127.0.0.1:10809",
    "https" : "http://127.0.0.1:10809"
}

# proxies = {
#     "https" : "http://192.168.0.105:10809"
# }


BASE_URL = 'https://fapi.binance.com'

kline = '/fapi/v1/klines'

kline_url = BASE_URL + kline + '?' + 'symbol=BTCUSDT&interval=1h&limit=100'
print(kline_url)

# print(re_ping)
resp = requests.get(url=kline_url,proxies=proxies).json()
print(resp)

# https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1h&limit=1000