# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

def filter_strip(value):
	return [s.strip() for s in value]

class LectureItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
	title    = scrapy.Field(input_processor=filter_strip)
	lecturer = scrapy.Field(input_processor=filter_strip)
	date     = scrapy.Field(input_processor=filter_strip)
	place    = scrapy.Field(input_processor=filter_strip)


