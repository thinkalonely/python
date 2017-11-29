# -*- coding: utf-8 -*-
# 操作注册表

import winreg
from tkinter import *
from tkinter import messagebox
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\yxt")

#newKey = winreg.CreateKey(key, "11")
#winreg.SetValueEx(newKey, "test2", 0, winreg.REG_SZ, "223")

def reg_subkey():
    try:
        i = 0
        data = []
        while 1:
            # EnumValue方法用来枚举键值，EnumKey用来枚举子键
            value = winreg.EnumKey(key, i)

            data.append(value)

            print(value)
            i = i + 1
    except OSError as err:
        print(err)
    finally:
        return data

print(reg_subkey())
#winreg.SetValue(key, "11", winreg.REG_SZ, '234')
#newKey = winreg.CreateKey(key,"MyNewkey")
#给新创建的键添加键值
#winreg.SetValue(newKey, "ValueName", winreg.REG_SZ,"ValueContent")
#winreg.SetValueEx(key,"NetworkAddress",0,winreg.REG_SZ,'234234234')
#winreg.DeleteKey(key, "test")

# 删除键
# winreg.DeleteKey(key, "Advanced")

# 删除键值
# winreg.DeleteValue(key, "IconUnderline")

# 创建新的键
# newKey = winreg.CreateKey(key,"Mykey1")

# 给新创建的键添加键值
#winreg.SetValue(key, "test1", winreg.REG_SZ, "333")
#winreg.SetValueEx(key, value_name, reserved, type, value)