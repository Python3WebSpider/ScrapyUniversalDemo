# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class MovieItem(Item):
    name = Field()
    cover = Field()
    categories = Field()
    published_at = Field()
    drama = Field()
    score = Field()
