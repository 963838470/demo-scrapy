# -*- coding: utf-8 -*-
import json
import scrapy
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseURL = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        datas = json.loads(response.body)['data']
        if len(datas) == 0:  # 提取不到数据，退出
            return
        for data in datas:
            item = DouyuItem()
            item["nickname"] = data["nickname"]
            item["vertical_src"] = data["vertical_src"]

            yield item

        self.offset += 20
        yield scrapy.Request(self.baseURL + str(self.offset), callback=self.parse)
