import scrapy


class VagalumeSpider(scrapy.Spider):
    name = "vagalume"
    start_urls = [
            'https://www.vagalume.com.br/top100/artistas/',
            #'https://www.vagalume.com.br/rosa-de-saron/',
            #'https://www.vagalume.com.br/rosa-de-saron/sem-voce.html',
    ]


    def parse_song(self, response):
        yield {
            'lyric': response.css("div#lyr_original div::text").extract(),
        }


    def parse_band(self, response):
        for a in response.css("div#artSongs ol li[itemprop=tracks] a")[:5]:
            yield response.follow(a, callback=self.parse_song)


    def parse(self, response):
        for a in response.css('div.topArt li.vArtH a')[:5]:
            yield response.follow(a, callback=self.parse_band)

