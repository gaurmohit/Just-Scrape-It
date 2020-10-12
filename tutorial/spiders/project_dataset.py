import scrapy
from scrapy import Selector

class Table(scrapy.Item):
    player = scrapy.Field()
    matches= scrapy.Field()
    inn= scrapy.Field()
    overs = scrapy.Field()
    mad= scrapy.Field()
    wick= scrapy.Field()
    avg = scrapy.Field()
    eco = scrapy.Field()
    b_strick = scrapy.Field()
    ct= scrapy.Field()
    st = scrapy.Field()

class ESPN_dataset(scrapy.Spider):
    name="project_dataset"

    def start_requests(self):
        allowed_domains= "http://www.espncricinfo.com/"
        url="http://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?class=3;id=6;type=team"
        yield scrapy.Request(url=url,callback=self.parse)


    def parse(self,response):
        lst=[]
        sel = response.xpath("//table[@class='engineTable']/tbody/tr/td//text()").extract()
        i=j=0
        table_row = Table()
        while i<len(sel)+1:
            if i%16 == 0 and j==1:
                table_row['player'] = lst[0]
                table_row['matches'] = lst[1]
                table_row['inn'] = lst[2]
                table_row['overs'] = lst[3]
                table_row['mad'] = lst[4]
                table_row['wick'] = lst[5]
                table_row['avg'] = lst[6]
                table_row['eco'] = lst[7]
                table_row['b_strick'] = lst[8]
                table_row['ct'] = lst[9]
                table_row['st'] = lst[10]
                lst[:] = []
                j=0

                yield table_row
                print(table_row)
                print("-------------------"+str(i))

            if i==len(sel):
                i+=1
                continue
            else:
                lst.append(sel[i])
            i+=1
            j=1

# 
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from datetime import datetime
#
# if _name_ == "__main__":
#         process = CrawlerProcess(get_project_settings())
#         try:
#
#                 arguments={'a1':a1,'a2':a2}
#                 process.crawl(scraper_name,**arguments)
#             process.start()
#
# class AmazonSpider(scrapy.Spider):
#
#     name = "amazon"
#     allowed_domains = ['amazon.co.uk']
#     start_urls = ['http://www.amazon.co.uk/product-reviews/B0042EU3A2/' ]
#
#     def parse(self, response):
#
#         for sel in response.xpath('//table[@id="productReviews"]//tr/td/div'):
#
#             item = AmazonItem()
#             item['rating'] = sel.xpath('./div/span/span/span/text()').extract()
#             item['date'] = sel.xpath('./div/span/nobr/text()').extract()
#             item['review'] = sel.xpath('./div[@class="reviewText"]/text()').extract()
#             item['link'] = sel.xpath('.//a[contains(.,"Permalink")]/@href').extract()
#             yield item
#
#         xpath_Next_Page = './/table[@id="productReviews"]/following::*//span[@class="paging"]/a[contains(.,"Next")]/@href'
#         if response.xpath(xpath_Next_Page):
#             url_Next_Page = response.xpath(xpath_Next_Page).extract()[0]
#             request = scrapy.Request(url_Next_Page, callback=self.parse)
#             yield request
