#date 2021.10.23
#author ltw
#dec while处理列表和字典

order_list=['beff','vegetable','milk','milk']
finish_list=[]
while order_list:
    print('waiting......')
    now_food=order_list.pop()
    print(f'Now is add {now_food}')
    finish_list.append(now_food)
print(f'All is ok!---{finish_list}')

#删除所有特定值
# print('\n')
# pets=['cat','dog','cat','pig']
# print(pets)
# kill=input('what do you want to remove?')
# while kill in pets:
#     pets.remove(kill)
# print(pets)

resposes={}
sign=True
while sign:
    name=input('what is your name?')
    respose=input('where city do you like?')
    resposes[name]=respose #将调查结果放入字典
    #是否继续
    come_on=input('would you like to ask your friend?(y/n)')
    if come_on == 'n':
        sign=False
print('\n____result____')
for key,values in resposes.items():
    print(f'{key} like {values}')
