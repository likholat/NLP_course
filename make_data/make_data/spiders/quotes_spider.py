import scrapy



urls = []
urls.append('https://psycheforum.ru/topic/165878-podruga-muzha/')
for i in range(2, 20):
    urls.append(f'https://psycheforum.ru/topic/165878-podruga-muzha/page/{i}/')

urls.append('https://psycheforum.ru/topic/154860-rushitsya-vtoroy-brak/')
for i in range(2, 110):
    urls.append(f'https://psycheforum.ru/topic/154860-rushitsya-vtoroy-brak/page/{i}/')

urls.append('https://psycheforum.ru/topic/135425-v-seme-seks-za-dengi-norma/')
for i in range(2, 70):
    urls.append(f'https://psycheforum.ru/topic/135425-v-seme-seks-za-dengi-norma/page/{i}/')

urls.append('https://psycheforum.ru/topic/147708-vlyubilas-v-zhenatogo-lyubovnika/')
for i in range(2, 37):
    urls.append(f'https://psycheforum.ru/topic/147708-vlyubilas-v-zhenatogo-lyubovnika/page/{i}/')


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = urls

    def parse(self, response):
        for quote in response.css('div.ipsQuote_contents'):
            yield {
                'text': ' '.join(s.strip().replace(u'\xa0', u' ') for s in quote.css('p::text').getall())
            }
