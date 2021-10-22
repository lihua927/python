#date: 2021.10.2
#author: 李天王
#desc: 列表切片
animals=['hourse','cat','dog','pig','cow']
for animal in animals:
    print(animal)
print(f'\n{animals[:3]}')   #前三个
print(animals[1:4])  #中三个
print(animals[-3:])  #后三个

new_animals=animals[:]
animals.append('old')
new_animals.append('new')
print(f'\nThis is old list: {animals}')
print(f'This is new list: {new_animals}')

#元组，元素值不能修改的列表
size= (18,4)
for i in size:
    print(i)
#size[0]=20 #不能修改
size=(20,5)  #元组整体修改可行
print(size)
