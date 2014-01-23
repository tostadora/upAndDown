import datetime

from model.currency import Currency

class Price:
    
    price = 0
    sale = False
    day = datetime.date.today()
    currency = Currency.EUROS
