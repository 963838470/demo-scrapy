# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    Title = scrapy.Field()
    OtherTitle = scrapy.Field()
    ImgSrc = scrapy.Field()
    Playable = scrapy.Field()
    Director = scrapy.Field()
    Performer = scrapy.Field()
    Year = scrapy.Field()
    Country = scrapy.Field()
    Type = scrapy.Field()
    Score = scrapy.Field()
    ScoreUserNum = scrapy.Field()
    Quote = scrapy.Field()
    DetailLink = scrapy.Field()
