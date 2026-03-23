#! /usr/bin/env python3
#-*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

#print(L[0][0])  # Apple
#print(L[1][1])  # Python
#print(L[2][2])  # Lisa

n1 = input('输入list行数（0-2）：')
n2 = input('输入list列数（0-3）：')
print('你查询的内容是：', L[int(n1)][int(n2)])