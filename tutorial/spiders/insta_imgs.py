import scrapy
import time

class spidy(scrapy.Spider):
    name="insta_imgs"

    def start_requests(self):
        url="https://www.instagram.com/ranveersingh/?hl=en"
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        images=response.xpath("//div[@class='_4rbun']/img/@src").extract()
        for img in images:
            yield scrapy.Request(url=img,callback=self.save_img)

    def save_img(self,img):
        print(img)
        print("-------------------")
        print(type(img))
        with open('/home/mohit/Pictures/imags/'+str(time.time())+'.JPEG','wb+') as ob:
            ob.write(img.body)
