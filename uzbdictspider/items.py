# -*- coding: utf-8 -*-
import scrapy


class DictionaryItem(scrapy.Item):
    letter = scrapy.Field()
    delimiter = scrapy.Field()
    translation = scrapy.Field()
