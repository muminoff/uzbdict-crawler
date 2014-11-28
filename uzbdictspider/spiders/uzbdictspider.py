# -*- coding: utf-8 -*-
import scrapy
import string
from uzbdictspider.items import DictionaryItem


class UzbDictSpider(scrapy.Spider):
    name = "uzbdictspider"
    allowed_domains = ["www.uzbek-dictionary.com"]
    start_urls = (
        'http://www.uzbek-dictionary.com/index.php?trans_text=%s&trans_lang=uz_en',
    )

    def start_requests(self):
        pass
        # start_urls = ['http://www.uzbek-dictionary.com/index.php?trans_text=%s&trans_lang=uz_en' % i \
        #                 for i in string.lowercase]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        print hxs.xpath('/html/body/div[@class=\'frame\']/*/text()').extract()
