[![PyPI](https://img.shields.io/badge/Python-All-blue.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-All-orange.svg)]()

# FileMonitor
代码审计辅助工具（文件监控）

# 使用：

### 环境：
MacOS 10.14  Python2/3环境运行通过

windows 7 Python2.7环境运行通过

如有问题或修改意见 请点击===>[问题反馈](https://github.com/TheKingOfDuck/FileMonitor/issues)

### 依赖：


> [watchdog](https://pypi.org/project/watchdog/)

可执行以下命令尝试安装

```
pip install watchdog
easy_install watchdog
```

### 运行：

```
git clone https://github.com/TheKingOfDuck/FileMonitor.git
cd FileMonitor
python fileMonitor.py
```

# 功能

* 排除不需要监控的文件目录(如测试基于thinkphp开发的CMS时可排除runtime目录)

* 显示/不显示目录变化(程序运行过程中读写变化很快 根据自身需求决定是否需要显示目录变化)

![screenshot](https://github.com/TheKingOfDuck/FileMonitor/blob/master/screenshot.png)

### 应用场景：

* https://xz.aliyun.com/t/3767
* https://xz.aliyun.com/t/3788
        


## 注意：所输入的路径均为绝对路径。


