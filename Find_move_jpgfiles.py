import os
import shutil

# 原始文件夹路径
# json_folder = "D:/Files/DataSet/pallet_labels"
# jpg_folder = "D:/Files/DataSet/pallet_frame"
json_folder = "D:/Files/DataSet/Pallet/Round1/labels_yolo_problems"
jpg_folder = "D:/Files/DataSet/Pallet/pallet_frame"
# 目标文件夹路径
target_folder = "D:/Files/DataSet/Pallet/Round1/tmp_images"

# 遍历json文件夹中的文件
for json_file in os.listdir(json_folder):
    if json_file.endswith(".txt"):
        # 获取json文件名（不包含扩展名）
        json_name = os.path.splitext(json_file)[0]
        # 构造对应的jpg文件路径
        jpg_file = os.path.join(jpg_folder, json_name + ".jpg")

        # 检查jpg文件是否存在
        if os.path.exists(jpg_file):
            # 构造目标文件路径
            target_jpg = os.path.join(target_folder, json_name + ".jpg")
            # 剪切jpg文件到目标文件夹
            shutil.copyfile(jpg_file, target_jpg)
            # shutil.move(jpg_file, target_jpg)
            print(f"成功剪切 {json_file} 对应的jpg文件到目标文件夹")

        else:
            print(f"找不到 {json_file} 对应的jpg文件")
