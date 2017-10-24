# !/usr/bin/env python
# -*- utf-8 -*-

import hashlib

db = {}
salt = 'pythonisbest'

def get_md5(password):
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    return pw_md5.hexdigest()

def register():
    print('请注册：')
    user = input('Please input your username: ')
    if user in db:
        print(user + 'is already registed!')
        print('请登录：')
    else:
        passwd = input('Please input your password: ')
        db[user] = get_md5(user + passwd + salt)
        print('注册成功，请登录：')
    login()

def login():
    user = input('Please input user: ')

    if user in db:
        passwd = input('Please input password: ')
        password = get_md5(user + passwd + salt)
        if password == db[user]:
            print('登录成功！')
        else:
            print('密码错误！')
            print('重新登录')
            login()
    else:
        print('User not exist!')
        register()
register()
print(db)
