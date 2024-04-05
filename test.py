import sqlite3


def get_login_data(openid):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    cursor = c.execute("SELECT * FROM wx_user_data where openid = \'" + openid+"\'")
    print("SELECT * FROM wx_user_data where openid = \'" + openid+"\'")
    if len(cursor.fetchall()) == 1:
        print("已经存在的用户")
        return "exist"
    else:
        print("新用户")
        cursor = c.execute("insert into wx_user_data values ('" + str(openid) + "','','','','未绑定','')")
        conn.commit()
        return "new_user"


def get_user_informations(openid):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * FROM wx_user_data where openid = \'" + openid+"\'")
    da = cursor.fetchall()[0]
    user_dat = {
        "user": da[1],
        'pass': da[2],
        "cookie": da[3],
        "name": da[4],
        "class": da[5],
    }
    print(user_dat)
    return user_dat
