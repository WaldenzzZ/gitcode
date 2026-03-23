#!/usr/bin/env python3
#-*- coding: utf-8 -*-

age = int(input('请输入年龄：'))

match age:
    case x if x < 10:
        print(f'输入的年龄是儿童，年龄为 {x} 岁')
    case 10:
        print('输入的年龄是10岁, 是个少年')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print(f'输入的年龄是青少年，年龄为 {age} 岁')
    case x if x < 60:
        print(f'输入的年龄是成年人，年龄为 {x} 岁')
    case x if x < 120:
        print(f'输入的年龄是老年人，年龄为 {x} 岁')
    case _:
        print('输入的年龄无效,请输入一个合理的年龄')