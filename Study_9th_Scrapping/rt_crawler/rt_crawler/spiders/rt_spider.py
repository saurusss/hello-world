import scrapy

from rt_crawler.items import TRItem

class RTSpider(scrapy.Spider):
    name = "RottenTomatoes"
    allowed_domain = ["rottemtomatoes.com"]
    start_urls = [
        "https://www.rottentomatoes.com/top/bestofrt/?year=2018"
    ]
    
    def parse(self, response):
        for tr in response.xpath('//*[@id="top_movies_main"]/div/table/tr'):
            href = tr.xpath('./td[3]/a/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)
            
    def parse_page_contents(self, response):
        item = RTItem()
        item["title"] = response.xpath('//*[@id="movie-title"]/text()')[0].extract().strip()
        item["score"] = response.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()').extract()
        yield item
        
        
            