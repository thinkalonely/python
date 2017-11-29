# -*- coding: utf-8 -*-
# 操作注册表

import winreg
from tkinter import *
from tkinter import messagebox
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\yxt")

def insert_reg():
    Ename = ('user', 'password', 'database', 'host', 'port', 'connect_timeout')
    data = []

    k_name = e.get()
    e.delete(0, END)
    data.append(e1.get())
    e1.delete(0, END)
    data.append(e2.get())
    e2.delete(0, END)
    data.append(e3.get())
    e3.delete(0, END)
    data.append(e4.get())
    e4.delete(0, END)
    data.append(e5.get())
    e5.delete(0, END)
    data.append(e6.get())
    e6.delete(0, END)

    if len(k_name) > 0:
        try:
            newKey  =  winreg.CreateKey(key, "%s" % k_name)


            i = 0
            while i < 6:
                if len(data[i]) > 0:

                    winreg.SetValueEx(newKey, "%s" % Ename[i], 0, winreg.REG_SZ, "%s" % data[i])
                    i = i + 1
                    messagebox.showinfo('info', '第%d项更新 Success' % i)

                elif len(data[i]) == 0:
                    i = i + 1
                    messagebox.showinfo('info', "第%d项输入的值为空、此项不更新" % i)
        except OSError as err:
            messagebox.showinfo('Error:', '%s' % err)
    else:
        messagebox.showinfo('info', "项名 输入的值为空！")
def reg_subkey():
    try:
        i = 0
        data = []
        while 1:
            # EnumValue方法用来枚举键值，EnumKey用来枚举子键
            value = winreg.EnumKey(key, i)

            data.append(value)
            i = i + 1
    except OSError as err:
        print()
    finally:
        return data
def delete_reg():

    k_name = e.get()
    #e.delete(0, END)
    names = reg_subkey()
    
    if (k_name in names):
        try:
            winreg.DeleteKey(key, "%s" % k_name)
            messagebox.showinfo('info', 'Delete Success')
        except OSError as err:
            messagebox.showinfo('Error:', '%s' % err)
    else:
        messagebox.showinfo('info', '输入的项名不存在！')
    

root = Tk()
root.title('操作注册表')
win = Frame(root, height=195, width=320)
win.grid_propagate(False)
win.grid()
L = Label(win, text="请输入项名: ")
L.grid(row=0, column=0,sticky='W')
e = Entry(win,width=20)
e.grid(row=0, column=2,sticky='W',columnspan=2)
Label(win, text="请输入键值: ").grid(row=1, column=0,sticky='W')
L1 = Label(win, text="user: ")
L1.grid(row=2, column=0,sticky='W')
e1 = Entry(win,width=20)
e1.grid(row=2, column=2,sticky='W',columnspan=2)
L2 = Label(win, text="pasd: ")
L2.grid(row=3, column=0,sticky='W')
e2 = Entry(win,width=20)
e2.grid(row=3, column=2,sticky='W',columnspan=2)
L3 = Label(win, text="data: ")
L3.grid(row=4, column=0,sticky='W')
e3 = Entry(win,width=20)
e3.grid(row=4, column=2,sticky='W',columnspan=2)
L4 = Label(win, text="host: ")
L4.grid(row=5, column=0,sticky='W')
e4 = Entry(win,width=20)
e4.grid(row=5, column=2,sticky='W',columnspan=2)
L5 = Label(win, text="port: ")
L5.grid(row=6, column=0,sticky='W')
e5 = Entry(win,width=20)
e5.grid(row=6, column=2,sticky='W',columnspan=2)
L6 = Label(win, text="time: ")
L6.grid(row=7, column=0,sticky='W')
e6 = Entry(win,width=20)
e6.grid(row=7, column=2,sticky='W',columnspan=2)



button_1 = Button(win, text="写入",bg="green", height=1,width=5, command=insert_reg)
button_1.grid(row=1, column=5, sticky='E')
button_2 = Button(win, text="删除",bg="red", height=1, command=delete_reg)
button_2.grid(row=1, column=6, sticky='E')
root.mainloop()