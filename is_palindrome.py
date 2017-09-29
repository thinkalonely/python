# !/usr/bin/python
# -*- utf-8 -*-
def is_palindrome(num):
    mun = int(str(num)[::-1])
    return mun == num
output = filter(is_palindrome, range(1, 100))
print(list(output))
def is_palindrome_str():
    out_str = ins_str[::-1]
    if out_str == ins_str:
        return ins_str + '---YES'
    else:
        return ins_str + '---NO'
ins_str = input("please inout a string: ")
if __name__ == "__main__":
    rome_str = is_palindrome_str()
    print(rome_str)
