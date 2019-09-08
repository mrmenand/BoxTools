import json
import xlrd
from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Page, Sunburst

def Excel2_enjson(xlsx_file):
    parent = ["Water, wild vegetables", "Flower", "Bamboo shoots", "Onion, ginger, garlic", "Pickled salt, fungi", "Chili",
              "Rhizome beans", "Melon", "Leafy vegetables",
              "Processed soy products", "Processing dairy products", "Fruit", "Citrus", "Tropical fruit",
              "Peach and plum jujube", "Melon and fruit", "Pear",
              "Apple", "Eggs", "Mutton", "Chicken, duck, goose", "Beef", "Pork", "Seafood", "Frozen goods",
              "Chilled", "Dry goods", "Freshwater live fresh", "North and South dry goods", "Whole grains"]
    ancestor = ["Vegetables", "Manufactured food", "Fresh fruits", "Meat & eggs", "Aquatic species",
                "Grain & oil non-staple food"]
    meal_parent, meal_ancestor = {}, {}  # 父类，祖先类对象
    meal_ancestor_list = []  # 祖先类列表
    meal_parent_list = []  # 父类列表
    meal = {}  # 品种对象
    meal_children_list = []  # 子类品种列表

    excel_file = xlrd.open_workbook(xlsx_file)
    sheet1 = excel_file.sheets()[0]
    n_rows = sheet1.nrows

    count = [0]  # 父类数量列表
    ancestorcount = 0  # 祖先类数量
    parent_id = 0  # 父类索引
    ancestor_id = 0  # 祖先类索引
    ancestor_front = 0  # 用于祖先类数量求和
    for row in range(1, n_rows):
        values = sheet1.row_values(row)
        if (values[-5] != parent_id + 1):
            meal_parent["name"] = parent[parent_id]
            meal_parent["value"] = count[parent_id]
            meal_parent["children"] = meal_children_list.copy()
            meal_parent_list.append(meal_parent.copy())
            meal_children_list.clear()
            count.append(0)
            parent_id = parent_id + 1
        zh_name = values[3]
        en_name = values[6]
        meal["zh_name"] = zh_name
        meal["name"] = en_name
        meal["value"] = 1
        meal_children_list.append(meal.copy())
        count[parent_id] = count[parent_id] + 1
        if (values[-1] != ancestor_id + 1):
            meal_ancestor["name"] = ancestor[ancestor_id]
            for z in range(ancestor_front, parent_id):
                ancestorcount += count[z]
            meal_ancestor["value"] = ancestorcount
            ancestorcount = 0
            meal_ancestor["children"] = meal_parent_list.copy()
            meal_ancestor_list.append(meal_ancestor.copy())
            meal_parent_list.clear()
            ancestor_id = ancestor_id + 1
            ancestor_front = parent_id

    meal_parent["name"] = parent[parent_id]
    meal_parent["value"] = count[parent_id]
    meal_parent["children"] = meal_children_list.copy()
    meal_parent_list.append(meal_parent.copy())
    meal_ancestor["name"] = ancestor[ancestor_id]
    for z in range(ancestor_front, parent_id + 1):
        ancestorcount += count[z]
    meal_ancestor["value"] = ancestorcount
    meal_ancestor["children"] = meal_parent_list.copy()
    meal_ancestor_list.append(meal_ancestor.copy())
    meal_parent_list.clear()

    with open("MealSun_en.json", "w", encoding="utf-8") as js:
        json.dump(meal_ancestor_list, js, ensure_ascii=False)


def Excel2_zhjson(xlsx_file):
    parent = ["水、野生菜类", "花类", "竹笋类", "姜葱蒜", "腌盐、菌类", "辣椒类",
              "根茎豆类", "瓜类", "叶菜类",
              "加工豆制品", "加工乳制品", "杂果类", "柑橘类", "热带杂果类",
              "桃李枣类", "瓜果类", "梨类",
              "苹果类", "禽蛋类", "羊肉类", "鸡鸭鹅肉类", "牛肉类", "猪肉类", "海鲜类", "冻货类",
              "冰鲜类", "干货类", "淡水活鲜类", "南北干货", "五谷杂粮"]
    ancestor = ["蔬菜类", "加工食品", "新鲜水果", "肉类蛋类", "水产大类",
                "粮油副食"]
    meal_parent, meal_ancestor = {}, {}  # 父类，祖先类对象
    meal_ancestor_list = []  # 祖先类列表
    meal_parent_list = []  # 父类列表
    meal = {}  # 品种对象
    meal_children_list = []  # 子类品种列表

    excel_file = xlrd.open_workbook(xlsx_file)
    sheet1 = excel_file.sheets()[0]
    n_rows = sheet1.nrows

    count = [0]  # 父类数量列表
    ancestorcount = 0  # 祖先类数量
    parent_id = 0  # 父类索引
    ancestor_id = 0  # 祖先类索引
    ancestor_front = 0  # 用于祖先类数量求和
    for row in range(1, n_rows):
        values = sheet1.row_values(row)
        if (values[-5] != parent_id + 1):
            meal_parent["name"] = parent[parent_id]
            meal_parent["value"] = count[parent_id]
            meal_parent["children"] = meal_children_list.copy()
            meal_parent_list.append(meal_parent.copy())
            meal_children_list.clear()
            count.append(0)
            parent_id = parent_id + 1
        zh_name = values[3]
        en_name = values[6]
        meal["name"] = zh_name
        meal["en_name"] = en_name
        meal["value"] = 1
        meal_children_list.append(meal.copy())
        count[parent_id] = count[parent_id] + 1
        if (values[-1] != ancestor_id + 1):
            meal_ancestor["name"] = ancestor[ancestor_id]
            for z in range(ancestor_front, parent_id):
                ancestorcount += count[z]
            meal_ancestor["value"] = ancestorcount
            ancestorcount = 0
            meal_ancestor["children"] = meal_parent_list.copy()
            meal_ancestor_list.append(meal_ancestor.copy())
            meal_parent_list.clear()
            ancestor_id = ancestor_id + 1
            ancestor_front = parent_id

    meal_parent["name"] = parent[parent_id]
    meal_parent["value"] = count[parent_id]
    meal_parent["children"] = meal_children_list.copy()
    meal_parent_list.append(meal_parent.copy())
    meal_ancestor["name"] = ancestor[ancestor_id]
    for z in range(ancestor_front, parent_id + 1):
        ancestorcount += count[z]
    meal_ancestor["value"] = ancestorcount
    meal_ancestor["children"] = meal_parent_list.copy()
    meal_ancestor_list.append(meal_ancestor.copy())
    meal_parent_list.clear()

    with open("MealSun_zh.json", "w", encoding="utf-8") as js:
        json.dump(meal_ancestor_list, js, ensure_ascii=False)


def sunburst_official(json_file) -> Sunburst:
    f = open(json_file,'r',encoding='utf-8')
    j = json.load(f)

    c = (
        Sunburst(init_opts=opts.InitOpts(width="4000px", height="2400px"))
        .add(
            "",
            data_pair=j,
            highlight_policy="ancestor",
            radius=[0, "95%"],
            sort_="null",
            levels=[
                {},
                {
                    "r0": "5%",
                    "r": "35%",
                    "itemStyle": {"borderWidth": 2},
                    "label": {"fontSize":35},
                },
                {"r0": "35%", "r": "70%", "label": {"align": "right","fontSize":32}},
                {
                    "r0": "70%",
                    "r": "72%",
                    "label": { "position": "outside","silent": False,"fontSize":10},
                    "itemStyle": {"borderWidth": 3},
                },
            ],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-meal80K"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c


if __name__ == '__main__':

    xlsx_file = './Meal80K.xlsx'
    MealSun_zh = "./MealSun_zh.json"
    MealSun_en = "./MealSun_en.json"
    Excel2_enjson(xlsx_file)
    Excel2_zhjson(xlsx_file)
    bar_en = sunburst_official(MealSun_en)
    bar_zh = sunburst_official(MealSun_zh)
    bar_en.render('en_meal.html')
    bar_zh.render('zh_meal.html')






