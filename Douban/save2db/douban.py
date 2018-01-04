''' 获取豆瓣电影Top250并插入数据库 '''

import requests
from bs4 import BeautifulSoup
import re
from sqlHelper import MSSQL

top250 = []

urls = [
    'https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]


def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    nodes = soup.select("ol div.item")
    # 另一种获取方式
    # nodes = soup.find_all("div",class_="item")
    for node in nodes:
        info = re.findall('<br/>\n\s+(.*?)\n\s+</p>', str(node),
                          re.S)[0].split('\xa0/\xa0')  # year country _type
        title = node.select('div.hd > a')[0].get_text().split('\n')[1]
        otherTitle = node.select('div.hd > a')[0].get_text().replace(
            '\xa0', '').replace('\n', '').replace(title + "/", "")
        imgSrc = node.select('div.pic > a > img')[0].attrs['src']
        if len(node.select('div.hd > .playable')) > 0:
            playable = node.select('div.hd > .playable')[0].get_text()
        else:
            playable = "false"
        year = str(info[0])
        country = str(info[1])
        score = node.select('span.rating_num')[0].get_text()
        if len(node.select('span.inq')) > 0:
            quote = node.select('span.inq')[0].get_text()
        else:
            quote = ""
        detailLink = node.select('div.hd > a')[0].attrs['href']
        director = re.findall('导演: (.*?)\xa0', str(node), re.S)[0]
        if len(re.findall('主演: (.*?)<br/>', str(node), re.S)) > 0:
            performer = re.findall('主演: (.*?)<br/>', str(node), re.S)[0]
        else:
            performer = ""
        _type = info[2]
        scoreUserNum = node.select(
            'div.star > span:nth-of-type(4)')[0].get_text().replace('人评价', '')
        sql = '''
                INSERT INTO Movie (Title, OtherTitle, ImgSrc, Playable, Director, Performer, Year, Country, Type, Score, ScoreUserNum, Quote, DetailLink) 
                VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s)
              '''
        params = (title, otherTitle, imgSrc, playable, director, performer,
                  year, country, _type, score, scoreUserNum, quote, detailLink)
        print(params)
        MSSQL().ExecNonQuery(sql, params)


for url in urls:
    get_info(url)
