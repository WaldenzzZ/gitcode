#按顺序打印名字
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#按顺序累加list中的数字
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

#range()函数生成一个证书序列，再通过list()函数转换为list，再进行列加
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while循环，只要条件满足，就不断循环，直到条件不满足时退出循环
#第一次循环是将99加到sum中，然后n-2变成了97，第二次循环是n依然大于0，所以继续循环，将97加到sum中，直到n不大于0
#最后输出的sum就是100以内的所有奇数的和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


n = 1
while n <= 20:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
