#date 2021.10.23
#author ltw
#dec 字典的遍历

myinfo={
    'first name':'li',
    'last name':'tianwang',
    'age' :18,
    'city':'beijing',
}
for key,values in myinfo.items():   #注意使用items转换为键值对列表
    print(f'The people {key} is {values}')

print('\n')

revers={
    'china':'changjiang',
    'us':'mixixibi',
    'aiji':'nile',
    'egypt':'nile',
}
#遍历键
for country in revers.keys():
    if country=='china':
        print(f'{country} has {revers[country]}')

    else:
        print(country)

print('\n')
#遍历值，并去重（利用集合的互异性）
for rever in revers.values():
    print(rever)

print('\n')
for rever in set(revers.values()):
    print(rever)
