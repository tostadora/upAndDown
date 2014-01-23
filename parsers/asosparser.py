#!/usr/bin/python

from parsers.webparser import WebParser

class AsosParser(WebParser):

    def properparse(self, soup):
        reslist = soup.find_all("span", "product_price_details")
        for el in reslist:
            self.price.price = el.string
            self.price.sale = 0
        reslist = soup.find_all("span", class_="previousprice")
        for el in reslist:
            self.saleprice.price = el.string
            self.saleprice.sale = 1
