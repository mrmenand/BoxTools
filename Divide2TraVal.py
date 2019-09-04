import os
import shutil

meal80k_root = '/home/guangyixiao/mr_menand/Datasets/Meal80K/'

all_data = os.path.join(meal80k_root,'all_data')
train_data = os.path.join(meal80k_root,'train')
val_data = os.path.join(meal80k_root,'val')
if os.path.exists(train_data) and os.path.exists(val_data):
    shutil.rmtree(val_data)
    shutil.rmtree(train_data)
    os.mkdir(train_data)
    os.mkdir(val_data)

FILTER = ['other','other_weiKaiDai','weiKaiDai']
all_meal_type = os.listdir(all_data)
if FILTER[0] in all_meal_type:
    all_meal_type = list(set(all_meal_type) ^ set(FILTER))

for  meal_type  in all_meal_type:
    path_meal_type = os.path.join(all_data,meal_type)
    path_train_meal = os.path.join(train_data,meal_type)
    path_val_meal = os.path.join(val_data,meal_type)

    list_meal_type = os.listdir(path_meal_type)
    nums = len(list_meal_type)
    if nums >= 10:
        os.mkdir(path_train_meal)
        os.mkdir(path_val_meal)
        print(f'Meal80K_Type : {meal_type}')
        if nums > 250:
            for idx,pic in enumerate(list_meal_type,1):
                path_meal_pic = os.path.join(path_meal_type, pic)
                if idx < 51:
                    shutil.copy(path_meal_pic,path_val_meal)
                else:
                    shutil.copy(path_meal_pic,path_train_meal)

        else:
            for idx, pic in enumerate(list_meal_type, 1):
                path_meal_pic = os.path.join(path_meal_type, pic)
                if idx < nums*0.15:
                    shutil.copy(path_meal_pic, path_val_meal)
                else:
                    shutil.copy(path_meal_pic, path_train_meal)




