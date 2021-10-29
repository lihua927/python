#date 2021.10.28
#author ltw
#dec  函数传递列表
def show_massage(infos):
    for info in infos:
        print(f'hello,{info}')


def send_massage(infos,hellos):
    while infos:
        mid=infos.pop()
        hellos.append(mid)
    print(f'hellos:{hellos}')
    print(f'infos:{infos}')

names=['lzh','dxy','cl']
isok=[]
send_massage(names[:],isok) #使用切片不会影响原列表
print(names)
print(isok)