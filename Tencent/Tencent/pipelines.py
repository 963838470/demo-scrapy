# -*- coding: utf-8 -*-
''' 管道文件 '''
import json


class TencentPipeline(object):
    ''' 处理管道类 '''

    def __init__(self):
        self.f = open("tencent.json", "w", encoding='utf8')

    def process_item(self, item, spider):
        ''' 处理实体 '''
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
