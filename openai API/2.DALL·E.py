# 代码说明：
# 1.本代码使用OpenAI的API来生成DALL·E 3模型的图像。
# 2.需要先注册OpenAI的API密钥，并在代码中替换为自己的密钥。
# 3.生成的图像保存在当前目录下的generated_image.png文件中。


from openai import OpenAI
import requests
import time
import os

# 初始化客户端
client = OpenAI(
    # 请替换为你的API密钥
    api_key="sk-8H4ypTvnDgST3uNypFS3XYmmo57VOfnjGFW2pqjcG2dtLwVS",
    # 使用便携AI聚合API的入口地址
    base_url="https://api.bianxie.ai/v1"
)

# 定义一个函数来下载图片
def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Image saved as {file_name}")
    else:
        print("Failed to download the image")

# 创建DALL·E 3图像生成请求
response = client.images.generate(
    model="dall-e-3",  # 指定使用的DALL·E 3模型
    prompt="请帮我制作一个网站logo，六边形，黑底白字，字为艺术字体M，需要整体看起来很有艺术设计感，M这个字需要让人一眼就能看出是字母M，但同时还要有艺术感，在很小的图标上也能看清楚，不需要额外的背景色之类的东西"
    ,
    n=1,  # 生成一张图像
    size="1024x1024"  # 图像大小
)

# 获取并保存生成的图像
image_url = response.data[0].url
print(response.data)
# download_image(image_url, "generated_image.png")
timestamp = time.strftime("%Y%m%d_%H%M%S")  # 获取当前时间戳
file_path = fr"C:\Users\JA085914\Desktop\PY\AI画图\generated_image_{timestamp}.png"  # 设置保存路径和文件名
download_image(image_url, file_path)  # 下载图片