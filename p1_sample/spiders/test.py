
from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from p1_sample.items import P1SampleItem 

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.shell import inspect_response

import codecs
import re






class MySpider(CrawlSpider):
    name = "p1"

    #allowed_domains = ["inmondadori.it"]
    allowed_domains = ["mondadoristore.it"]

#http://www.mondadoristore.it/libri/italiani/Guide-turistiche-e-Viaggi/genG00D/

    #start_urls = ["http://www.inmondadori.it/libri/italiani/Guide-turistiche-e-Viaggi/genG00D/"]
    start_urls = ["http://www.mondadoristore.it/libri/italiani/Guide-turistiche-e-Viaggi/genG00D/"]
   
    rules =    (

    
     Rule(SgmlLinkExtractor(allow='libri/italiani/Guide-turistiche-e-Viaggi/genG00D'),callback='parse_item',follow=True),
     
     Rule(SgmlLinkExtractor(allow='libri/italiani/Guide-turistiche-e-Viaggi/genG00D/\d{1,1}'),callback='parse_item',follow=True),

    )

#d{1,3}

    def parse_item(self, response,):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//div[contains(@class,'single-box')]")
        items = []
        for titles in titles:
            item = P1SampleItem()
            item ["title_url_name"] = titles.select(".//h3").extract()
            item ["author"] = titles.select(".//a[contains(@class,'link nti-author')]/text()").extract()
            item ["price"]  = titles.select(".//span[contains(@class,'new-price')]/text()").extract()
            items.append(item)
        return items
        spider = MySpider()
