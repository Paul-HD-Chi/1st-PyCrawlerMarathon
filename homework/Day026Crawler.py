# -*- coding: utf-8 -*-
import scrapy


class Day026crawlerSpider(scrapy.Spider):
    name = 'Day026Crawler'
    allowed_domains = ['www.ptt.cc/bbs/Stock']
    start_urls = ['http://www.ptt.cc/bbs/Stock/M.1578022091.A.734.html']
    
    def start_requests(self):
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        pass
