# -*- coding: utf-8 -*-

# Scrapy settings for lecture project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lecture'

SPIDER_MODULES = ['lecture.spiders']
NEWSPIDER_MODULE = 'lecture.spiders'

ITEM_PIPELINES = {
    'lecture.pipelines.JsonWriterPipeline': 300,
    'lecture.pipelines.LecturePipeline': 500,
    'lecture.pipelines.WordWriterPipeline':1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lecture (+http://www.yourdomain.com)'
