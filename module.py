#date 2021.10.28
#author ltw
#dec  使用模块

#1.直接导入整个模块
'''
import del3 as d
del3.order('gouqi','milk','pear')
'''
#2.导入模块中的某一个函数
from del3 import order as a   #as 定义别名，可避免与本程序函数名冲突
a('egg','milk','rou')

print('\n')
#3.导入模块的所有函数，此方法调用函数时。可直接写函数名。但对于大型模块不推荐
from del3 import *
order('niu','bi')