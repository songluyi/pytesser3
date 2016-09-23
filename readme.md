#pytesser3 使用说明

##需要环境
1. Python3.x以上

2. 需要安装PIL以及tesseract-ocr引擎。[点我下载tesseract-ocr引擎](http://101.96.10.43/internode.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe)

##如何使用

1. 下载pytesser3 解压后，放置在你的lib/site-packages 目录下

2. 修改__init__.py里面第十二行tesseract_exe_name为你tesseract-ocr安装路径，我填写的就是tesseract-ocr默认安装的，如果
你也是默认安装路径，那么请忽略本步骤，即可直接运行

##如何测试轮子是否好用

1. 你可以运行目录下的code.py 运行一下即可检验轮子是否成功。

如图：

![](http://www.songluyi.com/wp-content/uploads/2016/09/QQ图片20160923100109.png)


##其他注意事项

1. 为什么你的pytesser3下面有tesseract.exe为啥我还需要加载新引擎
**答：因为原来轮子很傻比，你只能安装一下tesseract-ocr引擎，把路径修改了**

2. 如果我需要识别中文，我该如何做呢？
**答：这是tesseract-ocr的事情 下载他的中文支持包，然后放置在其tessdata目录下，祝你好运~**

3. 为啥这个轮子不可以pip install
**答：原来作者就不行==，以后再说吧**

