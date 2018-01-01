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
        print('*' * 100)
        for node in nodes:
            title = node.css(".title::text").extract()
            p = node.css(".bd>p::text").extract()[0].split("<br>")
            print("n" * 100)
            print(node)
            print("n" * 100)
            item = DoubanItem()
            item["Title"] = title[0]
            item["OtherTitle"] = ((title[1].replace("\xa0/\xa0", "") + "/") if len(title) > 1 else "") + \
                node.css(".other::text").extract()[0].replace(
                    "\xa0/\xa0", "").replace(" ", "")

            item["ImgSrc"] = node.css(".pic>a>img::attr(src)").extract()[0]
            if len(node.css(".playable::text").extract()) > 0:
                item["Playable"] = node.css(".playable::text").extract()[0]
            item["Director"] = p[0]
            # item["Performer"] =
            item["Year"] = node.re("(.*)\xa0/\xa0")
            # item["Country"] =
            # item["Type"] =
            # item["Score"] =
            # item["ScoreUserNum"] =
            # item["Quote"] =
            item["DetailLink"] = node.css(".pic>a::attr(href)").extract()[0]
            yield item
        print('*' * 100)
