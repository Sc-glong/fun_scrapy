import scrapy
from fun.items import FunItem

class GuoguoSpider(scrapy.Spider):
    name = 'guoguo'
    allowed_domains = ['sc-glong.github.io/']
    start_urls = ['https://sc-glong.github.io/archives/']

    def parse(self, response):
        node_list = response.xpath("//article[@class='archive-item']")

        for node in node_list:
            item = FunItem()
            title = node.xpath("./a/text()").extract()
            time = node.xpath("./span/text()").extract()

            item['title'] = title[0]
            item['time'] = time[0]

            # 返回提取到的每个item，返回给管道文件，同时还会回来继续执行后面的代码
            yield item
