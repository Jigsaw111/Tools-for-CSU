# Tools-for-CSU

该项目旨在逐步完成一个可以方便日常学习生活的脚本库。

现有项目：

* 文件批量重命名工具
* 近代史在线听课代刷程序

## 批量重命名工具

使用该工具前应先准备好学生的姓名与学号，并以json的数据格式存储在本地。

json文件样例：

```json
{
    "学生1": "39011606**",
    "学生2": "39011606**"
}
```

根据程序提示输入指定的命名格式，以`dd`代表学生学号，以`ss`代表学生的姓名。

系统在搜索匹配的信息时只按照学生姓名进行正则，若需要按照学号匹配请修改json中的键值。

最后指定批量修改路径即可完成文件名的批量扫描修改，文件名的修改不包含子文件和子文件夹。

**运行环境 python3**

## 近代史在线听课代刷程序

在使用软件之前请先登录在线听课系统

程序运行后打开需要代刷的听课页面，通过网络数据抓包填入cookies数据。

在网页上点击视频进行播放，在其开始稳定播放后暂停播放，将其暂停时发出的网络请求地址填入脚本内。

回车后等待系统确认，当出现包含`true`的返回信息时即说明该视频的代刷已完成。

**运行环境 python3以及相关插件**
