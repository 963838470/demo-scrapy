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
    #nodes = soup.find_all("div",class_="item")
    for node in nodes:
        info = re.findall('<br/>\n\s+(.*?)\n\s+</p>', str(node),
                          re.S)[0].split('\xa0/\xa0')  # title otherTitle

        title = node.select('div.hd > a')[0].get_text().split('\n')[1]
        otherTitle = node.select('div.hd > a')[0].get_text().replace(
            '\xa0', '').replace('\n', '').replace(title + "/", "")
        imgSrc = node.select('div.pic > a > img')[0].attrs['src']
        playable = node.select('div.hd > .playable')[0].get_text()
        year = str(info[0])
        country = str(info[1])
        score = node.select('span.rating_num')[0].get_text()
        quote = node.select('span.inq')[0].get_text()
        detailLink = node.select('div.hd > a')[0].attrs['href']
        director = re.findall('导演: (.*?)\xa0', str(node), re.S)[0]
        performer = re.findall('主演: (.*?)<br/>', str(node), re.S)[0]
        _type = info[2]
        scoreUserNum = node.select(
            'div.star > span:nth-of-type(4)')[0].get_text().replace('人评价', '')
        sql = "INSERT INTO Movie (Title, OtherTitle, ImgSrc, Playable, Director, Performer, Year, Country, Type, Score, ScoreUserNum, Quote, DetailLink) VALUES ('" + title + "', %s, '" + \
            imgSrc + "', '" + playable + "', '" + director + "', '" + performer + "', '" + year + "', '" + \
            country + "', '" + _type + "', '" + score + "', '" + \
            scoreUserNum + "', '" + quote + "', '" + detailLink + "')"
        print(sql)
        MSSQL().ExecNonQuery(sql, (otherTitle))

        # print(node)

    # names = soup.select('div.hd > a')
    # srcs = soup.select('div.pic > a > img')
    # playables = soup.select('div.hd > .playable')
    # ps = re.findall('<br>\n\s+(.*?)\n\s+</p>', response.text, re.S)
    # places = re.findall('&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;', response.text)
    # levels = soup.select('span.rating_num')
    # quotes = soup.select('span.inq')
    # directors = re.findall('导演: (.*?)&nbsp;', response.text, re.S)
    # performers = re.findall('主演: (.*?)<br>', response.text, re.S)
    # scoreUserNums = soup.select('div.star > span:nth-of-type(4)')
    # for name, src, playabler, p, place, level, quoter, directorr, performerr, scoreUserNum in zip(names, srcs, playables, ps, places, levels, quotes, directors, performers, scoreUserNums):
    #     pc = p.split('&nbsp;/&nbsp;')
    #     title = name.get_text().split('\n')[1],
    #     otherTitle = name.get_text().replace('\xa0', '').replace(
    #         '\n', '').replace(name.get_text().split('\n')[1] + "/", ""),
    #     imgSrc = src.attrs['src'],
    #     playable = playabler.get_text(),
    #     year = str(pc[0]),
    #     country = str(pc[1]),
    #     score = level.get_text(),
    #     quote = quoter.get_text(),
    #     detailLink = name.attrs['href'],
    #     director = directorr,
    #     performer = performerr,
    #     _type = str(pc[2]),
    #     scoreUserNum = scoreUserNum.get_text().replace('人评价', '')
        # print(info)
        #sql = "INSERT INTO dbo.Movie (Title, OtherTitle, ImgSrc, Playable, Director, Performer, Year, Country, Type, Score, ScoreUserNum, Quote, DetailLink) VALUES ('" + title + "', '" + otherTitle + "', '" + imgSrc + "', '" + playable + "', '" + director + "', '" + performer + "', '" + year + "', '" + country + "', '" + _type + "', '" + score + "', '" + scoreUserNum + "', '" + quote + "', '" + detailLink
        # MSSQL().ExecNonQuery(sql)


for url in urls:
    get_info(url)
