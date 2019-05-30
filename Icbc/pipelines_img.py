# -*- coding: utf-8 -*-
import os,sys,scrapy,re
from settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
if sys.getdefaultencoding() != 'gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')
from scrapy.pipelines.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class icbcPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img=item["shopimg"]
        yield scrapy.Request(img)
    def item_completed(self, results, item, info):
        image_paths=[x["path"] for ok,x in results if ok]
        tmp=re.split("/",image_paths[0])
        oldpath=IMAGES_STORE+tmp[0]+"\\"+tmp[1]
        newpath=IMAGES_STORE+"img"+"\\"+item["shopcityid"]
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.rename(oldpath,newpath+"\\"+item["shopuuid"]+".jpg")

        return item