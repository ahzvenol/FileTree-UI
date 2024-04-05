import json
import os
import time

global_array = []

jump_self = True
jump_desktop_ini = True


def recursive(path, array):
    file_list = []
    for file_name in os.listdir(path):
        file_list.append((file_name, os.path.join(path, file_name)))
    file_list.sort(key=lambda x: os.path.isfile(x[1]))
    for file_name, absolute_path in file_list:
        if file_name == 'desktop.ini' or is_self(file_name) or is_desktop_ini(file_name):
            continue
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
