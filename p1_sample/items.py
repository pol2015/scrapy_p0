# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class P1SampleItem(scrapy.Item):
#class P1SampleItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #title = Field()
    #link = Field()

    title_url_name = Field()
    author = Field()
    price = Field()
    
#pass
