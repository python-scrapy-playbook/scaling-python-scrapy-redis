# Python Scrapy - Intro to scraping at scale
In this repo we have the code that we use in our Youtube video.
Feel free to clone it and play around with it

# Getting Started - Cheat Sheet
Useful commands below:
1. Clone this project: `git clone https://github.com/python-scrapy-playbook/scaling-python-scrapy-redis.git`
2. Create a Python Virtual Environment in the project: `python3 -m venv venv`
3. Activate the Python Virtual Environment: `source venv/bin/activate`
4. Install Scrapy using pip: `pip install scrapy`
5. Install Scrapy using pip: `pip install scrapy-redis`
6. Add the urls to redis: `python3 add-urls-to-redis.py`
7. Running the scrapy project: `scrapy crawl scrape_quotes_worker` 


# Signup for a free redis account
You can sign up here: https://redis.com/try-free/

# Update your settings.py:
Update the REDIS_URL in settings.py to contain your redis details.
It should look something like the following:
`REDIS_URL = 'redis://<username>:<password>@<redis-connection-url>:<redis-port-number>'`





