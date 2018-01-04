''' 获取电影详情并插入数据库 '''

import requests
from bs4 import BeautifulSoup
import re
from sqlHelper import MSSQL
import time


def get_info(obj):
    url = obj[13]
    id = obj[0]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    nodes = soup.select(".all")
    if len(nodes) <= 0:
        nodes = soup.select('[property="v:summary"]')
    if len(nodes) > 0:
        descript = nodes[0].prettify()
        sql = 'UPDATE Movie SET Descript=%s WHERE Id = %d'
        params = (descript, id)
        print(params)
        MSSQL().ExecNonQuery(sql, params)


ms = MSSQL()
result = ms.ExecQuery("SELECT * FROM Movie")
for obj in result:
    if obj[0] > -1:
        get_info(obj)
        time.sleep(10)  # 每次请求后等待一段时间，防止请求过快中断连接
