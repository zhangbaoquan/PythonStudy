
from study.utils import *

if __name__== '__main__':
    packageName = "com.chaozh.iReader"
    pagePath = "/com.chaozh.iReader.ui.activity.WelcomeActivity"

    adb = ADBUtils(packageName, pagePath)
    adb.openApp()


    # screenValue = screenSize.split("x")
    # print(screenValue)
    # width = screenValue[0]
    # height = screenValue[1]
    # print("width : " +width)
    # print("width length : "+ str(len(width)))
    # print("height length : "+ str(len(height)))
    #
    # width2 = width.split(":")
    # width2Value = str(width2[1])
    # print(width2Value.lstrip())
    # print("********")
    # print(str(screenValue[1]))

    size = adb.calculatScreenSize()
    print(size)
    width = size[0]
    heigh = size[1]
    print("width : "+width)
    print("heigh : "+heigh)



