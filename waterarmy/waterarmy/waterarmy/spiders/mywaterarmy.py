import scrapy
import requests
from scrapy.spider import BaseSpider
# from  NewsTitleFind.items import  MyItem
from scrapy.selector import HtmlXPathSelector
from waterarmy.items import WaterarmyItem
class QuotesSpider(scrapy.Spider):
    name = "test"

    # scrapy.Request(url=start_urls[0], callback=parse)
    choose = ""


    def start_requests(self):
        urls =[]


        rs = requests.get("https://www.yelp.com/search?find_loc=San+Francisco%2C+CA")
        print rs.text;

        # for i in range(start, end, 1):
        #     thisurl = "http://www.yiren10.com/se/"+self.choose+"/index_" + str(i)+".html";
        #     urls.append(thisurl)


        for url in urls:

            yield scrapy.Request(url,  callback=self.parse)

    def parse(self, response):
        # thisItem =MyItem();
        # page = HtmlXPathSelector(response)
        # title = page.select('//li/a/@title').extract()
        #
        # sites = page.select('//li/a[@target="_blank"]/@href').extract()
         x= 0
        # for i in title:
        #     # print i
        #     url="http://www.yiren10.com"+sites[x];
        #     # print url
        #     x+=1
        #     # print title[x];
        #     yield  scrapy.Request(url,  callback=self.parseson)

    # def parseson(self,response):
    #     Item = WaterarmyItem();
    #     # page = HtmlXPathSelector(response)
    #     #
    #     # imglink = page.select('//img/@src').extract()
    #     # title = page.select('//title/text()').extract()
    #     print title[0]
    #     Item["name"]=""
    #     Item['content'] =""
    #     # Item['url'] = imglink;
    #     yield Item
        # sites = page.select('//li/a[@target="_blank"]/@href').extract()
        # x = 0
        # for i in imglink:
        #     print i
            # url = "http://www.yiren10.com" + sites[x];
            # print url
            # x += 1
            # print title[x];


        # print len(sites);
        # for i in range(2,len(sites),1):
            # thisItem = MyItem();
            # namestr = '//table[@align="left"]/tr['+str(i)+']'+"/td[1]/text()"
            # thisItem['name'] = page.select(namestr).extract()[0]
            #
            # huigetinstr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[2]/text()"
            # thisItem['huigetin'] = page.select(huigetinstr).extract()[0];
            # chaogetinstr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[3]/text()"
            # thisItem['chaogetin'] = page.select(chaogetinstr).extract()[0];
            # huigetoutstr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[4]/text()"
            # thisItem['huigetout'] = page.select(huigetoutstr).extract()[0];
            # chaogetoutstr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[5]/text()"
            # thisItem['chaogetout'] = page.select(chaogetoutstr).extract()[0];
            # zhesuanstr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[7]/text()"
            # thisItem['zhesuan'] = page.select(zhesuanstr).extract()[0];
            # PDatastr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[6]/text()"
            # thisItem['Waiguanju'] = page.select(PDatastr).extract()[0];
            # PTimestr = '//table[@align="left"]/tr[' + str(i) + ']' + "/td[8]/text()"
            # thisItem['PTime'] = page.select(PTimestr).extract()[0];

            # print thisItem
            # yield thisItem

# huigetin = Field()
# chaogentin = Field()
# huigetout = Field()
# chaogetout = Field()
# zhesuan = Field()
# PData = Field()
# PTime = Field()