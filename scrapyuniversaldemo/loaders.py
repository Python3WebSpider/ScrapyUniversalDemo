from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Identity, Compose


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)
