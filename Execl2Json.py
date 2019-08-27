import json
from collections import defaultdict
import xlrd

parent = ["Water, wild vegetables", "Flower", "Bamboo shoots", "Onion, ginger, garlic", "Pickled salt, fungi", "Chili",
          "Rhizome beans", "Melon", "Leafy vegetables",
          "Processed soy products", "Processing dairy products", "Fruit", "Citrus", "Tropical fruit",
          "Peach and plum jujube", "Melon and fruit", "Pear",
          "Apple", "Eggs", "Mutton", "Chicken, duck, goose", "Beef", "Pork", "Seafood", "Frozen goods",
          "Chilled", "Dry goods", "Freshwater live fresh", "North and South dry goods", "Whole grains"]
ancestor = ["Vegetables", "Manufactured food", "Fresh fruits", "Meat & eggs", "Aquatic species",
            "Grain & oil non-staple food"]

meal_json = defaultdict(dict)
meal_parent, meal_ancestor = {}, {}

for i, val in enumerate(parent):
    meal_parent[i + 1] = val

for i, val in enumerate(ancestor):
    meal_ancestor[i + 1] = val

meal_json["parent_id"] = meal_parent
meal_json["ancestor_id"] = meal_ancestor

excel_file = xlrd.open_workbook("./meal1.xlsx")
sheet1 = excel_file.sheets()[1]
n_rows = sheet1.nrows
for row in range(1, n_rows):
    values = sheet1.row_values(row)
    meal_type = values[1]
    id = int(values[0])
    zh_name = values[3]
    en_name = values[6]
    nums = int(values[2])
    parent_id = int(values[-5])
    ancestor_id = int(values[-1])
    meal_json[meal_type]["id"] = id
    meal_json[meal_type]["zh_name"] = zh_name
    meal_json[meal_type]["en_name"] = en_name
    meal_json[meal_type]["nums"] = nums
    meal_json[meal_type]["parent_id"] = parent_id
    meal_json[meal_type]["ancestor_id"] = ancestor_id

with open("Meal2.json", "w", encoding="utf-8") as js:
    json.dump(meal_json, js, ensure_ascii=False)
