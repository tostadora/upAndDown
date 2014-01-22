#!/usr/bin/python

from parsers.asosparser import AsosParser
import sqlite3

def main():
    sqcon = sqlite3.connect('uadata.db')
    url = "http://www.asos.com/es/Su%C3%A9ter-estilo-marinero-de-Esprit/6sh7u/?iid=3454356&cid=6993&sh=0&pge=0&pgesize=36&sort=-1&clr=Natural+white&mporgp=L0VzcHJpdC9Fc3ByaXQtRmlzaGVybWFucy1KdW1wZXIvUHJvZC8."
    ap = AsosParser()
    ap.parse(url)
    print(ap.price.price)

if __name__ == "__main__":
    main()
