# -*- coding: utf-8 -*-
import scrapy
import string
from uzbdict.items import DictionaryItem
import html2text
import re

eng_alphabet = string.lowercase
uzb_alphabet = re.sub('w', '', eng_alphabet)
uzb_alphabet = re.sub('c', '', uzb_alphabet)
uzb_alphabet = [letter for letter in uzb_alphabet] + ["o\xe2\x80\x98", "g\xe2\x80\x98", "sh", "ch"]


class UzbDictSpider(scrapy.Spider):
    name = "uzbdictspider"
    allowed_domains = ["www.uzbek-dictionary.com"]

    def start_requests(self):
        eng_start_urls = ['http://www.uzbek-dictionary.com/trans.php?trans_text=%s&trans_lang=en_uz&trans_number=10000' % i \
                        for i in eng_alphabet]
        uzb_start_urls = ['http://www.uzbek-dictionary.com/trans.php?trans_text=%s&trans_lang=uz_en&trans_number=10000' % i \
                        for i in uzb_alphabet]
        all_urls = eng_start_urls + uzb_start_urls
        return [scrapy.Request(url=start_url) for start_url in all_urls]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        item = DictionaryItem()
        words = hxs.xpath('/html/body/div[@class="frame"]/a/text()').extract()
        separators = hxs.xpath('/html/body/div[@class="frame"]/span[@class="seperator"]/text()').extract()
        translations = hxs.xpath('/html/body/div[@class="frame"]/div[@class="meaning_wrapper"]').extract()
        trans_items = [html2text.html2text(t).strip() for t in translations]
        for x in range(len(words)):
            item['word'] = words[x]
            item['translation'] = trans_items[x]
            yield item
        # dictionary = dict(zip(letters, trans_items))
        # print dictionary
