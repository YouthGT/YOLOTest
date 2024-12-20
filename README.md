# YOLOv8-model-Test

## 实验数据集
DIOR_YOLO:“DIOR”是一个用于光学遥感图像目标检测的大规模基准数据集。数据集包含23463个图像和192472个实例，涵盖20个对象类。
这20个对象类是飞机、机场、棒球场、篮球场、桥梁、烟囱、水坝、高速公路服务区、高速公路收费站、港口、高尔夫球场、地面田径场、天桥、船舶、体育场、储罐、网球场、火车站、车辆和风磨

## 修改目录
back_end/start_train.py
>将代码放入 if __name__ == '__main__': 保护块中，确保只有在主程序启动时才会执行训练过程。
### 新加数据集配置
back_end/ultralytics/cfg/datasets/datasets.yaml 
```
path: ../datasets/  # dataset root dir
train: images/train  # train images
val: images/val  # val images
test:  # test images (optional)

# 类别数量
nc: 20  # 这里是20个类

# 类别名称 飞机、机场、棒球场、篮球场、桥梁、烟囱、水坝、高速公路服务区、高速公路收费站、港口、高尔夫球场、地面田径场、天桥、船舶、体育场、储罐、网球场、火车站、车辆、风磨
names:
  0: 'plane'
  1: 'airport'
  2: 'baseball-field'
  3: 'basketball-court'
  4: 'bridge'
  5: 'chimney'
  6: 'dam'
  7: 'highway service area'
  8: 'highway toll-gate'
  9: 'port'
  10: 'golf course'
  11: 'Surface track and field'
  12: 'platform bridge'
  13: 'ship'
  14: 'stadium'
  15: 'storage tank'
  16: 'tennis court'
  17: 'railway station'
  18: 'vehicle'
  19: 'windmill'
```
### 修改默认训练配置
back_end/back_end/ultralytics/cfg/default.yaml
```
line12: batch: 4  # (int) number of images per batch (-1 for AutoBatch) 
line17: device: 0  # (int | str | list, optional) device to run on, i.e. cuda device=0 or device=0,1,2,3 or device=cpu
```
## 现有问题
训练报错显示缺失图片(偶发事件🤷‍♂️)








