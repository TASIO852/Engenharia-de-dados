import scrapy

class TripadvisorItem(scrapy.Item):
    author = scrapy.Field()
    address = scrapy.Field()
    title = scrapy.Field()
    comment = scrapy.Field()
    date = scrapy.Field()

