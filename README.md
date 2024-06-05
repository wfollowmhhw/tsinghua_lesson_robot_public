# 自动选课（定时选？）

## 说明

就是个自动选课脚本，没啥抢课竞争力，可以放置选课，以便1:00睡大觉

## 环境配置

### python

首先你需要一个python环境，我用的是python=3.9

然后，你需要这几个包： 
1. paddlepaddle（百度的人工智能模型）
2. seleium （调用浏览器的）

安装方法：
```bash

pip install paddlepaddle paddleocr
pip install seleium

```

### webdriver

运行seleium需要浏览器driver，我用的是firefox的driver ，所以你需要下载geckodriver


这是发布位置：需要翻墙
[最新版网址点这里](https://github.com/mozilla/geckodriver/releases)

不会翻墙的同学请稍等，我稍后传个清华云盘链接

请记得给driver配环境变量呦

## 配置说明

### setting.json

在这个配置文件里，你需要配置一下：
1. name （你的学号）
2. password （你的密码）
3. start_time （选课开始时间）
4. term （选课学期）

需要注意：
- 不要改变时间的格式。
- 学期1号是秋季，2号是春季，3号是夏季。比如2024年暑假是2023-2024-3

### lessons.csv

这个文件是你想选的课的表单。每一行有三个字段：
1. 课程号
2. 课序号
3. 选课类型

注意： 排的靠上的先选

目前我还没有实现换页寻找，所以可能会出现如思政实践的一大堆课一个课程号，导致无法选课。

## 运行
运行方法：
```bash

python __init__.py

```


