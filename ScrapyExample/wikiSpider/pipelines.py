# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime
from string import whitespace
from itemadapter import ItemAdapter
from wikiSpider.items import Article

'''
*** NOTE ***

1) settings.py 의 # Configure item pipelines 부분이 활성화되면, 이곳에 데이터 처리 위임!
   ㄴ 비동기적으로 데이터를 처리하므로, 전체적인 크롤링 속도 증가

2) process_item 에 데이터 처리 내용 작성
   ㄴ 날짜시각과 본문에 대해서 적절하게 데이터 처리
   ㄴ 만약 다양한 Item 객체가 있고 그에 따른 다양한 처리가 있다면, isinstance() 활용 필요
'''

class WikispiderPipeline:

	def process_item(self, article, spider):
		if isinstance(article, Article):
			article['lastUpdated'] = article['lastUpdated'].replace(
				'This page was last edited on', '')
			article['lastUpdated'] = article['lastUpdated'].strip()
			article['lastUpdated'] = datetime.strptime(
				article['lastUpdated'], '%d %B %Y, at %H:%M')
			article['lastUpdated'] = article['lastUpdated'].strftime('%Y-%m-%d %H:%M')
			article['text'] = [line for line in article['text'] if line not in whitespace]
			article['text'] = ''.join(article['text'])
			return article
