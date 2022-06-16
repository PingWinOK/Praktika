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
        for category in response.xpath('.//ul[@class="clear"]/li/div[@class="header__catalog-dropdown clear"]').css("a::attr(href)").extract():
            yield response.follow("https://www.tradebox.dn.ua"+category, callback=self.parse_item)


    def parse_item(self, response):
        yield {
            "Название": response.xpath('.//a[@class="card__title"]/text()').get(),
            "Категория": response.xpath('.//div[@class="breadcrumbs"]').css("li::text").get(),
            "Цена": " ".join(response.xpath('.//div[@class="card__price"]/text()').get().split()),
            "Наличие": response.xpath('.//div[@class="card__availability"]/text()').get(),
            "Ссылка": response.css("a.card__title::attr(href)").get()

        }
