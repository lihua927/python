#date 2021.10.23
#author ltw
#dec 字典，列表嵌套

#字典列表
user1={
    'first':'li',
    'last':'tianwang',
    'city':'beijing',
}
user2={
    'first':'long',
    'last':'wang',
    'city':'changsha',
}
user3={
    'first':'deng',
    'last':'yao',
    'city':'wuhan',
}
users=[user1,user2,user3]
print(users)
print('\n')
for user in users:  #遍历列表
    print(user)
    print(f"He is {user['first']} {user['last']}")


print('\n')
#列表字典
love_fruits={
    'name':'lzh',
    'fruits':['apple','orange']
}
print(f'{love_fruits["name"]} like eat :')
for fruit in love_fruits['fruits']:
    print(fruit)

print('\n')
#字典套字典
uses={
    'lzh':{'age':19,'high':180},
    'dxy':{'age':18,'high':170},
}
for name,info in uses.items():
    print(f"{name} infomation is: {info}")
    print(f"{name} age is {info['age']}")
    print(f"{name} high is {info['high']}")
