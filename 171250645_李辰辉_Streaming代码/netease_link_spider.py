import scrapy

#ent: http://news.163.com/special/0001386F/rank_ent.html
#finance: http://money.163.com/special/002526BH/rank.html
#tech: https://tech.163.com/
#world: https://news.163.com/world/
#milite: https://war.163.com/
#sports: https://sports.163.com/
#gov: https://gov.163.com/
#edu: https://edu.163.com/

class LinkSpider(scrapy.Spider):
    name = "link"
    start_urls = ["https://tech.163.com/"]

    #used for finance and entertainment
    # def parse(self, response):
    #     news_link_list = response.css("div.left div.tabBox div.tabContents")[1].css("td")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "finance",
    #             "url": link_url
    #         }

    #used for technology
    def parse(self, response):
        news_link_list = response.css("div.newest-lists ul li.list_item")
        for news_item in news_link_list:
            link_url = news_item.css("a::attr(href)").get()
            if link_url is None:
                continue
            yield {
                "type": "tech",
                "url": link_url
            }

    ##used for world and military
    # def parse(self, response):
    #     news_link_list = response.css("div.today_news ul li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "world",
    #             "url": link_url
    #         }

    #used for sports
    # def parse(self, response):
    #     news_link_list = response.css("div.topnews li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "sports",
    #             "url": link_url
    #         }

    ##used for gov
    # def parse(self, response):
    #     news_link_list = response.css("div.rsborder li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "gov",
    #             "url": link_url
    #         }

    ##used for edu
    # def parse(self, response):
    #     news_link_list = response.css("div.lf_comment li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a")[0].root.attrib['href']
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "edu",
    #             "url": link_url
    #         }