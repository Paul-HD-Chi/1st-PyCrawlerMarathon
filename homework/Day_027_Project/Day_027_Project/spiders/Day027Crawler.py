# -*- coding: utf-8 -*-
import scrapy


class Day027crawlerSpider(scrapy.Spider):
    name = 'Day026Crawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/NBA/M.1578619525.A.5BF.html']
    
    def start_requests(self):
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse, cookies={'over18': '1'})

    def parse(self, response):
        pass
