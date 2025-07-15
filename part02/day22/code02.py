"""
网络数据获取

注：
数据查询服务供应商为“天行数据”，使用其免费API获取当日简讯。
"""
import requests

resp = requests.get('https://apis.tianapi.com/bulletin/index?key=1e706f95c755547864f8b86ad445e9cb')
if resp.status_code == 200:
    data = resp.json()
    for item in data['result']['list']:
        print(item)
