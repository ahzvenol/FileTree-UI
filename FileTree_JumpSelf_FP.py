import json
import os
import time

global_array = []

jump_self = True
jump_desktop_ini = True


def recursive(path, array):
    file_list = list(filter(lambda x: x != 'desktop.ini' or is_self(x) or is_desktop_ini(x), os.listdir(path)))
    file_list = list(map(lambda x: (x, os.path.join(path, x)), file_list))
    file_list.sort(key=lambda x: os.path.isfile(x[1]))
    print(file_list)
    for file_name, absolute_path in file_list:
        create_time = int(time.mktime(time.localtime(os.path.getctime(absolute_path))))
        modify_time = int(time.mktime(time.localtime(os.path.getmtime(absolute_path))))
        if os.path.isdir(absolute_path):
            arr = []
            recursive(absolute_path, arr)
            array.append(
                {"info": {"fileName": file_name, "createTime": create_time, "modifyTime": modify_time},
                 "content": arr})
        else:
            array.append(
                {"info": {"fileName": file_name, "size": os.stat(absolute_path).st_size, "createTime": create_time,
                          "modifyTime": modify_time}})


self_name = os.path.basename(__file__).split("/")[-1]


def is_self(file):
    return jump_self and file == self_name


def is_desktop_ini(file):
    return jump_desktop_ini and file == 'desktop.ini'


recursive(os.getcwd(), global_array)
with open(os.getcwd() + '\\FileTree.json', 'w', encoding='utf-8') as f:
    json.dump(global_array, f, ensure_ascii=False, indent=4)
