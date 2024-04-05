import re

import requests

r = requests.get("https://www.hevttc.edu.cn/info/1019/23511.htm")

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
