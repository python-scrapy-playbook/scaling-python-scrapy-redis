
import scrapy
from scrapy_redis.spiders import RedisSpider

class QuotesSpider(RedisSpider):
    name = "scrape_quotes_worker"
    redis_key = 'quotes_queue:start_urls'
    # Number of url to fetch from redis on each attempt
    redis_batch_size = 1
    # Max idle time(in seconds) before the spider stops checking redis and shuts down
    max_idle_time = 7
            
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
