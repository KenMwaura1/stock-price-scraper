import scrapy
from bs4 import BeautifulSoup
import re


class AfxScraperSpider(scrapy.Spider):
    name = 'afx_scraper'
    allowed_domains = ['https://afx.kwayisi.org']
    start_urls = ['https://afx.kwayisi.org/nseke//']

    def parse(self, response):
        print("Processing: " + response.url)
        # Extract data using css selectors
        row = response.css('table tbody tr ')
        # use XPath and regular expressions to extract stock name and price
        raw_stock_price = row.xpath('td[4]').re('[0-9].*')
        raw_stock_name = row.xpath('td[2]').re('[A-Z].*')
        # create a function to remove html tags from the returned list
        cleaned_data = []

        def clean_stock_name(raw_name):
            clean_name = BeautifulSoup(raw_name, "lxml").text
            clean_name = clean_name.split('>')
            # cleaned_data.append(clean_name[1])
            # print(clean_name)
            return clean_name[1]

        def clean_stock_price(raw_price):
            clean_price = BeautifulSoup(raw_price, "lxml").text
            # cleaned_data.append(clean_price)
            # print(clean_price)
            return clean_price

        cn = [clean_stock_name(r_name) for r_name in raw_stock_name]
        print(len(cn))
        cs = [clean_stock_price(r_price) for r_price in raw_stock_price]
        print(len(cs))
        cc = [clean_stock_price(r_change) for r_change in raw_stock_change]
        print(cc)
        # using list slicing to remove the unnecessary data
        stock_change = cc[6:]
        cleaned_data = zip(cn, cs,stock_change)
        zl = list(cleaned_data)
        print(zl)
        for item in cleaned_data:
            scraped_data = {
                'name': item[0],
                'price': item[1],
                'stock_change': item[2]
            }
            # yield info to scrapy
            yield scraped_data
