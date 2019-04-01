# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.ar']
	start_urls = ['https://celulares.mercadolibre.com.ar/xiaomi/redmi/note-6-pro/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="pagination__next"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[contains(@class,"item__title")]/a')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = MercadoItem()
		#info de producto
		ml_item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		ml_item['precio'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
		ml_item['condicion'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		ml_item['ubicacion'] = response.xpath('normalize-space(//p[contains(@class, "card-description")])').extract()
		ml_item['vendedor_url'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
		self.item_count += 1
		if self.item_count > 20:
			raise CloseSpider('item_exceeded')
		yield ml_item
