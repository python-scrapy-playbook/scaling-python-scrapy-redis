import redis
from redis import from_url

# Create a redis client
redisClient = redis.from_url('redis://<username>:<password>@<redis-connection-url>:<redis-port-number>')

# Push URLs to Redis Queue
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/1/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/2/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/3/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/4/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/5/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/6/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/7/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/8/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/9/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/10/")
