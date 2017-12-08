# /usr/bin/env python
# -*- utf-8 -*-

import re

mail = 'test.3@test.com'
rechar = r'^([a-z_0-9.-]{1,64})@([a-z0-9-]{1,200})(.{1,5}[a-z]{1,6})$'
# 用户名匹配字母或数字或-或_或.的组合
# 域名匹配 字母数字‘-’的组合

result = re.match(rechar, mail)
print(result)
