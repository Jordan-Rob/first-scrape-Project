import scrapy

class GoodReadsSpider(scrapy.Spider):
    #identity
    name = 'jum'
    #requests
    def start_requests(self):
        url = 'https://www.jumia.ug/laptops?page=1'
       
        yield scrapy.Request(url=url, callback=self.parse)

    #response
    def parse(self, response):
        for product in response.selector.xpath("//a[@class='link']"):
            price = product.xpath(".//span[@dir='ltr']/@data-price").extract_first()
            new_price = int(price)

            if (new_price < 1200000 ):
                yield {
                    'name':product.xpath(".//span[@class='name']/text()").extract_first(),
                    'price':product.xpath(".//span[@dir='ltr']/@data-price").extract_first()
                }

                
            

        next_page = response.selector.xpath("//a[@title='Next']/@href").extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        