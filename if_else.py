#date: 2021.10.21
#author: 李天王
#desc: if语句的使用

#1.1
color='green'
if(color=='green'):
    print('It is true')
else:
    print('It is false')

#1.2
age=int(input('输入你的年纪：'))  #这里注意类型
if(age < 13):
    print('You are a child')
elif(age < 18):
    print('You are a teneger')
elif(age < 50):
    print('You are a mider')
else:
    print('You are a older')

#1.3
mylove=['csl','cl','dxy']
if 'dxy' in mylove:
    print(f'\nI really like eat dxy')
if 'lc' in mylove:
    print('I really like eat lc')
if 'csl' in mylove:
    print("I really like eat csl")
print('how about you?')

