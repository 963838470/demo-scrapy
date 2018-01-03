import requests
from bs4 import BeautifulSoup
import re

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
    for name, src, playable, p, place, level, quote, director, performer, scoreUserNum in zip(names, srcs, playables, ps, places, levels, quotes, directors, performers, scoreUserNums):
        pc = p.split('&nbsp;/&nbsp;')
        info = {
            'Title': name.get_text().split('\n')[1],
            'OtherTitle': name.get_text().replace('\xa0', '').replace('\n', '').replace(name.get_text().split('\n')[1] + "/", ""),
            'ImgSrc': src.attrs['src'],
            'Playable': playable.get_text(),
            'Year': pc[0],
            'Country': pc[1],
            'Score': level.get_text(),
            'Quote': quote.get_text(),
            'DetailLink': name.attrs['href'],
            'Director': director,
            'Performer': performer,
            'Type': pc[2],
            'ScoreUserNum': scoreUserNum.get_text().replace('人评价', '')}
        print(info)
        top250.append(info)


for url in urls:
    get_info(url)

