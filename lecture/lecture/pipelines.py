# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from docx import Document
from docx.shared import Inches
import json
doc = Document()

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
    	# item['title']=item['title'].decode('utf-8')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class LecturePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        try:
        	lecturer = item['lecturer']
        except:
        	lecturer = [u""]
        place = item['place']
        date = item['date']

        s=u""
        if lecturer != u"":
        	s = s + title[0]+"\n"+date[0]+"-"+date[1]+"\n"+place[0]

       	p = doc.add_paragraph(s)


class WordWriterPipeline(object):

	def process_item(self, item, spider):
		doc.save("demo.docx")


