# -*- coding: utf-8 -*-
import scrapy
import json
import re
from scrapy_splash import SplashRequest
import datetime
from Icbc.items import IcbcItem
class IcbcSpider(scrapy.Spider):
    name = 'icbc'
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    allowed_domains = ['tmsf.com']
    start_urls=["http://www.tmsf.com/index.jsp"]
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,callback=self.parse,args={'wait':5})
    def areah(self,cc):
        if cc=='主城区':
            return '1'
        elif cc=='萧山区':
            return '2'
        elif cc=='余杭区':
            return '3'
        elif cc=='富阳区':
            return '4'
        elif cc=='大江东':
            return '5'
        elif cc=='市区总计':
            return '6'
        elif cc=='四县市':
            return '7'
        else:
            return '0'

    def parse(self, response):
        node_list=response.xpath("//dd[@id='myCont4']/div[1]/div[2]/table[1]/tbody[1]/tr")
        for node in node_list:
            item = IcbcItem()
            harea=node.xpath("./td[1]/text()").extract()[0].encode("utf-8")
            hareasign=self.areah(harea)
            hsign=node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            hreserve=node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            hsurplus=node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item['harea'] = harea
            item['hareasign'] = hareasign
            item['hsign'] = hsign
            item['hreserve'] = hreserve
            item['hsurplus'] = hsurplus
            item['htime']=self.nowtime
            yield item










