import scrapy
from scrapy.crawler import CrawlerProcess
from crawlers.spiders.batdongsan import BatdongsanSpider

if __name__ == '__main__':
    process = CrawlerProcess(settings={
        "SCRAPY_SETTINGS_MODULE": "crawlers.settings"
    })
    process.crawl(BatdongsanSpider)
    process.start()