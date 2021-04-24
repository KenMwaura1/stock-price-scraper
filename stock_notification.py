from nse_scraper.models import StockData, db_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

import africastalking as at

engine = db_connect()
Session = sessionmaker(bind=engine)
session = Session()
ticker_data = []


# TODO: Add a function to notify client once the price changes

def stock_query():
    sq = session.query(StockData.id, StockData.stock_ticker,
                       StockData.stock_price).filter(StockData.stock_ticker == "SCOM")

    for id, ticker, price in sq.order_by(desc(StockData.id)).limit(1):
        print(id, ticker, price)
        new_data = {'stock_id': id, 'stock_ticker': ticker, 'stock_price': price}
        return new_data


t = stock_query()
print(t['stock_price'])


def stock_notification():
    pass
