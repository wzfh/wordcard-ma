import requests
from urllib.parse import urlsplit

# 读取包含多个地址的文件
with open(r'C:\Users\Administrator\Desktop\新建文本文档.txt', 'r',encoding='utf-8', errors='ignore') as file:
    urls = file.readlines()
    # print(urls[1].replace('\n', '').strip())


# # 遍历每个URL
for url in urls:
    # 去除URL两端的空白字符
    url = url.replace('\n', '').strip()
    print(url)
#
#     # 检查URL是否有效
#     if not urlsplit(url).scheme:
#         print(f"无效的URL: {url}")
#         continue
# url="http://10.181.7.68:7405/dc/openapi/getPersonnelIntegrityFileInformation?CXZGZH=440902199409203714&XM=朱康林"
#     # 发送HTTP请求
    try:
        response = requests.get(url, timeout=5)
        #
        #     # 检查HTTP响应状态码
        print(response.text)
    except:
        print(f"请求超时：{url}")
        continue