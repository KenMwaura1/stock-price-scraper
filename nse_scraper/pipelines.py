# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
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
        instance = session.query(StockData).filter_by(**item).on_or_one()
        if instance:
            return instance
        stock_data = StockData(**item)
        try:
            session.add(stock_data)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"we have a problem, houston {e}")
            raise
        finally:
            session.close()
        return item
