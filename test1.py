#date: 2021.10.21
#author: 李天王
#desc: 字符串连接
#1.1
name='lzh'
message=f"hello {name},you are my good friend!"
print(message)

#1.2大小写
name="dxy"
print('\n')
print(name.upper())
print(name.title())
print(name.lower())

#1.3
print('\n')
author='lzh'
massage=f'{author} once said,"lzh is a good man"'
print(massage)

#1.4删除字符串两边空格
print('\n')
name=' terminal '
print(name.lstrip())
print(name.strip())
print(name.rstrip())

#1.5
print(3+5)
print(2*4)
print(2**3)
print(16/2)
print(16//2)  #整除
print(16%2)