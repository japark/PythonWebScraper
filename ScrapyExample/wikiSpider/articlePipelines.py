from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from wikiSpider.items import Article

'''
*** NOTE ***

1) 데이터 수집과 처리를 분리
   ㄴ 데이터를 처리하는 동안 계속 자료를 수집하므로, 전체적인 크롤링 속도 증가!
   ㄴ parse_items 함수에서의 데이터 처리는 최소화할 것

2) settings.py 에서 # Configure item pipelines 부분의 코드 코멘트 제거할 것!!!
   ㄴ pipelines.py 의 WikispiderPipeline 에서 데이터 처리 담당
'''

class ArticleSpider(CrawlSpider):
	name = 'articlePipelines'
	allowed_domains = ['wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
	rules = [
		Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
			callback='parse_items', follow=True),
	]

	def parse_items(self, response):
		article = Article()
		article['url'] = response.url
		article['title'] = response.css('h1::text').extract_first()
		article['text'] = response.xpath(
		  '//div[@id="mw-content-text"]//text()').extract()
		article['lastUpdated'] = response.css(
			'li#footer-info-lastmod::text').extract_first()
		return article
