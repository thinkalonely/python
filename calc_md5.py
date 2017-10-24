# !/usr/bin/env python
# -*- utf-8 -*-

import hashlib

db = {}
salt = 'pythonisbest'
print('请注册：')
username = input('Please input your username: ')
if username in db:
    print(username + 'is already registed!')
password = input('Please input your password: ')

def get_md5(password):
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    return pw_md5.hexdigest()

def register(user, passwd):
    db[user] = get_md5(user + passwd + salt)
    print('注册成功，请登录：')

def login():
    user = input('Please input user: ')

    if user in db:
        passwd = input('Please input password: ')
        password = get_md5(passwd)
        if password == db[user]:
            print('登录成功！')
        else:
            print('密码错误！')
    else:
        print('User not exist!')
    return login()
register(username, password)
login()
