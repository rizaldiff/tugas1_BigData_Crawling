import scrapy

class CNNIndonesiaSpider(scrapy.Spider):
    name = 'cnn'
    start_urls = ['https://www.cnnindonesia.com/indeks']

    def parse(self, response):
        # Ambil semua artikel berita dari halaman indeks
        articles = response.css('article')

        for article in articles:
            title = article.css('h2::text').get()
            link = article.css('a::attr(href)').get()

            yield {
                'Judul': title,
                'Link': link,
                "Media": "CNNIndonesia.com"
            }

        # Lanjutkan ke halaman berikutnya jika ada
        next_page = response.css('.pagination .next a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)