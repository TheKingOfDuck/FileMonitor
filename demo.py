# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mian
   Description :
   Author :       CoolCat
   date：          2019/5/11
-------------------------------------------------
   Change Activity:
                   2019/5/11:
-------------------------------------------------
"""
__author__ = 'CoolCat'

import os
import hashlib
import time


def monitor(dir):
    fileDirs = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            fileDirs.append(os.path.join(root, name))

    return fileDirs
        # for name in dirs:
        #     print(os.path.join(root, name))



def calcMD5(filepath):
    try:
        with open(filepath, 'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            hash = md5obj.hexdigest()
            # print(hash)
            return "修改了" + filepath + " Hash为：" + hash
    except:
        pass

def help():
    print(""" 
    _____________
   < FileMonitor >
    -------------
      /\_)o<
     |       | 
     | O . O |
      \_____/
    By CoolCat
      """)


if __name__ == '__main__':

    help()

    try:
        dir = str(raw_input(time.strftime('[%H:%M:%S]:') + "Please enter a directory:"))
    except:
        dir = str(input(time.strftime('[%H:%M:%S]:') + "Please enter a directory:"))
        pass
    #
    # dir = "../Aliyun/"

    print(time.strftime('[%H:%M:%S]:') + "FileMonitor is running...")

    # print(dir)

    a = monitor(dir)

    while True:
        #print(len(a))
        b = monitor(dir)
        #print(len(b))
        if a > b:
            c = list(set(b).difference(set(a)))
            try:
                print(time.strftime('[%H:%M:%S]:') + "新建了" + str(c[-1]))
            except:
                pass
        elif b > a:
            c = list(set(a).difference(set(b)))
            try:
                print(time.strftime('[%H:%M:%S]:') + "删除了" + str(c[-1]))
            except:
                pass
        elif len(a) == len(b):
            aList = []
            for pathName in a:
                hash = calcMD5(pathName)
                aList.append(hash)

            #print(aList)

            bList = []
            for pathName in b:
                hash = calcMD5(pathName)
                bList.append(hash)
            #print(bList)
            a = b

            cList = list(set(aList).difference(set(bList)))
            if len(cList) != 0:
                try:
                    print(time.strftime('[%H:%M:%S]:') + cList[-1])
                except:
                    pass
                a = b
            else:
                pass
            a = b
        else:
            pass
        a = b
        #break


