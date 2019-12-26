#!/usr/bin/env python
#coding:utf8
#! python3
#批量修改一个文件下的文件后缀
import sys
import os
import random
def Rename():

    #Path = "F:\\test\\"  # windows下的文件目录
    #Path = input("请输入你需要操作的目录(格式如'F:\\test')：")
    Path = r"D:\ele-pic"
    filelist = os.listdir(Path)
    for files in filelist:
        Olddir = os.path.join(Path,files)
        print(files)  #打印出老的文件夹里的目录和文件
        if os.path.isdir(Olddir):  #判断是否是文件，是文件，跳过
            continue
        filename = os.path.splitext(files)[0]
        #filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(Path,filename + '.png')  #只要修改后缀名就可以更改成任意想要的格式
        #可以修改文件名为随机名称
        # Newdir = os.path.join(Path,str(random.randint(2000,5000))+'.png')
        os.rename(Olddir,Newdir)
        
        

if __name__ == "__main__":
    Rename()
    
