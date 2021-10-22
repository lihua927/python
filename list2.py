#date: 2021.10.21
#author: 李天王
#desc: 列表的排序

#sort方法永久改变元素顺序
names=['pig','cat','dog','apple']
print(f'This is old sort:\n{names}')
names.sort()
print(f'This is new sort:\n{names}')
print('names\n')

#sorted()函数临时改变列表值
friends=['lzh','adf','cdf','mnt']
print(f'It is old sort:\n{friends}')
print(f'It is new sort（small--big）:\n{sorted(friends)}')
print(f'It is new sort（big--small）:\n{sorted(friends,reverse=True)}')
print(friends)
print(f'list friends is {len(friends)} cm\n') #求列表长度

#反转顺序
friends.reverse()
print(friends)
#回正顺序
friends.reverse()
print(friends)

