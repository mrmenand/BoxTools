import os
import shutil


def merge(a_path, b_path):
    """把B目录合并到A目录，文件名只有前面ID相同"""
    b_paths = os.listdir(b_path)
    a_paths = os.listdir(a_path)
    for fn_b in b_paths:  # folder name in  B
        tmp = []
        for fn_a in a_paths:
            if fn_a.startswith(fn_b):
                tmp.append(fn_a)
            # 字符串排序，匹配ASCII码最大的,在项目需求中ord("_")=95比数字大很多，即最短
        if tmp:
            b_new_path = os.path.join(b_path, fn_b)
            a_new_path = os.path.join(a_path, max(tmp))
            #

            for item in os.listdir(b_new_path):
                b_item = os.path.join(b_new_path, item)
                if os.path.isfile(b_item):
                    shutil.copy(b_item, a_new_path)
        else:
            # 目录不存在 
            continue


if __name__ == '__main__':
    merge("./B/", "./A/")
