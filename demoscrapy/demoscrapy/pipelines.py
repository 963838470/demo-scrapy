# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class DemoscrapyPipeline(object):
    def __init__(self):
        self.f = open("itcasr_pipeline.json", "w", encoding='utf8')
        print("劲来了")

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        self.f.write(content.encode('utf-8').decode('unicode_escape'))
        return item

    def close_spider(self, spider):
        self.f.close()
