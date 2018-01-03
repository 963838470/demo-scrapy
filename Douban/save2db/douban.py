import requests
from bs4 import BeautifulSoup
import re
from sqlHelper import MSSQL

top250 = []

urls = [
    'https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]


def get_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    names = soup.select('div.hd > a')
    srcs = soup.select('div.pic > a > img')
    playables = soup.select('div.hd > .playable')
    ps = re.findall('<br>\n\s+(.*?)\n\s+</p>', wb_data.text, re.S)
    places = re.findall('&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;', wb_data.text)
    levels = soup.select('span.rating_num')
    quotes = soup.select('span.inq')
    directors = re.findall('导演: (.*?)&nbsp;', wb_data.text, re.S)
    performers = re.findall('主演: (.*?)<br>', wb_data.text, re.S)
    scoreUserNums = soup.select('div.star > span:nth-of-type(4)')
    for name, src, playabler, p, place, level, quoter, directorr, performerr, scoreUserNum in zip(names, srcs, playables, ps, places, levels, quotes, directors, performers, scoreUserNums):
        pc = p.split('&nbsp;/&nbsp;')
        title = name.get_text().split('\n')[1],
        otherTitle = name.get_text().replace('\xa0', '').replace(
            '\n', '').replace(name.get_text().split('\n')[1] + "/", ""),
        imgSrc = src.attrs['src'],
        playable = playabler.get_text(),
        year = str(pc[0]),
        country = str(pc[1]),
        score = level.get_text(),
        quote = quoter.get_text(),
        detailLink = name.attrs['href'],
        director = directorr,
        performer = performerr,
        _type = str(pc[2]),
        scoreUserNum = scoreUserNum.get_text().replace('人评价', '')
        # print(info)
        #sql = "INSERT INTO dbo.Movie (Title, OtherTitle, ImgSrc, Playable, Director, Performer, Year, Country, Type, Score, ScoreUserNum, Quote, DetailLink) VALUES ('" + title + "', '" + otherTitle + "', '" + imgSrc + "', '" + playable + "', '" + director + "', '" + performer + "', '" + year + "', '" + country + "', '" + _type + "', '" + score + "', '" + scoreUserNum + "', '" + quote + "', '" + detailLink
        #MSSQL().ExecNonQuery(sql)

for url in urls:
    get_info(url)
