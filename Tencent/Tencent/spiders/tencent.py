# -*- coding: utf-8 -*-
'''爬虫执行页面'''
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    ''' 将页面的数据写入实体 '''
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURL = 'http://hr.tencent.com/position.php?&start'
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        nodes = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in nodes:
            item = TencentItem()
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            item['recruitNumber'] = node.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]
            print(item)
            yield item

        if self.offset < 2600:
            self.offset += 10
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
