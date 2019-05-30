from scrapy import cmdline
import sys
reload(sys)
sys.setdefaultencoding('gb2312')
# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
cmdline.execute("scrapy crawl icbc".split())