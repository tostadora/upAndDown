#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
from model.price import Price


class WebParser:
   
    price = Price()
    saleprice = Price()
 
    def parse(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        self.properparse(soup)

    def properparse(self, soup):
        pass
