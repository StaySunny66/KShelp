import json
from io import BytesIO

from flask import Flask, send_file, make_response
from flask import request
import requests
import prase
import test
import publicweb

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.get("/img")
def get_img():
    r = requests.get("http://121.22.25.47/CheckCode.aspx")
    resp = make_response(send_file(BytesIO(r.content), mimetype='image/gif'))
    resp.set_cookie("SameSite", "None", path="http://127.0.0.1:5000/")
    resp.set_cookie("ASP.NET_SessionId", r.cookies['ASP.NET_SessionId'], path="http://127.0.0.1:5000/")
    return resp


@app.get("/mycourse")
def get_my_course():
    yz_code = request.args.get("yz_code")
    user = request.args.get("user")
    password = request.args.get("password")
    cookie_id = request.cookies['ASP.NET_SessionId']
    login_result = prase.login(ASP_NET_SessionId=cookie_id, user=user, password=password, yz_code=yz_code)
    if login_result == 'error':
        return json.dumps({
            'errno': 1
        })
    else:
        course = prase.get_students_xsxkqk(user=user, ASP_NET_SessionId=cookie_id, xm=login_result['name'],
                                           gnmkdm="N121602")

        return json.dumps({
            "errno": 0,
            "data": course
        })


@app.get("/wx/mycourse")
def wx_get_my_course():
    yz_code = request.args.get("yz_code")
    user = request.args.get("user")
    password = request.args.get("password")
    cookie_id = request.args.get("cookie")
    login_result = prase.login(ASP_NET_SessionId=cookie_id, user=user, password=password, yz_code=yz_code)
    if login_result == 'error':
        return json.dumps({
            'errno': 1
        })
    else:
        course = prase.get_students_xsxkqk(user=user, ASP_NET_SessionId=cookie_id, xm=login_result['name'],
                                           gnmkdm="N121602")

        return json.dumps({
            "errno": 0,
            "data": course
        })


# 微信绑定接口 返回 errno userdata
@app.get("/wx/bangding")
def wx_bangding():
    yz_code = request.args.get("yz_code")
    user = request.args.get("user")
    password = request.args.get("password")
    cookie_id = request.args.get("cookie")
    login_result = prase.login(ASP_NET_SessionId=cookie_id, user=user, password=password, yz_code=yz_code)
    if login_result == 'error':
        # 返回 errno = 1发送错误取消登录
        return json.dumps({
            'errno': 1
        })
    else:
        user_data = prase.get_students_data(user=user, ASP_NET_SessionId=cookie_id, xm=login_result['name'],
                                            gnmkdm="N121501")

        return json.dumps({
            "errno": 0,
            "data": user_data
        })


@app.get("/login")
def login():
    return send_file("templates/1.html")


@app.get("/wx/imgcode")
def get():
    r = requests.get("http://121.22.25.47/CheckCode.aspx")
    open(f'img_buff/' + r.cookies['ASP.NET_SessionId'] + '.png', 'wb+').write(r.content)
    return r.cookies['ASP.NET_SessionId']


@app.get("/wx/getcj")
def get_cj():
    name = request.args.get("name")
    user = request.args.get("user")
    xuenian = request.args.get("xuenian")
    cookie_id = request.args.get("cookie")
    xueqi = request.args.get("xueqi")

    cj_data = prase.get_student_cj(name, user, cookie_id, xuenian, xueqi)
    if cj_data == 'erro':
        print('成绩获取失败')
        return json.dumps({
            'errno': 1,
            'data': ''

        })
    else:
        return json.dumps({
            'errno': 1,
            'data': cj_data

        })


@app.get("/img_buff")
def send_img():
    img_id = request.args.get("img_id")
    return send_file('img_buff/' + img_id + '.png', mimetype='image/gif')


@app.get("/wx/user_login")
def get_user_information():
    code = request.args.get('code')

    params = {
        "appid": "wx8189b29a80e907fe",
        "secret": "543c26472e6936aabecb2e17228301d4",
        "js_code": code,
        "grant_type": 'authorization_code'

    }

    url = "https://api.weixin.qq.com/sns/jscode2session"
    r = requests.get(url=url, params=params)
    json.loads(r.text)
    openid = json.loads(r.text)["openid"]
    print(openid)

    if test.get_login_data(openid) == 'exist':
        state = 1
    else:
        state = 0

    ret_dat = {
        "state": state,
        "data": test.get_user_informations(openid=openid),
        "openid": openid

    }
    print(ret_dat)

    return ret_dat


@app.get("/wx/getNewsList")
def get_News_List():
    pub = publicweb.HevttcPubWeb()
    return json.dumps(pub.get_news())


@app.get("/wx/getJwcList")
def get_Jwc_List():
    pub = publicweb.HevttcJwcWeb()
    return json.dumps(pub.get_news())


@app.get("/wx/getArticle")
def get_Article():
    url = request.args.get("url")
    pub = publicweb.HevttcPubWeb()
    return json.dumps(pub.get_page_detail(url))


if __name__ == '__main__':
    app.run()
