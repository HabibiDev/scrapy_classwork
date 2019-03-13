import scrapy
from ..items import PostItem


class HabrSpider(scrapy.Spider):
    name = "habr"
    start_urls = ['https://habr.com/ru/company/itsumma/blog/443490/',]

    def parse(self, response):
        fields_item = PostItem()
        fields_item['title'] = response.xpath(
            "//span[contains(@class, 'post__title-text')]/text()").extract_first()
        fields_item['image'] = response.xpath(
            "//div[contains(@class, 'post__text post__text-html js-mediator-article')]/img/@src").extract_first()
        fields_item['description'] = ' '.join(response.xpath(
            "//div[contains(@class, 'post__text post__text-html js-mediator-article')]//text()").extract()).rstrip().rstrip()
        return fields_item
