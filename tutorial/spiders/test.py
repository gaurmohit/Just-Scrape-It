import scrapy

class first_spider(scrapy.Spider):
  name= 'test'

  def start_requests(self):
      urls='https://nces.ed.gov/ccd/schoolsearch/school_detail.asp?Search=1&DistrictID=0100360&ID=010036000092'
      yield scrapy.Request(url=urls,callback=self.parse)

  def parse(self,response):
      result1=response.xpath("//strong/text()").extract()
      result2=response.xpath("//font/text()").extract()
      print(result1+result2)
      print(len(result1+result2))
      yield result1+result2

