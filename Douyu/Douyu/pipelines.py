# -*- coding: utf-8 -*-
''' 管道文件 '''
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):
    ''' 处理管道类 '''

    def get_media_requests(self, item, info):
        vertical_src = item["vertical_src"]
        yield scrapy.Request(vertical_src)

    # def item_completed(self, results, item, info):
    #     if isinstance(item, dict) or self.images_result_field in item.fields:
    #         item[self.images_result_field] = [x for ok, x in results if ok]
    #     return item
