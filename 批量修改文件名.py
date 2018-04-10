import os
path = '/Users/changzhang/Desktop/实验专用文件夹/'
# 获得路径下所有文件名列表
dir_name = os.listdir(path)
list_file_time = {}
for i in dir_name:
    # new_name = 'chanzghang' + i

    # Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
    # num = i.rfind('g')
    # new_name = i[num + 1:]
    # os.rename(path + i, path + new_name)
    # list_file_time[os.path.getctime(path + i)] = i
    print(os.path.getctime(path + i))

# print(list_file_time)
