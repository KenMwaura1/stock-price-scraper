[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
# stock-price-scraper
Web scraper utilizing scrapy to scrape live stock prices from the Nairobi Stock Exchange. 
The prices are then saved in Postgres Database after each scrape, we use sqlalchemy as ORM 
and psycopg2 as database connector. 
The actual platform we are scraping is [afx](https://afx.kwayisi.org/nseke/)
## Getting Started 
### Prerequisites
- Python and pip (I am currently using 3.9.2) Any version above 3.5 should work.
- An [Africas Talking account](https://account.africastalking.com/auth/register/).
    - Api Key and username from your account. Create an app and take note of the api key.
- Postgresql Database.
    - This could either be installed locally or via docker 