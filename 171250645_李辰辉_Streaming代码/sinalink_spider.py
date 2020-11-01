import scrapy

#edu: http://edu.sina.com.cn/
#gov: http://gov.sina.com.cn/
#milite: https://mil.news.sina.com.cn/
#world: https://news.sina.com.cn/world/
#sports: http://sports.sina.com.cn/
#finance: http://finance.sina.com.cn/topnews/
#ent: https://ent.sina.com.cn/hotnews/ent/Daily/
#tech: https://tech.sina.com.cn/

class SlinkSpider(scrapy.Spider):
    name = "slink"
    start_urls = ["https://tech.sina.com.cn/"]

    #used for entertainment
    # def parse(self, response):
    #     news_link_list = response.css("div#Con11 td.ConsTi")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "ent",
    #             "url": link_url
    #         }

    #used for finance
    # def parse(self, response):
    #     news_link_list = response.css("div#page div.loopblk")[1].css("td.ConsTi")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "finance",
    #             "url": link_url
    #         }

    # used for technology
    def parse(self, response):
        news_link_list = response.css("ul#rcon1 li")
        for news_item in news_link_list:
            link_url = news_item.css("a::attr(href)").get()
            if link_url is None:
                continue
            yield {
                "type": "tech",
                "url": link_url
            }

    ##used for world
    # def parse(self, response):
    #     news_link_list = response.css("ol#subShowRank1_c1 li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "world",
    #             "url": link_url
    #         }

    #used for military
    # def parse(self, response):
    #     news_link_list = response.css("div.zgjq div.middle li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "milite",
    #             "url": link_url
    #         }

    #used for sports
    # def parse(self, response):
    #     news_link_list = response.css("div#ty-top-ent0 a")
    #     for news_item in news_link_list:
    #         link_url = news_item.root.attrib['href']
    #         if link_url is None:
    #             continue
    #         link_url = "https:" + link_url
    #         yield {
    #             "type": "sports",
    #             "url": link_url
    #         }

    # ##used for gov
    # def parse(self, response):
    #     news_link_list = response.css("div.china li.today dt")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "gov",
    #             "url": link_url
    #         }

    # #used for edu
    # def parse(self, response):
    #     news_link_list = response.css("div.rank_wrap div.rank_list_wrap div.rank_news ul li")
    #     for news_item in news_link_list:
    #         link_url = news_item.css("a::attr(href)").get()
    #         if link_url is None:
    #             continue
    #         yield {
    #             "type": "edu",
    #             "url": link_url
    #         }