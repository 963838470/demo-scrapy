# -*- coding: utf-8 -*-
import scrapy
import re
import os
import urllib
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode

        hxs = Selector(response)  # 创建查询对象，HtmlXPathSelector已过时

        if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):  # 如果url能够匹配到需要爬取的url，就爬取
            # 匹配到大的div下的所有小div（每个小div中包含一个图片）
            items = hxs.xpath('//div[@class="item_list infinite_scroll"]/div')

            for i in range(len(items)):  # 遍历div个数
                # 查询所有img标签的src属性，即获取校花图片地址
                src = hxs.xpath(
                    '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
                # 获取span的文本内容，即校花姓名
                name = hxs.xpath(
                    '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
                school = hxs.xpath(
                    '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()  # 校花学校

                if src:
                    # 拼接实际路径,因为.extract()会返回一个list，但是我们是依次取得div，所以是取第0个
                    absoluteSrc = "http://www.xiaohuar.com" + src[0]
                    file_name = "%s_%s.jpg" % (
                        school[0], name[0])  # 拼接文件名，学校_姓名
                    # 拼接这个图片的路径，我是放在F盘的pics文件夹下
                    desktop = os.path.join(
                        os.path.expanduser("~"), 'Desktop', 'pics')
                    if os.path.exists(desktop) == False:
                        os.mkdir(desktop)
                    file_path = os.path.join(desktop, file_name)
                    # 接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径
                    urllib.request.urlretrieve(absoluteSrc, file_path)

            all_urls = hxs.xpath('//a/@href').extract()  # 提取界面所有的url
            for url in all_urls:  # 遍历获得的url，如果满足条件，继续爬取
                if url.startswith('http://www.xiaohuar.com/list-1-'):
                    yield Request(url, callback=self.parse)
