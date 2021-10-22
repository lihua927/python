#date: 2021.10.21
#author: 李天王
#desc: if和for语句的使用
#1.1
users=['admin','ltw','dxy']
for user in users:
    if(user == 'admin'):
        print(f'{user}你充了钱，你老大')
    else:
        print(f'hello {user},你今天可以充钱了吗？\n')

#1.2
names=[]
if names:
    print('I have many friends')
else:
    print('I am a 小丑\n')

#1.3 添加用户名到已知列表（区分大小写）
cur_users=['zz','ltw','Lzh']
cur_users_baks=cur_users[:]  #创建列表副本
for i in range(len(cur_users_baks)):
    cur_users_baks[i]=cur_users_baks[i].lower() #将副本列表全部转换为小写

print(cur_users)
user=input('请输入用户名：')
if user.lower() in cur_users_baks:
    print('username is owned,please input new name')
else:
    cur_users.append(user)
    print('username created')
print(cur_users)