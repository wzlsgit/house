# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcbcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    harea = scrapy.Field()
    hareasign = scrapy.Field()
    hsign = scrapy.Field()
    hreserve = scrapy.Field()
    hsurplus = scrapy.Field()
    htime = scrapy.Field()


