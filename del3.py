#date 2021.10.28
#author ltw
#dec  实参为可变长元组或字典

#该函数主要用来模拟收集客户的所有食物需求,并打印出来
#参数不定长
def order(*foods):
    print('your order list is:')
    for food in foods:
        print(food)
    print(foods) #本质上把所有参数放进了foods元组中
# order('cow','milk')

print('\n')
#该函数功能为收集用户的信息，并以字典的形式表现出来
#其中前两个字段必须提供，后一个看需求添加
def user(first,last,**o_infos):
    o_infos['xing']=first
    o_infos['ming']=last
    return o_infos

# myinfo=user('li','hua')
# print(myinfo)
# yourinfo=user('deng','yao',sex='female')
# print(yourinfo)