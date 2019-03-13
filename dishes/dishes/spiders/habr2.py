import scrapy
from ..items import PostItem


class HabrSpider(scrapy.Spider):
    name = "habr2"
    start_urls = ['https://habr.com/ru/']

    def parse(self, response):
        page = response.xpath(
            "//ul[contains(@class, 'toggle-menu toggle-menu_pagination')]/@href").extract()
        posts_link = response.xpath(
            "//a[contains(@class, 'post__title_link')]/@href").extract()
        for i in posts_link:
            yield scrapy.Request(i, callback=self.parse_post)

    def parse_post(self, response):
        fields_item = PostItem()
        fields_item['title'] = response.xpath(
            "//span[contains(@class, 'post__title-text')]/text()").extract_first()
        fields_item['image'] = response.xpath(
            "//div[contains(@class, 'post__text post__text-html js-mediator-article')]/img/@src").extract_first()
        fields_item['description'] = ' '.join(response.xpath(
            "//div[contains(@class, 'post__text post__text-html js-mediator-article')]//text()").extract()).rstrip().rstrip()
        return fields_item
