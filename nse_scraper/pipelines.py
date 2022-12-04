
# useful for handling different item types with a single interface
from sqlalchemy.orm import sessionmaker

from nse_scraper.models import StockData, create_items_table, db_connect


class NseScraperPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates stock_data table
        """
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        process item and store to database
        """
        session = self.Session()
        stock_data = StockData()
        stock_data.stock_name = item["name"]
        stock_data.stock_price = float(item["price"].replace(',', ''))
        stock_data.stock_ticker = item["ticker"]
        try:
            session.add(stock_data)
            session.commit()
            # query again
            obj = session.query(StockData).first()
            # print(obj.stock_ticker)
        except Exception as e:
            session.rollback()
            print(f"we have a problem, houston {e}")
            raise
        finally:
            session.close()
        return item
