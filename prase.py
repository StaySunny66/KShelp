import re
from urllib import parse
import json
import requests


# 开始登录 操作
def get_login_view_state(ASP_NET_SessionId):
    headers = {
        "Host": "121.22.25.47",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://121.22.25.47",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://121.22.25.47/default2.aspx",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "ASP.NET_SessionId=" + ASP_NET_SessionId
    }
    response = requests.get('http://121.22.25.47/DEFAULT2.ASPX', headers=headers)
    response.encoding = "gbk"
    view = re.findall('name="__VIEWSTATE" value="(.*?)"', response.text, 0)
    if len(view) == 1:
        print('获取到登陆界面__VIEW_STATE', parse.quote(view[0]))
        return parse.quote(view[0])
    else:
        print("view获取失败 下面是响应数据==============================================================")
        print(response.text)
        print("view获取失败 上面是响应数据==============================================================")


def login(ASP_NET_SessionId, yz_code, user, password):
    headers = {
        "Host": "121.22.25.47",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://121.22.25.47",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://121.22.25.47/default2.aspx",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "ASP.NET_SessionId=" + ASP_NET_SessionId
    }
    view_state = get_login_view_state(ASP_NET_SessionId)

    data = "__VIEWSTATE=" + view_state + "&txtUserName=" + user + "&TextBox2" \
                                                                  "=" + password + "&txtSecretCode=" + yz_code + "&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage=&hidPdrs=&hidsc= "
    response = requests.post('http://121.22.25.47/DEFAULT2.ASPX', headers=headers, data=data)
    response.encoding = "gbk"
    result = login_chick(user, ASP_NET_SessionId)
    if result == 'error':
        print("登录校验失败，获取失败")
        return "error"
    else:

        return {
            "name": result,
            "cookie": ASP_NET_SessionId
        }


# 检查是否登录成功
def login_chick(user, ASP_NET_SessionId):
    url = 'http://121.22.25.47/xs_main.aspx?xh=' + user
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Cookie": "ASP.NET_SessionId=" + ASP_NET_SessionId,
        "Host": "121.22.25.47",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://121.22.25.47/default2.aspx",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47 "
    }

    r = requests.get(url, headers=headers)
    name = re.findall("<span id=\"xhxm\">(.*?)同学</span>", r.text, 0)
    if len(name) == 1:
        print("登录成功 获得姓名:", name[0]);
        return name[0]
    else:
        print("登录失败！")
        return "error"


# http://121.22.25.47/xs_main.aspx?xh=0914200104
def get_user_message(ASP_NET_SessionId, user):
    url = 'http://121.22.25.47/xs_main.aspx?xh=' + user
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "ASP.NET_SessionId=" + ASP_NET_SessionId,
        "Host": "121.22.25.47",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://121.22.25.47/xs_main.aspx?xh=" + user,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47 "
    }
    r = requests.get(url=url, headers=headers)
    # print(r.text)


# 获取本学期课表 信息
def get_course_default(user, ASP_NET_SessionId, xm, gnmkdm):
    cookies = {
        'ASP.NET_SessionId': ASP_NET_SessionId,
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Host": "121.22.25.47",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://121.22.25.47/xs_main.aspx?xh=" + user,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47 "

    }
    url = "http://121.22.25.47/xskbcx.aspx?xh=" + user + "&xm=" + xm + "&gnmkdm=" + gnmkdm

    data = "xh=" + user + "&xm=" + xm + "&gnmkdm=" + gnmkdm

    response = requests.post(url, headers=headers, data=data.encode("gb2312"),
                             cookies=cookies)
    s = re.findall("<br>(.*?)<br>周(.*?)第(.*?),(.*?)节{第(.*?)-(.*?)周}<br>(.*?)<br>(.*?)<", response.text, flags=0)
    print(response.text)

    print(s)

    print("我的课表")
    print("课程名称    上课时间     ")
    for a in s:
        print(a)


def pas_xkqk(raw_data):
    print(raw_data)

    week_list = ('一', '二', '三', '四', '五', '六', '日')
    day_list = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6}
    course_data = dict()

    for x in range(1, 20):
        week_data = dict()
        for y in week_list:
            day_data = dict()
            for z in range(1, 6):
                day_data[z] = ''
            week_data[y] = day_data
        course_data[x] = week_data

    # 开始数据解析

    print(str(json.dumps(course_data)))

    pra = """<td>.*?</td><td>.*?</td><td><a href='.*?'  target='_blank'>(.*?)</a></td><td>.*?</td><td>.*?</td><td><a href='.*?'  target='_blank'>"""

    course_name = re.findall(pra, raw_data)
    for ss in course_name:
        print(ss)

    pra = '<span id="DBGrid__ctl.*?_Label4">(.*?)</span>'
    course_time = re.findall(pra, raw_data)
    for aa in course_time:
        print(aa)

    index = {}

    i = 0
    for course in course_name:
        index[course] = course_time[i]
        i += 1

    print(index)

    for cou in course_name:
        print('课程名称', cou)
        print('上课时间')
        ppp = re.findall('周(.*?)第(.*?),(.*?)节{第(.*?)-(.*?)周', index[cou], 0)
        for d in ppp:
            for week_index in range(int(d[3]), int(d[4]) + 1):
                print('第', week_index, '周')
                course_data[week_index][str(d[0])][day_list[int(d[1])]] = str(cou)

    return course_data



def get_students_xsxkqk(user, ASP_NET_SessionId, xm, gnmkdm):
    cookies = {
        'ASP.NET_SessionId': ASP_NET_SessionId,
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Host": "121.22.25.47",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://121.22.25.47/xs_main.aspx?xh=" + user,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47 "
    }

    url = "http://121.22.25.47/xsxkqk.aspx?xh=" + user + "&xm=" + xm + "&gnmkdm=" + gnmkdm

    data = "xh=" + user + "&xm=" + xm + "&gnmkdm=" + gnmkdm

    response = requests.post(url, headers=headers, data=data.encode("gb2312"),
                             cookies=cookies)

    # print(response.text)

    return pas_xkqk(response.text)

def get_students_data(user, ASP_NET_SessionId, xm, gnmkdm):
    cookies = {
        'ASP.NET_SessionId': ASP_NET_SessionId,
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Host": "121.22.25.47",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://121.22.25.47/xs_main.aspx?xh=" + user,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47 "
    }

    url = "http://121.22.25.47/xsgrxx.aspx?xh=" + user + "&xm=" + xm + "&gnmkdm=" + gnmkdm

    data = "xh=" + user + "&xm=" + xm + "&gnmkdm=" + gnmkdm

    response = requests.post(url, headers=headers, data=data.encode("gb2312"),
                             cookies=cookies)
    name = re.findall(
        '<span id="xm">(.*?)</span>',
        response.text, flags=0)
    xuyuan = re.findall(
        '<span id="lbl_xy">(.*?)</span>',
        response.text, flags=0)
    class_r = re.findall(
        '<span id="lbl_zymc">(.*?)</span>',
        response.text, flags=0)
    print(response.text)
    if len(name) == 1 and len(xuyuan) == 1 and len(class_r) == 1:
        print(response.text)
        print(name[0], xuyuan[0], class_r[0])
    else:
        print("失败")
    return {
        'name': name,
        'xuyuan': xuyuan,
        'class': class_r
    }


def get_student_cj(name, user, ASP_NET_SessionId, xuenian, xueqi):
    url = "http://121.22.25.47/Xscjcx.aspx?xh=" + user + "&xm=" + str(
        parse.quote(name, encoding='gb2312')) + "&gnmkdm=N121613"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "ASP.NET_SessionId=" + ASP_NET_SessionId,
        "Host": "121.22.25.47",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://121.22.25.47/xs_main.aspx?xh=" + user,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47 "
    }
    response = requests.get(url, headers=headers)
    response.encoding = "gbk"
    view = re.findall('name="__VIEWSTATE" value="(.*?)"', response.text, 0)
    if len(view) == 1:
        print('获取到登陆成绩查询 __VIEW_STATE:', parse.quote(view[0]))
        __VIEW_STATE = view[0]
        print('开始获取成绩数据')
        data = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": __VIEW_STATE,
            "hidLanguage": "",
            "ddlXN": xuenian,
            "ddlXQ": xueqi,
            "ddl_kcxz": "",
            "btn_zcj": "历年成绩".encode('gb2312')
        }
        headerss = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "max-age=0",
            "Content-Length": "50079",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "ASP.NET_SessionId=" + ASP_NET_SessionId,
            "Host": "121.22.25.47",
            "Origin": "http://121.22.25.47",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://121.22.25.47/Xscjcx.aspx?xh=" + user + "&xm=" + str(
                name.encode('gb2312')) + "&gnmkdm=N121613",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
        }

        r = requests.post(url, headers=headerss, data=data)
        # r.encoding = 'utf-8'
        print(r.text)
        s = re.findall(
            '<td>(.*?)</td><td>(.*?)</td><td>.*?</td><td>(.*?)</td><td>(.*?)</td><td>.*?</td><td>(.*?)</td><td>   ('
            '.*?).</td><td>(.*?)</td><td>.*?</td><td>.*?</td><td>.*?</td><td>(.*?)</td><td>.*?</td><td>.*?</td>',
            r.text, 0)
        print(s)
        if len(s) > 0:
            print("成功")
            return s
        else:
            return 'error'

    else:
        print("view获取失败 下面是响应数据==============================================================")
        print(response.text)
        print("view获取失败 上面是响应数据==============================================================")
        return 'error'

# login("x03ov045umfxv0rat3fmxz55", "kahj", "0914200104", "gxy7788521")
# get_course_default("0914200104", "x03ov045umfxv0rat3fmxz55",  "高旭阳", "N121602")
# get_students_xsxkqk("0914200104", "x03ov045umfxv0rat3fmxz55",  "高旭阳", "N121602")
# get_login_view_state("lmnnf03u0ztvyvex1swebi45")
# get_student_cj("高旭阳", "0914200104", "oqok1d45c5j01oy2zirkqg3w", '2021-2022', "2")
