#组合练习，输入、存储、调用函数计算最大值，输出，format格式化输出

count = int(input('请输入数字数量: '))
numbers = []

for i in range(count):
    num = int(input(f'请输入第{i + 1}个数字: '))
    numbers.append(num)

max_number = max(numbers)
print('最大的数字是:', max_number)
#print('这个数字的十六进制表示为:', hex(max_number))
print(f'{max_number} 的十六进制表示为: {hex(max_number)}')