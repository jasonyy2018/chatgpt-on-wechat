import requests
import json

# 设置Azure DALL-E-3的API地址和密钥
api_url = "https://wckjopenai1.openai.azure.com/"
api_key = "513fd1114aa24883aa47218ee0969ba7"

# 读取待生成图像的输入文本
input_text = "a cat sitting on a table"

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
    print("Generated image URL:", generated_image_url)
else:
    print("Error:", response.text)
