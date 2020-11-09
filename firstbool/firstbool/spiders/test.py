import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
