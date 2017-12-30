# -*- coding: utf-8 -*-
'''爬取实体类'''
import scrapy


class TencentItem(scrapy.Item):
    '''定义实体类'''
    positionName = scrapy.Field()  # 职位名称
    positionLink = scrapy.Field()  # 职位详情链接
    positionType = scrapy.Field()  # 职位类别
    recruitNumber = scrapy.Field()  # 招聘人数
    workLocation = scrapy.Field()  # 工作地点
    publishTime = scrapy.Field()  # 发布时间
