# -*- coding: utf-8 -*-
import scrapy
#from sqlHelper import MSSQL
from Douban.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    #start_urls = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    start_urls = ['https://movie.douban.com/top250?start=0']

    def parse(self, response):
        
        nodes = response.css("ol.grid_view div.item")
        for node in nodes:
            item = DoubanItem()
            item["Title"] = node.css(".title::text").extract()[0]
            item["OtherTitle"] =node.css(".other::text").extract()[0].replace("&nbsp;/&nbsp;","")
            print('*' * 100)
            print(item["OtherTitle"])
            print(item["OtherTitle"].replace(" / ",""))
            print('*' * 100)
            # item["ImgSrc"] =
            # item["Playable"] =
            # item["Director"] =
            # item["Performer"] =
            # item["Year"] =
            # item["Country"] =
            # item["Type"] =
            # item["Score"] =
            # item["ScoreUserNum"] =
            # item["Quote"] =
            # item["DetailLink"] =
            yield item
