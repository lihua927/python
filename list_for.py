#date: 2021.10.22
#author: 李天王
#desc: 列表操作


#for循环调用列表元素
foods=['apple','blana','rice','cooke']
for food in foods:
    print(f'I like eat {food}')
    print('It is nice\n')
print('what food do you like best?')

#range的使用
for num in range(1,11):
    print(num)
nums=list(range(10))
print(nums)
print(sum(nums))
print('\n')

#打印20以内奇数
for ji in range(1,20,2):
    print(ji)

#将1-10的平方放进列表中
squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

#列表解析
new_squares=[i**2 for i in range(1,11)]
print(new_squares)