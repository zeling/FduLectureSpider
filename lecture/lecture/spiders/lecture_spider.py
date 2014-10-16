# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.loader import ItemLoader
from lecture.items import LectureItem


class LectureSpider(scrapy.Spider):
	name            = "fduLectures"
	allowed_domains = ["fudan.edu.cn"]
	start_urls      = ["http://news.fudan.edu.cn/calendar/?a=list&m=recent&range=7"]

	def parse(self, response):
		# with open("lecture.html","wb") as f:
		# 	f.write(response.body)
		# l = ItemLoader(item=LectureItem(), response=response
		# 	)
		# l.add_css('title','.eventlist>dl>dd>h4>a::text')
		# l.add_css('lecturer','.eventlist>dl>dd>div>p::text')
		# l.add_css('place','.eventlist>dl>dd>div>p::text')
		# l.add_css('date','.eventlist>h3::text')
		# l.add_css('time','.eventlist>dl>dt::text')
		# return l.load_item()
		for s in response.xpath('//html/body/div/dl/dd/h4/a/@href').extract():
			url = 'http://news.fudan.edu.cn/calendar/?a=one&evid='+s[18:-1]
			yield scrapy.Request(url, callback=self.parseItem)


	def parseItem(self, response):
		l = ItemLoader(item=LectureItem(), response=response)
		l.add_css('title', '.eventdetail>h1::text')
		l.add_xpath('lecturer', '//tr[5]/td[2]/text()')
		l.add_xpath('place', '//tr[4]/td[2]/text()')
		l.add_xpath('date', '//tr[2]/td[2]/text()')
		l.add_xpath('date', '//tr[3]/td[2]/text()')
		return l.load_item()
		
		tds = response.xpath('//td/text()').extract()


		# lecturer = response.xpath('//table/tbody/tr[4]/td[2]').extract()
		# title    = response.css('.eventdetail>h1::text').extract()
		# place    = response.css('tbody > tr:nth-child(3) > td:nth-child(2) ::text').extract()
		# date     = response.css('div>table>tbody>tr:nth-child(1)>td:nth-child(2)::text').extract()
		# return LectureItem(
		# 	lecturer=lecturer,
		# 	title=title,
		# 	place=place,
		# 	date=date,
		# )


