# 图片检测程序运行指南

## 远行环境准备

    1. 安装Python3
    2. 安装open-cv处理库

        pip3 opencv-contrib-python==3.4.5.20

## 运行方式

    1. 在应用的根目录下，执行以下命令：

        python3 run_test.py

## 测试数据及结果说明

    1. 结果说明：
        1. 控制台输出的为照片与基准照片的相似度
        2. 照片检测采用了两种不同的算法验证:
            Feature算法 — 值越大越相似。最小为0，最大为100（完全相同)
            Hash算法    - 值越小越相似。最小为0(完全相同)

    2. 测试数据说明：
        - data\base_image.jpg为基准照片
        - data\check_data\same.jpg -> 未做任何修改的照片
        - data\check_data\cut.jpg -> 做了剪切处理的照片
        - data\check_data\resize.jpg -> 调整尺寸的照片
        - data\check_data\gammar_adjust.jpg -> 调整了图像Gammar曲线的照片
        - data\check_data\other_x.jpg -> 其他不同的照片
