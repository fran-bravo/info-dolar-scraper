from dolar.spiders.infodolar import InfodolarSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()

process.crawl(InfodolarSpider)
process.start()
