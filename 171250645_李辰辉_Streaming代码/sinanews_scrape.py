import scrapy

type_url = [
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezuev1797157.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/china/2019-10-13/doc-iicezuev1588598.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1841487.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1841490.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1841506.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/chanjing/cyxw/2019-10-13/doc-ihytcerm8843159.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/chanjing/cyxw/2019-10-13/doc-iicezzrr1836852.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/china/2019-10-13/doc-iicezzrr1835882.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1841499.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/china/2019-10-13/doc-iicezzrr1845433.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezuev1797167.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/chanjing/cyxw/2019-10-13/doc-iicezuev1786796.shtml"},
{"type": "finance", "url": "http://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1828596.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/china/2019-10-13/doc-iicezuev1809974.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezuev1797160.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezuev1797159.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/china/2019-10-13/doc-iicezuev1813019.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1841486.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezuev1797148.shtml"},
{"type": "finance", "url": "https://finance.sina.com.cn/roll/2019-10-13/doc-iicezzrr1841496.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-13/doc-iicezuev1814201.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-13/doc-iicezuev1813011.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-13/doc-iicezuev1812072.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-13/doc-iicezuev1811586.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezzrr1808013.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezzrr1691698.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezzrr1653548.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezzrr1646623.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezuev1598737.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezuev1596639.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezzrr1640604.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-12/doc-iicezuev1595561.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-11/doc-iicezuev1539035.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-11/doc-iicezuev1453610.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-11/doc-iicezzrr1496401.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/2019-10-11/doc-iicezzrr1490277.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-11/doc-iicezuev1396698.shtml"},
{"type": "milite", "url": "https://mil.news.sina.com.cn/jssd/2019-10-11/doc-iicezuev1389967.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/zt_d/159/"},
{"type": "sports", "url": "https://sports.sina.com.cn/tennis/atp/2019-10-12/doc-iicezzrr1776973.shtml"},
{"type": "sports", "url": "https://slide.sports.sina.com.cn/t/slide_2_794_230798.html"},
{"type": "sports", "url": "https://sports.sina.com.cn/run/2019-10-12/doc-iicezuev1711270.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/run/2019-10-12/doc-iicezuev1722079.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/run/2019-10-12/doc-iicezuev1735350.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/run/2019-10-12/doc-iicezzrr1761641.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/run/2019-10-12/doc-iicezzrr1796198.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/run/2019-10-12/doc-iicezzrr1797221.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/others/pingpang/2019-10-12/doc-iicezuev1753147.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/others/pingpang/2019-10-12/doc-iicezuev1756502.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezzrr1845903.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezzrr1846975.shtml"},
{"type": "sports", "url": "https://slide.sports.sina.com.cn/k/slide_2_786_230744.html#p=1"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezuev1802281.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezuev1801793.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezzrr1848485.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezzrr1847976.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezuev1805187.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/basketball/nba/2019-10-13/doc-iicezuev1804322.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/national/2019-10-12/doc-iicezzrr1754078.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/national/2019-10-12/doc-iicezuev1672907.shtml"},
{"type": "sports", "url": "https://slide.sports.sina.com.cn/n/slide_2_789_230800.html"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/national/2019-10-12/doc-iicezzrr1755132.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/national/2019-10-12/doc-iicezzrr1722576.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/j/2019-10-12/doc-iicezzrr1763183.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/j/2019-10-12/doc-iicezzrr1733807.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/j/2019-10-12/doc-iicezzrr1711771.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/china/j/2019-10-12/doc-iicezzrr1781350.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/zt_d/euro2020/"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/laliga/2019-10-13/doc-iicezzrr1842324.shtml"},
{"type": "sports", "url": "https://slide.sports.sina.com.cn/g_laliga/slide_2_730_230905.html"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/laliga/2019-10-13/doc-iicezuev1801795.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/laliga/2019-10-13/doc-iicezuev1802071.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/laliga/2019-10-12/doc-iicezuev1684213.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/laliga/2019-10-12/doc-iicezuev1679650.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/pl/2019-10-12/doc-iicezzrr1726750.shtml"},
{"type": "sports", "url": "https://sports.sina.com.cn/g/pl/2019-10-12/doc-iicezuev1686396.shtml"},
{"type": "sports", "url": "https://slide.sports.sina.com.cn/o/slide_2_730_230430.html"},
{"type": "sports", "url": "https://sports.sina.com.cn/zl/"},
{"type": "sports", "url": "https://sports.sina.com.cn/zl/football/2019-10-08/zldoc-iicezzrr0724262.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-13/doc-iicezzrr1774651.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezuev1734839.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezzrr1781599.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezuev1716536.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/c/2019-10-12/doc-iicezzrr1750696.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezuev1759163.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezzrr1789426.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezuev1741677.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-13/doc-iicezzrr1839945.shtml"},
{"type": "world", "url": "https://news.sina.com.cn/w/2019-10-12/doc-iicezzrr1692871.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/i/2019-10-12/doc-iicezzrr1673635.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/i/2019-10-12/doc-iicezzrr1689314.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/d/s/2019-10-12/doc-iicezzrr1662412.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/t/2019-10-12/doc-iicezzrr1702421.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/i/2019-10-12/doc-iicezuev1699755.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/d/i/2019-10-12/doc-iicezuev1618567.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/d/f/2019-10-12/doc-iicezzrr1662899.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/t/2019-10-12/doc-iicezuev1694354.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/t/2019-10-12/doc-iicezzrr1659983.shtml"},
{"type": "tech", "url": "https://tech.sina.com.cn/d/c/2019-10-12/doc-iicezzrr1688477.shtml"}
]
index = 0
current_type = "finance"
news_num = len(type_url)

class NewsSpider(scrapy.Spider):

    name = "snews"
    start_urls = ["https://finance.sina.com.cn/roll/2019-10-13/doc-iicezuev1797157.shtml"]

    def parse(self, response):
        global type_url
        global index
        global current_type
        global news_num
        try:
            if "slide" in response.url:
                div_body = response.css("div.part-a")
                imgnum = div_body.css("span.num::text").get()\
                    .replace(" ","").replace("/","")
                textlen = len(div_body.css("div.swp-tit h2::text").get())
                cmt_blk = response.css("div#bottom_sina_comment span em")
                cmtnum = cmt_blk[0].css("a::text").get().replace(",","")
                patnum = cmt_blk[1].css("a::text").get().replace(",","")

                yield {
                    "media": "sina",
                    "type": current_type,
                    "time": "2019-10-10",
                    "cmtnum": int(cmtnum),
                    "patnum": int(patnum),
                    "textlen": textlen,
                    "imgnum": int(imgnum)
                }
            else:
            # if "/photoview/" not in response.url:
                cmt_div = response.css("div.sina-comment-form.sina-comment-top")
                em_div = cmt_div.css("span.count em")
                cmtnum = em_div[0].css("a::text").get()
                patnum = em_div[1].css("a::text").get()
                article_div = response.css("div#artibody")
                if len(article_div) == 0:
                    article_div = response.css("div#article")
                ps = article_div.css("p")
                imgs = article_div.css("img")
                imgnum = len(imgs)
                textlen = 0
                for p in ps:
                    text = p.root.text
                    if text is None:
                        continue
                    textlen += len(text)
                cmtnum = cmtnum.replace(",", "")
                patnum = patnum.replace(",","")
                yield{
                    "media": "sina",
                    "type": current_type,
                    "time": "2019-10-09",
                    "cmtnum": int(cmtnum),
                    "patnum": int(patnum),
                    "textlen": textlen,
                    "imgnum": imgnum
                }
        except Exception as e:
            print("Fail to scrape" + response.url)
            fail_url = response.url
            f = open("fail_url.json", "a")
            fail_type = current_type
            fail_line = "{\"type\": \"" + fail_type + "\", \"url\": \"" + fail_url + "\"},\n"
            f.writelines(fail_line)
            f.close()
        index = index + 1
        if index < news_num:
            current_type = type_url[index].get("type")
            next_url = type_url[index].get("url")
            yield scrapy.Request(url=next_url, callback=self.parse)