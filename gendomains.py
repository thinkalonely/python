import random
import string
order = input("Please input:\n 字母加数字选择 1：\n 全字母选择2：\n 全数字选择3：\n 清空文本按 d: ")

tmplist = []
list1 = string.ascii_lowercase + string.digits
list2 = string.ascii_lowercase

numlist = string.digits
namepath ='C:\\users\\hoo\desktop\\domains.txt'

if order == '1':
    tmplist = list1
elif order == '2':
    tmplist = list2
elif order == '3':
    tmplist = numlist
elif order == 'd':
	print('正在清除数据...')
	with open(namepath, 'w') as f:
		f.write('')
	print('完成 ！')
def write_txts():
	tname = set()
	num = input("Please input 生成长度:")
	startstr = input("enter startstr: ")
	endstr = input("enter endstr: ")
	print("Please wait a moument")
	for i in range(590):
		ch = startstr + ''.join(i for i in random.sample(tmplist, int(num))) + endstr
		tname.add(ch)
	print("All about %s donames." % len(tname))
	for ch in tname:
		with open(namepath, 'a') as f:
			f.write(ch+'\n')
if order != 'd':
	write_txts()
