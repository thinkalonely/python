# !/usr/bin/python
# -*- utf-8 -*-

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
std = Student('Bob', 23, 80)

print(json.dumps(std, default=lambda obj: obj.__dict__))
