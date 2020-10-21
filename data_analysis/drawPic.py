# coding=utf-8
"""
@project : python_work
@author  : zhangbaoquan
#@file   : drawPic.py
#@ide    : PyCharm
#@time   : 2020-10-21 08:25:51
@desc    :
matplotlib : 数学绘图库，方便绘制图表

"""

import matplotlib.pyplot as plt

# 绘制折线图
data = []
for a in range(1, 10):
    if a == 2 or a == 4:
        data.append(a * a)
    elif a == 3 or a == 5:
        data.append(a * a * a)
    else:
        data.append(a)
print(data)

plt.plot(data)

# 设置图表标题，并给x,y设置标签
plt.title('hello')
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square Value", fontsize=12)
# plt.show()
# 保存图片，默认保存在当前文件目录，替换show
plt.savefig('square_plot.png')
