from typing import List, Any

from models import StockData, db_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
import africastalking as at
import os

at_username = os.environ.get("at_username")
at_api_key = os.environ.get("at_api_key")
mobile_number = os.environ.get("mobile_number")
# print(at_username, at_api_key)
# Initialize the Africas sdk py passing the api key and username from the .env file
at.initialize(at_username, at_api_key)
sms = at.SMS
account = at.Application

engine = db_connect()
Session = sessionmaker(bind=engine)
session = Session()
ticker_data = []


# TODO: Add a function to notify client once the price changes
# Create a function to query the Database for latest stock data
def stock_query():
    sq = session.query(StockData.id, StockData.stock_ticker, StockData.stock_name,
                       StockData.stock_price).filter(StockData.stock_ticker == "SCOM")

    for id, ticker, name, price in sq.order_by(desc(StockData.id)).limit(1):
        # print(id, name, ticker, price)
        new_data = {'stock_id': id, 'stock_name': name, 'stock_ticker': ticker, 'stock_price': price}
        return new_data


# Create a function to send a message containing the stock ticker and price
def stock_notification(stock_data: list, number: int):
    try:
        response = sms.send(stock_data, [number])
        print(account.fetch_application_data())
        print(response)
    except Exception as e:
        print(f" Houston we have a problem: {e}")


message: list[Any] = [f'{stock_query()["stock_name"]}, is now Kes {stock_query()["stock_price"]} per share']
# check if Safaricom share price is more than Kes 39 and send a notification.
if stock_query().get("stock_price") >= 39:
    # Call the function passing the message  and mobile_number as a arguments
    print(message)
    stock_notification(str(message), mobile_number)
