#!/usr/bin/python

import sqlite3

from parsers.asosparser import AsosParser
from helpers import uadatabase

def main():
    if not uadatabase.check_database():
        uadatabase.create_database() 
    sqcon = sqlite3.connect('uadata.db')
    sqcon.row_factory = sqlite3.Row
    sqcur = sqcon.cursor()
    ap = AsosParser()
    for row in sqcur.execute('SELECT * FROM product'):
        ap.parse(row['url'])
        print(ap.price.price)

if __name__ == "__main__":
    main()
