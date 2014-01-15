#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
from model.price import Price

URLs = ["http://www.asos.com/es/ASOS/ASOS-Denim-Shirt-in-Long-Sleeve-with-Leopard-Print/Prod/pgeproduct.aspx?iid=3520721&cid=3602&sh=0&pge=0&pgesize=36&sort=-1&clr=Grey", "http://www.asos.com/es/Vaqueros-acampanados-con-lavado-medio-de-ASOS/545mu/?iid=2962382&cid=5230&sh=0&pge=0&pgesize=36&sort=-1&clr=Blue&mporgp=L0FTT1MvQVNPUy1GbGFyZS1KZWFuLUluLU1pZC1XYXNoL1Byb2Qv"]

class WebParser:
   
    price = Price()
    saleprice = Price()
 
    def parse(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text)

    def properparse(soup):
        pass
