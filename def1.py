#date 2021.10.28
#author ltw
#dec 函数的定义

#函数的定义
# def display_message():
#     print('I am studying def')
#
#
# def like_book(title):
#     print(f'I like read {title}')
#
# display_message()
# like_book('<Are men are brothers>')

def cloth(size,color):
    print(f'This cloth size is {size} and color is {color}')

cloth('small','red')
cloth(size='big',color='green')

#指定默认参数
def city(name,country='china'):
    print(f'{name} is in {country}')
city('changsha')
city('lundom','us')
print('\n')
#带返回值的函数
def city_country(name,country):
    return f"{name},{country}"

print(city_country('wuhan','hubei'))

print('\n')
#返回字典
def make_album(name,album,nums=None):
    a={'name':name,'album':album}
    if nums:
        a['nums']=nums
    return a
# music=make_album('lzh','high')
# music1=make_album('dxy','niu',6)
# print(music)
# print(music1)
# print('\n')

while True:
    print('Ask some questions to you("q" to quit)')
    singer=input('input your singer: ')
    if singer == 'q':
        break
    zhuanji=input('his album is: ')
    if zhuanji == 'q':
        break
    info=make_album(singer,zhuanji)
    print(info)