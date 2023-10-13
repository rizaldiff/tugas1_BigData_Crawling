import scrapy
import pandas as pd

class KompasSpider(scrapy.Spider):
    name = "kompas"
    start_urls = ["https://indeks.kompas.com/"]

    def parse(self, response):
        articles = response.css(".article__list")
        
        for article in articles:
            judul = article.css(".article__link::text").get()
            tanggal = article.css(".article__date::text").get()
            link = article.css(".article__link::attr(href)").get()
            
            yield {
                "Judul": judul,
                "Tanggal": tanggal,
                "Link": link,
                "Media": "Kompas.com"
            }
        
        next_page = response.css(".paging__link-next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)