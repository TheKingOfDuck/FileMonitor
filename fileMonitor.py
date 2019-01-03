# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fileMonitor
   Description :
   Author :       CoolCat
   date：          2019/1/3
-------------------------------------------------
   Change Activity:
                   2019/1/3:
-------------------------------------------------
"""
__author__ = 'CoolCat'

from watchdog.observers import Observer
from watchdog.events import *
import time

global doWithout
global showDir


class FileEventHandler(FileSystemEventHandler):


    def __init__(self):
        FileSystemEventHandler.__init__(self)


    def on_moved(self, event):

        ###  文件移动显示青色
        if doWithout in event.src_path:
            pass
        elif event.is_directory and showDir == "y":
            print(time.strftime('[%H:%M:%S]:') + "\033[0;36m%s\033[0m" % "directory moved from {0} to {1}".format(event.src_path,event.dest_path))
            pass
        elif event.is_directory == False:
            print(time.strftime('[%H:%M:%S]:') + "\033[0;36m%s\033[0m" % "file moved from {0} to {1}".format(event.src_path,event.dest_path))

    def on_created(self, event):

        ###  文件创建显示绿色

        if doWithout in event.src_path:
            pass
        elif event.is_directory and showDir == "y":
            print(time.strftime('[%H:%M:%S]:') + "\033[5;32m%s\033[0m" % "directory created:{0}".format(event.src_path))
            pass
        elif event.is_directory == False:
            print(time.strftime('[%H:%M:%S]:') + "\033[5;32m%s\033[0m" % "file created:{0}".format(event.src_path))

    def on_deleted(self, event):

        ###  文件删除显示红色
        if doWithout in event.src_path:
            pass
        elif event.is_directory and showDir == "y":
            print(time.strftime('[%H:%M:%S]:') + "\033[0;31m%s\033[0m" % "directory deleted:{0}".format(event.src_path))
            pass
        elif event.is_directory == False:
            print(time.strftime('[%H:%M:%S]:') + "\033[0;31m%s\033[0m" % "file deleted:{0}".format(event.src_path))

    def on_modified(self, event):

        ###  文件修改显示蓝色
        if doWithout in event.src_path:
            pass
        elif event.is_directory and showDir == "y":
            print(time.strftime('[%H:%M:%S]:') + "\033[0;34m%s\033[0m" % "directory modified:{0}".format(event.src_path))
            pass
        elif event.is_directory == False:
            print(time.strftime('[%H:%M:%S]:') + "\033[0;34m%s\033[0m" % "file modified:{0}".format(event.src_path))


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

if __name__ == "__main__":
    help()

    import sys
    if sys.version_info.major == 2:
        try:
            monitorDir = raw_input(time.strftime('[%H:%M:%S]:') + "Please enter a directory:")
            doWithout = raw_input(time.strftime('[%H:%M:%S]:') + "Unnecessary directory:")
            showDir = raw_input(time.strftime('[%H:%M:%S]:') + "Display directory changes(y or n):")
        except:
            pass
    else:
        monitorDir = input(time.strftime('[%H:%M:%S]:') + "Please enter a directory:")
        doWithout = input(time.strftime('[%H:%M:%S]:') + "Unnecessary directory:")
        showDir = input(time.strftime('[%H:%M:%S]:') + "Display directory changes(y or n):")

    print(time.strftime('[%H:%M:%S]:') + "\033[0;31m%s\033[0m" % "FileMonitor is running...")

    # # monitorDir = "/Users/CoolCat/php"
    # print(type(monitorDir))


    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler,monitorDir,True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


