import scrapy
import os

# https://www.tradebox.dn.ua
"""
реализовать спайдер для сбора всех товаров.
Сохранять необходимо название, категорию(инструмент, бытовая техника и т.д.),
цену, и полную ссылку на товар.
Формат выдачи любой, но лучше csv.
"""


class SPIDER(scrapy.Spider):
    name = 'TRADEBOX_SPIDER'
    allowed_domains = ['tradebox.dn.ua']
    start_urls = ['https://www.tradebox.dn.ua']

    def parse(self, response):
        for category in response.xpath(".//ul[@class='clear']/li").css("a::attr(href)").extract():
            yield response.follow(category,callback=self.parse_category)

    def parse_category(self, response):
        for podcategory in response.xpath(".//div[@class = 'typography cards-bottom']").css("a::attr(href)").extract():
            yield response.follow(podcategory,callback=self.parse_list_item)

    def parse_list_item(self, response):
        for item in response.xpath(".//div[@class = 'card']").css("a.card__title::attr(href)").extract():
            yield response.follow(item,callback=self.parse_item)

    def parse_item(self, response):
        yield {
            "Название": response.css("h1::text").get(),
            "Категория": response.xpath('.//div[@class="breadcrumbs"]/ul/li/a').css("a::text")[2].get(),
            "Цена": response.xpath('.//div[@class="product__price"]/span/text()').get(),
            "Наличие": response.xpath('.//div[@class="product__availability"]/text()').get(),
            "Ссылка": response.url

        }
