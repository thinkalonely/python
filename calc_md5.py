# !/usr/bin/env python
# -*- utf-8 -*-

import hashlib

user = input('Please input your username: ')
passwd = input('Please input your password: ')
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def calc_md5(password):
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    return pw_md5.hexdigest()

def login(user, password):
    if user in db:
        if password == db[user]:
            print('登录成功！')
        else:
            print('密码错误！')
    else:
        print('User not exist!')

password = calc_md5(passwd)
login(user, password)

