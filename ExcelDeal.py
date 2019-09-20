import json
import os
from collections import defaultdict

from xlrd import open_workbook
from xlutils.copy import copy

read_excel = open_workbook("./Meal80K.xlsx") # 用wlrd提供的方法读取一个excel文件
read_table = read_excel.sheets()[0]
rows = read_table.nrows # 用wlrd提供的方法获得现在已有的行数
cols = read_table.ncols # 用wlrd提供的方法获得现在已有的列数
write_excel = copy(read_excel) # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
write_table = write_excel.get_sheet(0) # 用xlwt对象的方法获得要操作的sheet

path_of_all = r"/home/guangyixiao/zhangqi/300_exp/all_data/"
list_dirs_data = os.listdir(path_of_all)
FILTER = ['other','other_weiKaiDai','weiKaiDai']
if FILTER[0] in list_dirs_data:
    list_dirs_data = list(set(list_dirs_data)^set(FILTER))

dict_dir_num = defaultdict(list)

for dir in list_dirs_data:
    num_pics = len(os.listdir(path_of_all+"/"+dir))
    dict_dir_num[dir].append(num_pics)



json_path = "./food_type_20180515_201908240936.json"
with open(json_path,"r") as js:
    js_content = json.load(js)
    for item in js_content["food_type_20180515"]:
        food_type = str(item["id"]) + "_" + item["pin_yin_short"]
        name = item["name"]
        if food_type in dict_dir_num:
            dict_dir_num[food_type].append(name)

for row in range(1,rows):
    tmp = []
    values = read_table.row_values(row)
    food_type= values[1]
    for food in list_dirs_data:
        if food.startswith(food_type):
            tmp.append(food)
    if tmp:
        write_table.write(row, 1, max(tmp))
        write_table.write(row, 2, dict_dir_num[max(tmp)][0])

        dict_dir_num.pop(max(tmp))
    else:
        continue

for k,v in dict_dir_num.items():
    if len(v)>1:
        write_table.write(rows, 1, k)
        write_table.write(rows, 2, v[0])
        write_table.write(rows, 3, v[1])
        rows += 1
write_excel.save("./Meal80K.xlsx") # xlwt对象的保存方法，这时便覆盖掉了原来的excel
