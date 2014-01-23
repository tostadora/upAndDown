#!/usr/bin/python

import sys
import os
import requests
from bs4 import BeautifulSoup

from model.price import Price


class WebParser:
   
    price = Price()
    saleprice = Price()
 
    def parse(self, url):
        proxies = { 'http' : os.environ['http_proxy'] }
        r = requests.get(url, proxies = proxies)
        soup = BeautifulSoup(r.content)
        self.properparse(soup)

    def properparse(self, soup):
        pass
