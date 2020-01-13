import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
#        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
#        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
        'https://www.ptt.cc/bbs/NBA/M.1578868205.A.978.html',
        'https://www.ptt.cc/bbs/NBA/M.1578875405.A.18B.html'
    ]

    process = CrawlerProcess(get_project_settings())
    process.crawl('Day028Cralwer', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()
