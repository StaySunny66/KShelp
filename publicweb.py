import re

import requests


class HevttcPubWeb:
    basicUrl = "https://www.hevttc.edu.cn/"

    def get_news(self):
        r = requests.get(self.basicUrl + "xwgl.htm")
        r.encoding = "Unicode"
        data = re.findall('<a href="(.*?)" class="flex flex-items" title="(.*?)">', r.text.replace(u'\u200b', ''))
        for li in data:
            print(li)
        return {
            "ListData": data
        }

    def get_page_detail(self, url):
        r = requests.get(self.basicUrl + url)
        r.encoding = "Unicode"

        res = r.text.replace(u'\u200b', "").replace("&nbsp;", "")
        tittle = re.findall('<h1 class="news_tit f30">(.*?)</h1>', res)
        # print(tittle)
        date = re.findall('<div class="fl"><span>【发布日期： (.*?)】</span', res)
        # print(date)
        data = re.findall('<span style="font-family: .*?; font-size: .*?;">(.*?)</span></p>', res)

        article = {
            "tittle": tittle[0],
            "date": date[0],
            "content": data
        }
        print(article)
        return article
class HevttcJwcWeb:
    basicUrl = "https://jwc.hevttc.edu.cn/"

    def get_news(self):
        r = requests.get(self.basicUrl + "tzgg.htm")
        r.encoding = "Unicode"
        data = re.findall('<a href="(.*?)" title=".*?">(.*?)</a>', r.text.replace(u'\u200b', ''))
        for li in data:
            print(li)
        return {
            "ListData": data
        }

    def get_page_detail(self, url):
        r = requests.get(self.basicUrl + url)
        r.encoding = "Unicode"

        res = r.text.replace(u'\u200b', "").replace("&nbsp;", "")
        # print(res)
        tittle = re.findall('<h2 class="art q y">(.*?)</h2>', res)
        # print(tittle)
        date = re.findall('<span>发布时间：<b>(.*?)</b></span>', res)
        # print(date)
        data = re.findall('<span style=".??font-family:.??">(.??)</span>', res)

        article = {
            "tittle": tittle[0],
            "date": date[0],
            "content": data
        }
        print(article)
        return article
