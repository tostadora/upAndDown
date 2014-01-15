#!/usr/bin/python

from parsers.webparser import WebParser

class AsosParser(WebParser):

    def properparse(soup):
        reslist = soup.find_all("span", class_="product_price_details")
        for el in reslist:
            print("normal: " + el.string)
            price = el.string
        reslist = soup.find_all("span", class_="previousprice")
        for el in reslist:
            print("rebajas: " + el.string)
            sale = 1
            saleprice = el.string
