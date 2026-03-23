#！/usr/bin/env python3
#-*- coding: utf-8 -*-

height = float(input('请输入身高（m）：'))
weight = float(input('请输入体重（kg）：'))

bmi = weight / (height * height)
if bmi < 18.5:
    print('您的bmi指数反映你的体型过轻')
elif bmi < 25:
    print('您的bmi指数反映你的体型正常')
elif bmi < 28:
    print('您的bmi指数反映你的体型过重')
elif bmi < 32:
    print('您的bmi指数反映你的体型肥胖')
else:
    print('您的bmi指数反映你的体型严重肥胖')
