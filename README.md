# Processing-and-Conversion-of-Dataset-and-Annotation-Formats
## 代码主要内容：CV方向数据集及标注文件的处理
## 基本情况
python = 3.7, 要运行全部代码，需要cv2, PIL, tqdm, numpy, json, shutil等库。
### Extract_frames.py
- 将`.mp4`文件的每一帧抽取成`.jpg`文件
- 可以指定视频文件和图像文件的格式
- 可以修改`count`变量改变抽取帧的间隔
### Find_move_jpgfiles.py
- 用于找到对应于标注的图像文件
- 使用`shutil.copyfile`或者`shutil.move`来复制或剪切图像
- 可以自定义标注格式，如`.json`或`.txt`
### labelme2yolo_keypoint.py
- 用于将labelme软件生成的`.json`格式标注转换成YOLO格式的`.txt`标注, 针对关键点检测领域或目标检测领域
- 生成的YOLO格式关键点标签只有`0`或`2`，即不可见或可见两类
- 关键点检测标注需要框是平行于图像边界的矩形且非重合的，以便提取框中的关键点
### yolo2labelme_keypoint.py
- 用于将YOLO格式的`.txt`标注转换成`.json`格式, 针对关键点检测领域领域
- 代码最初目的是帮助实现半自动标注. 人工标注少量数据, 然后将推理得到的标注在labelme中进行微调(因此需要标注为`.json`格式)
### split_dataset.py
- 按照自己设定的比例分割数据，可分为数据集, 测试集, 验证集三部分
## 感谢
`labelme2yolo_keypoint.py`代码来自<https://github.com/TommyZihao/Label2Everything/tree/main/labelme2yolo-keypoint>
