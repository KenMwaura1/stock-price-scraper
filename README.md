## Badges 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
# Daily Stock Price Scraper 
Web scraper utilizing scrapy to scrape live stock prices from the Nairobi Stock Exchange. 
The prices are then saved in Postgres Database after each scrape, we use sqlalchemy as ORM 
and psycopg2 as database connector. 

The accompanying article(part one) can be found [here](https://dev.to/ken_mwaura1/daily-share-price-notifications-using-python-sql-and-africas-talking-part-one-17p)
Part Two detailing deployment and notification [here](https://dev.to/ken_mwaura1/daily-share-price-notifications-using-python-sql-and-africas-talking-part-two-37db)

The actual platform we are scraping is [afx](https://afx.kwayisi.org/nseke/) website. 
## Getting Started 
### Prerequisites
- Python and pip (I am currently using 3.9.2) Any version above 3.5 should work.
- An [Africas Talking account](https://account.africastalking.com/auth/register/).
    - Api Key and username from your account. Create an app and take note of the api key.
- Postgresql Database.
    - This could either be installed locally or via  [docker](https://www.docker.com/).
      This [article](https://blog.crunchydata.com/blog/easy-postgresql-12-and-pgadmin-4-setup-with-docker) is an awesome resource on how to get Postgresql and pgadmin4  installed as containers.
      
    Create a database `nse_scraper `. Either using SQL or 3-party client like pgadmin4 or [dbeaver](https://dbeaver.io/)

## Installation

Clone this repo

```bash 
  git clone https://github.com/KenMwaura1/stock-price-scraper
```
## Step 1
Change into the directory

`cd stock-price-scraper`
## Step 2
Create a virtual environment (venv) to hold all the required dependencies.Here we use
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
## Step 6 - Deployment
Heroku account registration First and foremost, you would need to register an account with Heroku, it’s free!
Installing Heroku CLI After your account registration, let’s use Heroku CLI to create and manage our project. You may check out the installation steps for other OS here.
```shell
# for arch-linux
sudo pacman -S heroku 
```
To log in using Heroku’s CLI, simply cd to your project folder and run `heroku login`.
```shell
$ cd nse_scraper 

$ heroku login 

heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/xxxx-xxxx-xxxx-xxxx-xxxx?requestor=xxxx.xxxx.xxxxLogging in... done
Logged in as &*^@gmail.com

...
```
### Git 
Checkout the `heroku_deployment` branch.
```shell
git checkout heroku_deployment
```
At this stage, you should already have set up your project with git init and git commit etc. The next steps are to turn your project into a git repository and push it to Heroku.
```shell
# i. To create a Heroku application:
$ heroku apps:create daily-nse-scrape

# ii. Add a remote to your local repository:
$ heroku git:remote -a daily-nse-scraper

# iii. Deploy your code
$ git push heroku heroku_deployment:main
```
Tweak the project name as necessary. 
### Setup free tier managed PostgreSQL service on Heroku
This step is fairly simple, simply go to the ‘Resources’ tab on your Heroku dashboard and look for ‘Heroku Postgres’, select the free tier (or whichever you deem fit).
Finally, adjust your Scrapy project’s connection to your database accordingly.

```shell
# settings.py

# POSTGRES SETTINGS
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASS")
database = os.environ.get("POSTGRES_DB")
drivername = "postgresql"
DATABASE = f"{drivername}://{username}:{password}@{host}:{port}/{database}"

# Or alternatively:
DATABASE_CONNECTION_STRING = ‘postgres://xxxx:xxxx@ec2-xx-xxx-xxx-xx.compute-1.amazonaws.com:5432/xxxxxx
```
Ensure you add your configuration variables in ‘Settings’ → ‘Reveal Config Vars‘. This will allow Heroku to get and set the required environment configuration for our web scraper to run.



## License

[MIT](https://choosealicense.com/licenses/mit/)

