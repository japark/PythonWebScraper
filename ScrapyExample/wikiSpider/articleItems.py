from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from wikiSpider.items import Article

'''
*** NOTE ***

1) 수집한 내용을 Item 객체에 저장 및 출력
   ㄴ items.py 에 Article 클래스 정의
   ㄴ 콘솔에 파이썬 딕셔너리 형태로 데이터 출력

2) 결과를 파일로 저장
   ㄴ csv 로 결과 저장 : scrapy runspider articleItems.py -o articles.csv -t csv
   ㄴ json 으로 결과 저장 : scrapy runspider articleItems.py -o articles.json -t json
   ㄴ xml 로 결과 저장 : scrapy runspider articleItems.py -o articles.xml -t xml

3) 콘솔에 난잡하게 출력되는 로그를 별도의 파일로 저장
   ㄴ scrapy runspider articleItems.py --logfile wiki.log
   ㄴ settings.py 의 LOG_LEVEL 항목으로 로그 수준 조정 (INFO/DEBUG/WARNING/ERROR/CRITICAL)
   ㄴ 콘솔에는 print() 에 의한 부분만 출력됨
'''

class ArticleSpider(CrawlSpider):
	name = 'articleItems'
	allowed_domains = ['wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
	rules = [
		Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
			callback='parse_items', follow=True),
	]

	def parse_items(self, response):
		article = Article()
		print(response.url)
		article['url'] = response.url
		article['title'] = response.css('h1::text').extract_first()
		article['text'] = response.xpath(
		  '//div[@id="mw-content-text"]//text()').extract()
		lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
		article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
		return article
