#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
from model.price import Price


class WebParser:
   
    price = Price()
    saleprice = Price()
 
    def parse(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        properparse(soup)

    def properparse(soup):
        pass
