[![PyPI](https://img.shields.io/badge/Python-All-blue.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-All-orange.svg)]()

# FileMonitor
代码审计辅助工具（文件监控）

**优先使用fileMonitor.py 不推荐main.py 这三年前的玩意儿了 总体上都不推荐使用这种方式挖洞 建议看看IAST**

# 更新：


**感谢[moyuwa](https://github.com/moyuwa)反馈的Bug，如有问题或修改意见 请点击===>[问题反馈](https://github.com/TheKingOfDuck/FileMonitor/issues)**

upload to pypi
```
python setup.py sdist
twine upload dist/*
```

# 使用：

所有unix相关的系统可使用pip一键安装:

```
python3 -m pip install filemon==1.3 -i https://pypi.python.org/simple/
filemon -h
```

### 环境：
MacOS 10.14  Python2/3环境运行通过

windows 7 Python2.7环境运行通过

### 依赖：

> [watchdog](https://pypi.org/project/watchdog/)

### 运行：

```
git clone https://github.com/TheKingOfDuck/FileMonitor.git
cd FileMonitor
python fileMonitor.py
```

无需依赖版：

```
python main.py
```
(路径可为相对路径)

php版本：

```
php fileMonitor.php --dir ./
```


# 功能

* 排除不需要监控的文件目录(如测试基于thinkphp开发的CMS时可排除runtime目录)

* 显示/不显示目录变化(程序运行过程中读写变化很快 根据自身需求决定是否需要显示目录变化)

![screenshot](https://github.com/TheKingOfDuck/FileMonitor/blob/master/screenshot.png)

### 应用场景：

* https://xz.aliyun.com/t/3767
* https://xz.aliyun.com/t/3788
        


## 注意：所输入的路径均为绝对路径。


