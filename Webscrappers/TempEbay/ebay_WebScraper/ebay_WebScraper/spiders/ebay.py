import scrapy
import scraper_api

client = scraper_api.ScraperAPIClient('69ec9c37d459d0fd1cee61beaa6ee1ea')


class EbaySpider(scrapy.Spider):
    name = "ebay"
    #allowed_domains = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/sch/i.html?_from=R40&_nkw=rolex&_sacat=0&rt=nc&Year%2520Manufactured=2020%252DNow&_dcat=31387&_ipg=240"]

    def parse(self, response):
        LinkToProducts = response.xpath('//a[@class="s-item__link"]/@href').getall()
        if LinkToProducts:
            for url in LinkToProducts: 
                yield scrapy.Request(client.scrapyGet(url), callback = self.parse_page)
            #yield from response.follow_all(LinkToProducts,callback=self.parse_page)
        NextPageButton = response.xpath('//a[@aria-label="Go to next search page"]/@href').get()
        if NextPageButton:
            yield scrapy.Request(client.scrapyGet(NextPageButton), callback = self.parse)
            #yield response.follow(NextPageButton, callback=self.parse)
        
        
    def parse_page(self, response):
        Product_Title = ''.join(response.xpath('//h1[@class="x-item-title__mainTitle"]/span/text()').getall())
        Product_Price = ''.join(response.xpath('//div[@class="x-price-primary"]/span/text()').getall())
        Item_Specs =  response.xpath('//div[@class="ux-layout-section-evo ux-layout-section--features"]//div[@class="ux-labels-values__labels"]')
        all_spec = []
        for container in Item_Specs: 
            label = ''.join(container.xpath('.//text()').getall())
            value_ = ''.join(container.xpath('./following-sibling::div[1][@class="ux-labels-values__values"]//text()').getall())
            all_spec.append(label + ' : ' + value_)
        all_spec = ' --- ' .join(all_spec)
        
        yield{'Product_Title': Product_Title, 
              'Product_Price': Product_Price, 
              'Item_Specs': Item_Specs, 
              'all_spec': all_spec}