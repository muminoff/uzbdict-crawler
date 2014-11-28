# -*- coding: utf-8 -*-
import scrapy
import string
from uzbdict.items import DictionaryItem
import html2text


class UzbDictSpider(scrapy.Spider):
    name = "uzbdictspider"
    allowed_domains = ["www.uzbek-dictionary.com"]
    # start_urls = (
    #     'http://www.uzbek-dictionary.com/trans.php?trans_text=e&trans_lang=uz_en&trans_number=10000',
    # )

    def start_requests(self):
        start_urls = ['http://www.uzbek-dictionary.com/trans.php?trans_text=%s&trans_lang=uz_en&trans_number=10000' % i \
                        for i in string.lowercase]
        return [scrapy.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        item = DictionaryItem()
        letters = hxs.xpath('/html/body/div[@class="frame"]/a/text()').extract()
        separators = hxs.xpath('/html/body/div[@class="frame"]/span[@class="seperator"]/text()').extract()
        translations = hxs.xpath('/html/body/div[@class="frame"]/div[@class="meaning_wrapper"]').extract()
        # print len(letters), len(separators), len(translations)
        # print letters, len(letters)
        # print separators, len(separators)
        # print translations, len(translations)
        trans_items = [html2text.html2text(t).strip() for t in translations]
        dictionary = dict(zip(letters, trans_items))
        print dictionary
