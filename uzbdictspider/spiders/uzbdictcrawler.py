# -*- coding: utf-8 -*-
import scrapy


class UzbDictSpider(scrapy.Spider):
    name = "uzbdictspider"
    allowed_domains = ["www.uzbek-dictionary.com"]
    start_urls = (
        'http://www.uzbek-dictionary.com/',
    )

    def parse(self, response):
        pass
