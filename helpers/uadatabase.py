import os.path
import sqlite3

def create_database():
    sqcon = sqlite3.connect('uadata.db')
    sqcur = sqcon.cursor()
    sqcur.execute("""CREATE TABLE product (product_id, url, name)""")
    sqcon.commit()
    sqcon.close()
    return

def check_database():
    return os.path.isfile('uadata.db')
