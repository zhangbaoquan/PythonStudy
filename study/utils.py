import os

""" 
ADB 工具类
"""


# 判断当前字符串是否为空
def isEmpty(s):
    if str(s).isspace() or len(str(s)) <= 0:
        return 0
    else:
        return 1

class ADBUtils:
    def __init__(self, packageName, pagePath):
        self.packageName = packageName
        self.pagePath = pagePath

    # 打开应用
    def openApp(self):
        openAppCommand = " adb shell am start " + self.packageName + self.pagePath
        os.system(openAppCommand)

    # 关闭应用
    def closeApp(self):
        closeAppCommand = " adb shell am force-stop " + self.packageName
        os.system(closeAppCommand)

    # 计算手机的分辨率，然后返回一个包含宽度和高度的列表
    def calculatScreenSize(self):
        # 获取设备分辨率的原始数据
        result = os.popen("adb shell wm size").read()
        print("设备分辨率："+result)
        if isEmpty(result) == 0:
            # 这里设置了一个默认值，防止分辨率获取失败
            result = "1080x1920"
        value = result.split("x")
        width = str(value[0])
        high = str(value[1])
        print("heigh：" + high)
        if width.find(':') != -1:
            # 过滤width值之前的所有数据
            width = str(width.split(':')[1]).lstrip()
            print("width：" + width)
        size = [width, high]
        return size








