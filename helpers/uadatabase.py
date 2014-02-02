import os.path
import sqlite3

def create_database():
    sqcon = sqlite3.connect('uadata.db')
    sqcur = sqcon.cursor()
    sqcur.execute("""CREATE TABLE product (product_id, url, name)""")
    sqcur.execute("""CREATE TABLE price (price_id, product_id, day, price, on_sale)""")
    sqcon.commit()
    sqcon.close()
    return

def connect():
    return sqlite3.connect('uadata.db')

def check_database():
    return os.path.isfile('uadata.db')
