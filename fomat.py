#! /usr/bin/env python3
#sys.path.append('D:/Code/gitcode')
#-*- coding: utf-8 -*-
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位


s1 = input('小明去年的成绩：')
s2 = input('小明今年的成绩：')
r = (int(s2) - int(s1)) / int(s1)
print('小明的成绩提升了 {:.1%}'.format(r))
#print('小明的成绩提升了 {:.1%}'.format((int(s2) - int(s1)) / int(s1)))
#print('小明的成绩提升了 {:.1%}'.format((85 - 72) / 72))
#print('小明的成绩提升了 {:.1%}'.format(13 / 72))
#print('小明的成绩提升了 {:.1%}'.format(0.18055555555555555))
#print('小明的成绩提升了 {:.1%}'.format(0.2))