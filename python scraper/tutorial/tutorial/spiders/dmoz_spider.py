import scrapy

from tutorial.items import rcmItem

class rcmSpider(scrapy.Spider):
    name = "rcm"
    allowed_domains = ["rcm.corp.emc.com"]
    start_urls = [
        "http://rcm.corp.emc.com/Systems/RCM_Schedule/",
    ]

    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
