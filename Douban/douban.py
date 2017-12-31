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
    times = re.findall('<br>(.*?)&nbsp', wb_data.text, re.S)
    places = re.findall('&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;', wb_data.text)
    levels = soup.select('span.rating_num')
    quotes = soup.select('span.inq')
    for name, time, place, level, quote in zip(names, times, places, levels, quotes):
        info = {
            'name': name.get_text().split('/')[0].split('\n')[1],
            'time': time.split('\n')[1].replace(' ', ''),
            'place': place,
            'level': level.get_text(),
            'quote': quote.get_text()
        }
        top250.append(info)


for url in urls:
    get_info(url)

file = open('电影.html', 'w', encoding='utf-8')
file.write("<table>")
for movie in top250:
    file.write("<tr><td>" + movie["name"] + "</td><td>" + movie["level"] + "</td><td>" +
               movie["time"] + "</td><td>" + movie["place"] + "</td><td>" + movie["quote"] + "</td></tr>")
file.write("</table>")
file.close()
