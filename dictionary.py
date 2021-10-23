#date 2021.10.23
#author ltw
#dec 字典的使用

myinfo={
    'first name':'li',
    'last name':'tianwang',
    'age' :18,
    'city':'beijing',
}
print(myinfo)
print(f"my age is {myinfo['age']}") #输出某个元素

#增加键值对
myinfo['high']=180

#修改键值对
myinfo['age']=19

#删除键值对
del myinfo['city']
print(myinfo)

#获取不存在键值对时，返回一条消息，而不是报错
test=myinfo.get('niu','It is nothing')
print(test)