import csv
from scrapy.crawler import CrawlerProcess
import scrapy


class holidaysSpider(scrapy.Spider):
    name = 'holidays'
    start_urls = ['https://www.officeholidays.com/countries/india/2021']

    def parse(self, response):
        my_list = ["region ","govt ","nap ","country "]
        for x in my_list:
            for ele in response.xpath('//tbody/tr[@class="'+x+'"]'):
                dict = {
                       'days': ele.xpath('td[1]/text()').getall(),
                       'date': ele.xpath('td[@style="white-space:nowrap;"]/time/text()').getall(),
                       'hol_type': ele.xpath('td[@style="white-space:nowrap;"]/text()').getall(),
                       'holidays': ele.xpath('td/a[@class="country-listing"]/text()').getall(),
                       'states': ele.xpath('td[@class="hide-ipadmobile"]/text()').getall(),
                }
                #print(x + " Type")
                #print(dict)
                yield(dict)
