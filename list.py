#date: 2021.10.21
#author: 李天王
#desc: 学习列表

#1.1引用列表元素
frinds=['lzh','dxy','sh']
print(frinds)
print(frinds[-1])
welcome="welcome to my party"
print(f'{frinds[1]}, {welcome}')
print('\n')
#1.2列表元素的增删改操作
frinds[0]='ltw'
frinds.append('dlz')
print(frinds)
#删除，插入元素
del frinds[2]
frinds.insert(2,'csl')
print(frinds)
teacher=frinds.pop()  #将元素弹出
print(f'{teacher},you are a good girl')
print(frinds)