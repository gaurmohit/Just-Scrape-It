import scrapy
import time

class second_spider(scrapy.Spider):
    name="pin_img"

    def start_requests(self):
        url="https://in.pinterest.com/javidante/justice-league-of-america/"
        yield scrapy.Request(url=url,callback=self.parse)


    def parse(self,response):
            imgs= response.xpath("//div[@class='GrowthUnauthPinImage']/a/img/@src").extract()
            print ('-------------')
            print (imgs)
            for img in imgs:
                yield scrapy.Request(url=img,callback=self.save_img)


    def save_img(self,img):
            print("----------------")
            print(type(img))
            with open('/home/mohit/Pictures/pinterest/'+str(time.time())+'.JPEG','wb+') as f:
                f.write(img.body)
