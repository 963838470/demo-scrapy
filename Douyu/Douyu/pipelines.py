# -*- coding: utf-8 -*-
''' 管道文件 '''
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from Douyu.settings import IMAGES_STORE as image_store


class DouyuPipeline(ImagesPipeline):
    ''' 处理管道类 '''

    def get_media_requests(self, item, info):
        vertical_src = item["vertical_src"]
        yield scrapy.Request(vertical_src)

    def item_completed(self, results, item, info):
        path = [x["path"] for ok, x in results if ok]
        os.rename(image_store + path[0],
                  image_store + item["nickname"] + ".jpg")
        return item
