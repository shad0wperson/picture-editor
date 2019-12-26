# --** coding="UTF-8" **--
# 
# author:SueMagic  time:2019-01-01
import os
import re
import sys

def rename():
    fileList = os.listdir(r"D:\ele-pic")
    # 输出此文件夹中包含的文件名称
    print("修改前：" + str(fileList)[1])
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(r"D:\ele-pic")
    # 名称变量
    num = 0
    # 遍历文件夹中所有文件
    for fileName in fileList:
        # 匹配文件名正则表达式
        pat = ".+\.(png)"
        # 进行匹配
        pattern = re.findall(pat, fileName)
        # 文件重新命名
        os.rename(fileName, (str(num + 1) + '.' + pattern[0]))
        # 改变编号，继续下一项
        num = num + 1
    print("***************************************")
    # 改回程序运行前的工作目录
    os.chdir(currentpath)
    # 刷新
    sys.stdin.flush()
    # 输出修改后文件夹中包含的文件名称
    print("修改后：" + str(os.listdir(r"D:\ele-pic")[1]))
    af_names = os.listdir(r"D:\ele-pic")
    for af_name in af_names:
        print(">>>>>>>正在写入文件名%s到文件图片目录下" % af_name)
        with open('pic-url.txt','a') as f:
            f.write("http://boontonelectronics.com/wp-content/uploads/2019/" + af_name +"\n")
            f.close()

    
if __name__ == "__main__":
    rename()
    

