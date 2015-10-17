# -*- coding: utf-8 -*-

import scrapy

class StockSpider(scrapy.Spider):
    name = 'Stock'
    allowed_domains = ['']
    start_urls = []
    
    def parse(self, response):
        pass
     