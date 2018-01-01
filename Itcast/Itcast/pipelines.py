import json


class ItcastPipeline(object):
    def __init__(self):
        self.f = open("itcasr_pipeline.json", "w", encoding='utf8')
        print("劲来了")

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        self.f.write(content.encode('utf-8').decode('unicode_escape'))
        return item

    def close_spider(self, spider):
        self.f.close()
