## Badges 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
# Daily Stock Price Scraper 
Web scraper utilizing scrapy to scrape live stock prices from the Nairobi Stock Exchange. 
The prices are then saved in Postgres Database after each scrape, we use sqlalchemy as ORM 
and psycopg2 as database connector. 

The accompanying article can be found [here](https://dev.to/ken_mwaura1/daily-share-price-notifications-using-python-sql-and-africas-talking-part-one-17p)

The actual platform we are scraping is [afx](https://afx.kwayisi.org/nseke/) website. 
## Getting Started 
### Prerequisites
- Python and pip (I am currently using 3.9.2) Any version above 3.5 should work.
- An [Africas Talking account](https://account.africastalking.com/auth/register/).
    - Api Key and username from your account. Create an app and take note of the api key.
- Postgresql Database.
    - This could either be installed locally or via  [docker](https://www.docker.com/).
      This [article](https://blog.crunchydata.com/blog/easy-postgresql-12-and-pgadmin-4-setup-with-docker) is an awesome resource on how to get Postgresql and pgadmin4  installed as containers.

## Installation

Clone this repo

```bash 
  git clone https://github.com/KenMwaura1/stock-price-scraper
```
## Step One
Change into the directory

`cd stock-price-scraper`
## Step 2
Create a virtual environment (venv) to hold all of the required dependecies.Here we use
the built-in venv module.

`python -m venv env`

Activate the virtual environment

` source env/bin/activate`

Alternatively if you are using [pyenv](https://github.com/pyenv/pyenv).


```shell 
pyenv virtualenv nse_scraper
pyenv activate nse_scraper
   ```
## Step 3
Install the required dependencies:

`pip install -r requirements `

## Step 4 
Change into the nse_scraper folder and create an environment file. 
```shell
cd nse_scraper
touch .env 
```
Add your credentials as specified in the example file.

OR

Copy the provided  example and edit as required:

` cp .env-example env`

## Step 5
Navigate up to the main folder *stock-price-scraper*
Run the scraper and check the logs for any errors . 
```shell
cd .. 
scrapy crawl afx_scraper
```
or 
Run the scraper and have it output to a json file to preview. 
```shell
scrapy crawl afx_scraper -o test.json 
```
## License

[MIT](https://choosealicense.com/licenses/mit/)

