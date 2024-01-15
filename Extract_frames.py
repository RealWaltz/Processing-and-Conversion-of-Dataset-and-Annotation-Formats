import os
import cv2

def extract_frames(video_folder, output_dir):
    # 遍历视频文件夹中的所有文件
    for filename in os.listdir(video_folder):
        # 获取文件的完整路径
        video_path = os.path.join(video_folder, filename)
        # 判断文件是否为视频文件
        if not os.path.isfile(video_path) or not filename.endswith(".mp4"):
            continue

        # 获取视频文件名（不包括扩展名）
        video_name = os.path.splitext(filename)[0]

        # 加载视频
        video = cv2.VideoCapture(video_path)
        success, frame = video.read()
        count = 1

        while success:
            # 生成帧图像文件名
            frame_name = f"{output_dir}/{video_name}_{count}.jpg"
            # 保存帧图像
            cv2.imwrite(frame_name, frame)

            # 读取下一帧
            success, frame = video.read()
            count += 1

        # 释放视频对象
        video.release()

# 调用函数进行帧提取
video_path = "D:/Files/DataSet/pallet"  # 输入视频文件路径
output_dir = "D:/Files/DataSet/pallet_frame"     # 输出帧图像保存路径
extract_frames(video_path, output_dir)

