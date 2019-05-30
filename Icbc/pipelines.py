# -*- coding: utf-8 -*-
import pymysql,sys
if sys.getdefaultencoding() != 'gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')
from scrapy.pipelines.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
def dbHandle():
    conn = pymysql.connect(host = "192.168.100.56",user = "root",port = 22767,passwd = "1a2s3d$f",charset = "utf8",use_unicode=False)
    return conn
class IcbcPipeline(object):
    def process_item(self, item, spider):
        def save_mysql(item):
            try:
                dbObject = dbHandle()
                cursor = dbObject.cursor()
                cursor.execute("USE test")
                sql = "INSERT INTO house_date(harea,hareasign,hsign,hreserve,hsurplus,htime) VALUES(%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(item["harea"],item["hareasign"], item["hsign"],item["hreserve"],item["hsurplus"],item["htime"]
                                ))
                cursor.connection.commit()
            except BaseException as e:
                print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
                dbObject.rollback()


        save_mysql(item)
        return item
    def item_completed(self, results, item, info):

        return item