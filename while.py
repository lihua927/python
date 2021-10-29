#date 2021.10.23
#author ltw
#dec while的使用
#不断要求输入，知道遇到quit

# info='please input your peiliao("quit"):'
# while True:
#     pizza=input(info)
#     if pizza == 'quit':
#         break
#     print(f'I will add {pizza}')

sign=True
while sign:
    age=int(input('input your age:'))
    if age < 3:
        print('For free')
        sign = False
    elif age < 12:
        print('pay for 10$')
    else:
        print('pay for 15$')
