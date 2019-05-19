


import os



class DeviceUtils:

    packageName = "com.chaozh.iReader"
    pagePath = "/com.chaozh.iReader.ui.activity.WelcomeActivity"
    openAppCommand = " adb shell am start " + packageName + pagePath
    """ 创建一个工具类 """
    def calculate(self):
        # 打开手机应用
        os.system(self.openAppCommand)
        # 获取手机屏幕的大小
        size_str = os.popen("adb shell wm size").read()
        return size_str


if __name__=='__main__':
    print('哈喽 python')
    device = DeviceUtils()
    print("手机分辨率 ： "+device.calculate())