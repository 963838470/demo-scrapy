''' 获取电影详情并插入数据库 '''

import requests
from bs4 import BeautifulSoup
import re
from sqlHelper import MSSQL


def get_info(obj):
    url = obj[13]
    id = obj[0]
    response = requests.get(url)
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
    get_info(obj)
