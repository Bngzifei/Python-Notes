"""
Python中导入模块时，实际上会把被导入的模块执行一遍，如下：
先看被调用的模块test.py：





那怎么才能只是单纯调用而不执行被调用模块的代码呢？要想被调用模块代码不被执行，前提得知道变量__name__是什么意思，
简单来说就是，如果不涉及模块导入的话，__name__的值就是” __main__“，
如果当此模块被导入引用的话，那么这个模块内的__name__值就是文件的名字（不带.py），如下test_1.py：




上边所说要是弄懂的话，那我们在被调用的模块中，可执行的代码前加上这么一句判断，if __name__ == '__main__':，
被调用的模块的代码就不会被执行了！




接下来才是正题
以下参考自Joy_Shen的一个回答。
先大概了解一下python基本运行机制。Python程序运行时不需要编译成二进制代码，而是直接从源码运行程序，简单来说就是，
Python解释器将源码转换为字节码，然后再由解释器来执行这些字节码。

解释器的具体工作：
1、完成模块的加载和链接；
2、将源代码编译为PyCodeObject对象(即字节码)，写入内存中，供CPU读取；
3、从内存中读取并执行，结束后将PyCodeObject写回硬盘当中，也就是复制到.pyc或.pyo文件中，以保存当前目录下所有脚本的字节码文件。

之后若再次执行该脚本，它先检查【本地是否有上述字节码文件】和【该字节码文件的修改时间是否在其源文件(就是.py源码)之后】，是就直接执行，
否则重复上述步骤。

那有的小伙伴就有疑问了，__pycache__文件夹的意义何在呢？
因为第一次执行代码的时候，Python解释器已经把编译的字节码放在__pycache__文件夹中，这样以后再次运行的话，如果被调用的模块未发生改变，
那就直接跳过编译这一步，直接去__pycache__文件夹中去运行相关的 *.pyc 文件，大大缩短了项目运行前的准备时间。


"""