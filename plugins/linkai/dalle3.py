import requests
import json

# 设置Azure DALL-E-3的API地址和密钥
api_url = "https://api.example.com/dalle3"
api_key = "your_api_key"

# 设置输入文本和生成图像的触发词
input_text = ""
trigger_word = "画"

while True:
    # 接收用户输入的文本
    user_input = input("请输入文本：")

    # 判断用户输入是否以触发词开头
    if user_input.startswith(trigger_word):
        # 提取输入文本（去除触发词）
        input_text = user_input[len(trigger_word):].strip()
        print("输入文本：", input_text)

        # 构建请求的payload
        payload = {
            "text": input_text
        }

        # 发送POST请求给Azure DALL-E-3 API
        response = requests.post(api_url, headers={"Authorization": api_key}, json=payload)

        # 解析API的响应
        if response.status_code == 200:
            result = json.loads(response.text)
            generated_image_url = result["image_url"]
            print("生成的图像URL：", generated_image_url)
        else:
            print("错误：", response.text)
    else:
        print("请输入以触发词开头的文本")
