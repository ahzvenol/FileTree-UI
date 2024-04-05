import json
import os
import time

arr = []


def recursive(path, arr):
    file_list = os.listdir(path)
    # 通过奇怪的方式判断文件和文件夹(文件夹无扩展名,无法找到'.') # 早晚要改
    file_list.sort(key=lambda x: x.find('.'))
    for file in file_list:
        absolute_path = os.path.join(path, file)
        create_time = int(time.mktime(time.localtime(os.path.getctime(absolute_path))))
        modify_time = int(time.mktime(time.localtime(os.path.getmtime(absolute_path))))
        if os.path.isdir(absolute_path):
            arrr = []
            recursive(absolute_path, arrr)
            arr.append(
                {"info": {"fileName": file, "createTime": create_time, "modifyTime": modify_time}, "content": arrr})
        else:
            arr.append({"info": {"fileName": file, "size": os.stat(absolute_path).st_size, "createTime": create_time,
                                 "modifyTime": modify_time}})


recursive(os.getcwd(), arr)
with open(os.getcwd() + '\\FileTree.json', 'w', encoding='utf-8') as f:
    json.dump(arr, f, ensure_ascii=False, indent=4)
