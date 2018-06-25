# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = MovieItem()
            tops = each_movie.xpath('./span/font/text()').extract()
            if len(tops) > 0:
                item['top'] = tops[0]
            else:
                item['top'] = each_movie.xpath('./span[@class="state1 new100state1"]/text()').extract()[0]
            item['style'] = each_movie.xpath('./span[@class="mjjq"]/text()').extract()[0]
            item['tv'] = each_movie.xpath('./span[@class="mjtv"]/text()').extract()[0]
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item