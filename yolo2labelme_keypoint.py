import os
import json
from PIL import Image


# def get_image_dimensions(image_folder):
#     image_path = os.path.join(image_folder, "VID_1_1.jpg")  # 假设图像文件名为VID_1_1.jpg
#     image = Image.open(image_path)
#     image_width, image_height = image.size
#     return image_width, image_height


def yolo_to_labelme( txt_folder, save_folder):
    # image_width, image_height = get_image_dimensions(image_folder)
    image_width = 720  # 图片宽度
    image_height = 1280  # 图片高度

    txt_files = os.listdir(txt_folder)
    for txt_file in txt_files:
        if not txt_file.endswith(".txt"):
            continue

        txt_path = os.path.join(txt_folder, txt_file)
        save_path = os.path.join(save_folder, os.path.splitext(txt_file)[0] + ".json")

        with open(txt_path, 'r') as f:
            lines = f.readlines()

        labelme_data = {
            "version": "5.4.0.post1",
            "flags": {},
            "shapes": [],
            "imagePath": os.path.join("..\\original_images\\"+os.path.splitext(txt_file)[0] + ".jpg"),  # 图片路径
            "imageData": None,  # 图片数据（base64编码）
            "imageHeight": image_height,  # 图片高度
            "imageWidth": image_width  # 图片宽度
        }

        for line in lines:
            line = line.strip().split()
            bbox_class_id = int(line[0])
            bbox_center_x_norm = float(line[1])
            bbox_center_y_norm = float(line[2])
            bbox_width_norm = float(line[3])
            bbox_height_norm = float(line[4])

            bbox_top_left_x = int((bbox_center_x_norm - bbox_width_norm / 2) * image_width)
            bbox_top_left_y = int((bbox_center_y_norm - bbox_height_norm / 2) * image_height)
            bbox_bottom_right_x = int((bbox_center_x_norm + bbox_width_norm / 2) * image_width)
            bbox_bottom_right_y = int((bbox_center_y_norm + bbox_height_norm / 2) * image_height)

            shape = {
                "label": "pallet",  # 类别名称
                "points": [[bbox_top_left_x, bbox_top_left_y], [bbox_bottom_right_x, bbox_bottom_right_y]],  # 框的坐标
                "group_id": None,
                "description": None,
                "shape_type": "rectangle",
                "flags": {},
                "mask": None
            }
            labelme_data["shapes"].append(shape)

            # 添加关键点信息
            keypoints = line[5:]
            for i in range(8):
                keypoint_x_norm = float(keypoints[i * 3])
                keypoint_y_norm = float(keypoints[i * 3 + 1])

                keypoint_x = int(keypoint_x_norm * image_width)
                keypoint_y = int(keypoint_y_norm * image_height)

                keypoint_label = "left_" + str(i + 1) if i < 4 else "right_" + str(i - 3)

                keypoint = {
                    "label": keypoint_label,
                    "points": [[keypoint_x, keypoint_y]],
                    "group_id": None,
                    "description": "",
                    "shape_type": "point",
                    "flags": {},
                    "mask": None
                }

                labelme_data["shapes"].append(keypoint)



        with open(save_path, "w") as f:
            json.dump(labelme_data, f, indent=4)


# 使用示例
# image_folder = "path/to/image/folder"  # 图像文件夹路径
txt_folder = "D:/Files/DataSet/Pallet/Round1/labels_yolo"  # 包含txt文件的文件夹路径
save_folder = "D:/Files/DataSet/Pallet/Round1/labels_json"  # 保存JSON文件的文件夹路径

yolo_to_labelme(txt_folder, save_folder)