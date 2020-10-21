#coding=utf-8
"""
@project : python_work
@author  : zhangbaoquan
#@file   : net.py.py
#@ide    : PyCharm
#@time   : 2020-10-21 23:11:10
@desc    : 网络的使用

{
  "total_count": 6078781,
  "incomplete_results": false,
  "items": [
    {
      "id": 83222441,
      "node_id": "MDEwOlJlcG9zaXRvcnk4MzIyMjQ0MQ==",
      "name": "system-design-primer",
      "full_name": "donnemartin/system-design-primer",
      "private": false,
"""

import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)

# 将相应存储在,这里存储的是一个json
response = r.json()
# 解析json数据,这里是存储里面的仓库信息
items = response['items']
# 输出仓库信息的长度
print(len(items))

# 输出第一个仓库信息
p0 = items[0]
# print(p0)
print(len(p0))
# 打印所有的键
for key in p0.keys():
    print(key)