import scrapy
import time

type_url = [
    {"type": "finance", "url": "https://money.163.com/19/1011/15/ER7GNMH7002580S6.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/07/ER96JJ6J00258105.html"},
    {"type": "finance", "url": "http://money.163.com/19/1010/10/ER4C1L6O002580S6.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/17/ERA81R0400258J1R.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/15/ERA2A1DG002580S6.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/07/ER96FQNC00259DLP.html"},
    {"type": "finance", "url": "https://money.163.com/19/1011/18/ER7P09HH002580S6.html"},
    {"type": "finance", "url": "https://money.163.com/19/1013/07/ERBQ9F9300258105.html"},
    {"type": "finance", "url": "http://money.163.com/19/1011/17/ER7OFOQV00258105.html"},
    {"type": "finance", "url": "http://money.163.com/19/1012/12/ER9MOV9600259DLP.html"},
    {"type": "finance", "url": "https://money.163.com/19/1011/12/ER74IVS800258105.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/16/ERA76H6Q00259DLP.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/17/ERA7T4TO00259DLP.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/14/ER9V9FUM00259DLP.html"},
    {"type": "finance", "url": "https://money.163.com/19/1011/08/ER6MH86U00258105.html"},
    {"type": "finance", "url": "https://money.163.com/19/1011/11/ER73AJUT00258152.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/07/ER9720NP00258105.html"},
    {"type": "finance", "url": "https://money.163.com/19/1012/17/ERA9G1MK002580S6.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/10/ER9G6JHN0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/10/ER9G7M2M0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/10/ER9HRP6S0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4TQLB00237VT3.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/11/ER9JHU1L0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/10/ER9I0KAA0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4JSLL00237VT3.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4IUHK00237VT3.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4H98R00237VT3.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/11/ER9JDSHM0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/10/ER9HVANE0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4BES700237VT9.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4PA3H00237VT9.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/16/ERA4EECO00237VT9.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1008/10/EQV7JSHU0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1006/10/EQQ3CHSM0023995U.html"},
    {"type": "gov", "url": "https://gov.163.com/19/0808/15/EM2N0DCV00237VT3.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/09/ER9E30QS002399RB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1011/11/ER70SLMU002399RB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1010/09/ER498FEU002399RB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1008/16/EQVRD1E1002399RB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1008/12/EQVDN0QG002399RB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1006/17/EQQRAIMA002399RB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/17/ERAAB52400237VTB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/17/ERAA9Q5G00237VTB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/17/ERAASJ7U00237VTB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/17/ERAA8NL600237VTB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/17/ERAAR16100237VTB.html"},
    {"type": "gov", "url": "https://gov.163.com/19/1012/17/ERAA5TQP00237VTB.html"},
    # {"type": "milite", "url": "http://war.163.com/photoview/4T8E0001/2304601.html"},
    {"type": "milite", "url": "http://war.163.com/photoview/4T8E0001/2304605.html"},
    {"type": "milite", "url": "http://war.163.com/photoview/4T8E0001/2304604.html"},
    {"type": "milite", "url": "http://war.163.com/photoview/4T8E0001/2304603.html"},
    {"type": "milite", "url": "http://war.163.com/photoview/4T8E0001/2304602.html"},
    {"type": "milite", "url": "https://news.163.com/air/19/1013/10/ERC288LI000181O6.html"},
    {"type": "milite", "url": "https://war.163.com/19/1013/09/ERC0TGSO000181KT.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1012/16/ERA50HQR00058782.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/08/ERBT8G6A00058782.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1012/22/ERAQA98L00058782.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/06/ERBNAVE700058782.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1012/23/ERATUGFP00058782.html"},
    {"type": "sports", "url": "http://sports.163.com/special/2019sh_masters/"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBNSVS800058781.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBO3MSO00058781.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/10/ERC1VQAV00058781.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/08/ERBSGR2S00058781.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBPKVEH00058781.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBO5LFM00058781.html"},
    {"type": "sports", "url": "http://sports.163.com/cba/"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/08/ERBTNETT0005877V.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/08/ERBSN41B0005877V.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBNJ1FC0005877V.html"},
    {"type": "sports", "url": "https://sports.163.com/nba/"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/10/ERC2674L0005877U.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/09/ERC0VFGS0005877U.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1012/10/ER9FHNCR0005877U.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1012/12/ER9MENUB0005877U.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/08/ERBSCLH400058780.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBQSVQ700058780.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1013/07/ERBPF8EE00058780.html"},
    {"type": "sports", "url": "https://sports.163.com/19/1012/23/ERAS601B00058780.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/09/ERC0KL63000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/09/ERBVSQ1M00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/09/ERBVGJ8B000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/09/ERBV529R000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/09/ERBV2M0T000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/08/ERBUC5NB00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/08/ERBU3PI1000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/08/ERBR59KT00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1013/08/ERBR599V00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/14/ER9V08KT00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/14/ER9UIMNG00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/14/ER9U2JCR00097U7S.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/12/ER9OSCCL00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/12/ER9NKBUN00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/11/ER9M24SD00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/11/ER9LIAO600097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/11/ER9K9HRN00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/11/ER9J7DPH000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/10/ER9HHD9T00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/10/ER9FSDP3000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/09/ER9EDVP200097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/08/ER9A9QO1000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/07/ER98JS83000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/07/ER98AJEO000998GP.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/07/ER97UKUD000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/07/ER97MVKB00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1012/07/ER963BIS000998GP.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/17/ER0114CM00097U81.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/16/EQVTO3HG00098IEO.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/16/EQVTDIJ0000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/16/EQVTBH0C000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/16/EQVSROE1000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/16/EQVSHVM5000999LD.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/15/EQVNCEK900097U7S.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/14/EQVL7QJA00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/14/EQVL1A0L00097U7S.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/13/EQVJ8MO900097U80.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/13/EQVIMUPI00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/13/EQVHB12400097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/12/EQVG4M6F00097U7R.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/12/EQVG3IOK00097U7T.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/12/EQVD3RQO00098IEO.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/11/EQVAKCQL00098IEO.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/11/EQVA44N600097U7H.html"},
    {"type": "tech", "url": "https://tech.163.com/19/1008/11/EQV9R88700098IEO.html"},
    {"type": "world", "url": "https://news.163.com/19/1012/01/ER8JLKMT0001899N.html"},
    {"type": "world", "url": "https://news.163.com/19/1011/23/ER8CNO2O0001899N.html"},
    {"type": "world", "url": "https://news.163.com/19/1012/12/ER9PMIUA0001899N.html"},
    {"type": "world", "url": "https://news.163.com/19/1012/00/ER8E5T2R0001899O.html"},
    {"type": "world", "url": "https://news.163.com/19/1012/03/ER8NNI8T0001875N.html"},
    {"type": "world", "url": "https://news.163.com/19/1012/03/ER8OHH7K0001899N.html"},
    {"type": "world", "url": "https://news.163.com/19/1012/07/ER97NC1U0001899O.html"},
]
index = 0
current_type = "finance"
news_num = len(type_url)

class NewsSpider(scrapy.Spider):

    name = "news"
    start_urls = ["https://money.163.com/19/1011/15/ER7GNMH7002580S6.html"]

    def parse(self, response):
        global type_url
        global index
        global current_type
        global news_num

        try:
            if "/photoview/" not in response.url:
                cmtnum = response.css("a.js-tiecount::text").get()
                patnum = response.css("a.js-tiejoincount::text").get()
                ps = response.css("div.post_text p")
                imgs = response.css("div.post_text img")
                imgnum = len(imgs)
                textlen = 0
                for p in ps:
                    text = p.root.text
                    if text is None:
                        continue
                    textlen += len(text)

                try:
                    pse = response.css("div#endText p")

                    for p in pse:
                        text = p.root.text
                        if text is None:
                            continue
                        textlen += len(text)

                    explicitImgNum = int(response.css("div.nph_cnt span")[0].root.text.replace("/",""))
                    imgnum += explicitImgNum
                except Exception as ie:
                    print(ie)
                # wline = '{"media": "netease", "type": "' + current_type +'", "time": "2019-10-09", "cmtnum": '\
                #         + cmtnum + ', "patnum": ' + patnum + ', "textlen": ' + str(textlen) + ', "imgnum": ' \
                #         + str(imgnum) + '}\n'
                # f.write(wline)

                yield{
                    "media": "netease",
                    "type": current_type,
                    "time": "2019-10-11",
                    "cmtnum": int(cmtnum),
                    "patnum": int(patnum),
                    "textlen": textlen,
                    "imgnum": imgnum
                }
            else:
                cmt_div = response.css("a.tie-actCount")
                cmtnum = cmt_div[0].root.text
                patnum = cmt_div[1].root.text
                imgnav = response.css("div.thumb.cf ul li")
                imgnum = imgnav[-1].css("span::text").get()
                textlen = response.css("div.headline h1::text").get()

                # wline = '{"media": "netease", "type": "' + current_type + '", "time": "2019-10-09", "cmtnum": ' \
                #         + cmtnum + ', "patnum": ' + patnum + ', "textlen": ' + str(textlen) + ', "imgnum": ' \
                #         + str(imgnum) + '}\n'
                # f.write(wline)

                yield {
                    "media": "netease",
                    "type": current_type,
                    "time": "2019-10-11",
                    "cmtnum": int(cmtnum),
                    "patnum": int(patnum),
                    "textlen": len(textlen),
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

            print(e)

        print("=======================================================================================================")

        index = index + 1
        if index < news_num:
            current_type = type_url[index].get("type")
            next_url = type_url[index].get("url")
            yield scrapy.Request(url=next_url, callback=self.parse)
