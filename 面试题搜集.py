大的方向:

布隆过滤器:
设计模式:
数据结构与算法:
数据库调优:
redis:
mongodb:
多线程多进程协程:
消息队列:
RPC
领域驱动设计
敏捷开发
GDB
websocket
SSE(Server Sent Events)
Redis的 ORM  redisco Walrus
发布/订阅模式
asyncio框架,未来web开发不可能离开websocket等实时技术



谈谈装饰器，迭代器，yield，内存管理等

Python高并发解决方案

web安全相关，sql注入，xss

如何面试Python开发?
https://www.zhihu.com/question/33398583

面试经历:
https://segmentfault.com/a/1190000014540229

牛客网:
https://www.nowcoder.com/discuss/136491

核心: 扎实的基础和灵活的思维
公司 艾维邑动
http://avazuinc.com/home/

https://www.appannie.com/cn/
JD:工作描述 (job description)

剑指offer
牛客左神

Python之美专刊:
https://zhuanlan.zhihu.com/python-cn

sanic项目:
https://github.com/dongweiming/lyanna

python分支代码技巧:
https://zhuanlan.zhihu.com/p/35425907

详解Python元类:
https://zhuanlan.zhihu.com/p/30861351

算法题:
https://labuladong.gitbook.io/algo/

Python布隆过滤器:
https://www.cnblogs.com/yscl/p/12003359.html

https://my.oschina.net/u/4336234/blog/3441424

站酷:UI设计网站
https://www.zcool.com.cn/

debian教程:
https://www.debian.org/doc/manuals/debian-reference/ch01.zh-cn.html

网页转成PDF,搜集一下

一个完整的项目设计:
https://zhuanlan.zhihu.com/p/28672237

python web框架评测网站:
https://python-guide.readthedocs.io/en/latest/scenarios/web/

python web 应用性能调优:
https://tech.glowing.com/cn/python-web-performance-optimization/

用于替换requests的性能更好的库:
https://github.com/gwik/geventhttpclient

提的合并:
https://github.com/gwik/geventhttpclient/pull/85

opentracing, 完善分布式环境下的性能追踪

阅读开源项目代码:
https://zhuanlan.zhihu.com/p/22275595

新版的pypi站点:https://pypi.org/

开发中经常提及的Pr是什么意思？
PR是Pull Request缩写，Git/svn之类用的。比如GitHub上的项目，你pull下来，
修改了部分代码之后再提交PR，然后管理员觉得你改的代码没毛病，确认。这个项目某部分代码就改成你的了.

python web开发实战:
https://zhuanlan.zhihu.com/p/22371355

潘俊勇

https://python-modernize.readthedocs.io/en/latest/

PR模板指导:
https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository

BTW:顺便一提 (by the way)

代码质量保证:
https://zhuanlan.zhihu.com/p/22338225

Python 不能不知的模块:
https://zhuanlan.zhihu.com/p/22246193

golang erlang

terminus 打开本地终端: 快捷键  Ctrl + L

windows下python第三方的库集合:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

No module named '_curses'解决办法:
https://www.pianshen.com/article/9233675404/

windows下安装bpython:
https://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_python_006_bpython.html

按位取反运计算方法:
https://blog.csdn.net/xiexievv/article/details/8124108

学术科研互动平台:
http://muchong.com/t-11559382-1

golang公链学习资料:
https://blog.csdn.net/itcastcpp/article/details/86603408

Golang精编100题-搞定golang面试:
https://blog.csdn.net/itcastcpp/article/details/80462619?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.nonecase

截图神器:ShareX
https://github.com/ShareX/ShareX/releases/tag/v13.1.0

Python 文件操作常用函数:

1.> 等效于 rm * -rf 命令递归删除的:
import shutil
shutil.rmtree(路径)

2.> 等效于 mkdir -p 命令递归创建目录:

os.makedirs(dst)

3.> 等效于 cp -r src_path dst_path
import shutil
shutil.copytree(src, dst)

4. 注意: os.system(系统命令)
返回值为0 才是正常执行,否则就是执行失败

5. 这种就是程序退出,类似于 手动按下 ctrl + c 键:
import sys
sys.exit()

6.切换到指定目录:
os.chdir(指定路径)

7.获取当前所在路径:
os.getcwd()

仔细看下这个仓库:
https://github.com/jumper2014/PyCodeComplete

做成这个打包:
https://www.jianshu.com/p/692bab7f8e07

知乎专栏-Python实践之路:
https://zhuanlan.zhihu.com/python2018

知乎专栏-90 条写 Python 程序的建议:
https://zhuanlan.zhihu.com/p/144228839

这个网站需要挂代理才能访问:
https://itbook.download/

自定义编写的python脚本实现开机自启动。

增量爬虫，最主要的就是爬取的url的去重,所以需要持久化存储,那就使用mongodb存起来,
当再次爬取的时候,进行比对去重,实现增量爬取。

解决报错:[944:9704:0723/151739.208:ERROR:browser_switcher_service.cc(238)
https://blog.cnrainbird.com/index.php/2020/04/21/python_windows_xia_yun_xing_selenium_ti_shi_devtools_listening_on_ws_127_0_0_1/


Python中文网教程:
https://www.cnpython.com/tags/262753

mongodb基础操作:
https://blog.csdn.net/fengbingchun/article/details/89069165

mongodbmanager可视化连接器:还有一个robo3T
https://www.mongodbmanager.com/download-mongodb-manager-free


mongodb基础操作命令:
1、查询指定集合的所有记录：
	db.centos8_table.find() 或者 db.centos8_table.find({})
	查询关键字指定的记录:
	db.centos8_table.find({"kw":kw})
2、删除指定集合的所有记录：
如果你想删除所有数据，可以使用以下方式（类似常规 SQL 的 truncate 命令）：
	db.col.remove({})   注意:remove方法需要一个query参数,删除所有给{}即可
	删除关键字指定的记录:
	db.col.remove({"kw":kw})

https://www.runoob.com/mongodb/mongodb-remove.html

mongodb常用查询命令:
https://blog.csdn.net/liqi_q/article/details/79086238

github加载慢解决办法:
https://github.com/521xueweihan/GitHub520?utm_source=gold_browser_extension

脚本之家电子书:
https://www.jb51.net/do/book.html

git reset三种模式
https://www.jianshu.com/p/c2ec5f06cf1a

免费终端连接软件MobaXterm:
https://mobaxterm.mobatek.net/download-home-edition.html

在民企使用vdi办公的同事使用下面的登录方式：
IE浏览器或safari浏览器访问下面地址：
地址一：webagent.sangfor.net.cn/ssl/mqkjyvdc.php
地址二：webagent.sangfor.net/ssl/mqkjyvdc.php
账号密码为办公VDI（200.200.8.80）的账号密码（账号默认为工号，忘记密码的同事可以联系its重置）
收起

智齿客服开发文档:
http://www.sobot.com/developer/%E5%BC%80%E6%94%BE%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%8D%95%E7%B3%BB%E7%BB%9F/

app后端设计:
https://blog.csdn.net/newjueqi/article/details/19003775

iteye网站:
https://www.iteye.com/magazines/130

前端设计资源网站:
https://zhuanlan.zhihu.com/p/115949816

https://www.freesion.com/article/4140230558/

俄罗斯搜索引擎:
yandex浏览器

解决github访问慢的问题:
https://zhuanlan.zhihu.com/p/93436925
140.82.113.3	github.com
199.232.69.194	github.global.ssl.fastly.net

github无法加载图片:
https://blog.csdn.net/qq_38232598/article/details/91346392

go依赖包代理:
https://www.goproxy.io/zh/

golang 安装一个项目下的所有依赖:
https://blog.csdn.net/weixin_34319640/article/details/94330725

go依赖工具:
https://github.com/gpmgo/gopm

windows10搭建go语言开发环境:
https://www.cnblogs.com/jiangson/p/12022288.html

https://golang.google.cn/doc/install?download=go1.14.6.windows-amd64.msi

goland配置:
http://www.coder55.com/article/1233

go钱包项目:
https://github.com/mining-pool/not-only-mining-pool

https://www.cnblogs.com/zlslch/p/6860229.html

ubuntu中root账户的密码:911611

数据库导入导出操作:
https://www.cnblogs.com/withfeel/p/10796633.html

关于Python异常的最好的讲解:
https://blog.csdn.net/zong596568821xp/article/details/78180229?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-1-78180229.nonecase

redis服务设置为开机自启动:
https://www.cnblogs.com/songjilong/p/12580755.html

vim /etc/init.d/redis
就是创建一个redis的脚本,授权可执行,类似于windows中的.exe文件,开机自动执行.

设置后,重启命令:
/etc/init.d/redis restart 或者
service redis restart

mongodb设置开机自启动:
https://www.cnblogs.com/jifeng/p/7844201.html

celery设置开机自启动:
https://www.cnblogs.com/Ting-light/p/9948201.html
注意看报错::::自己进行授权操作.

【敌后武功团纪念文章】20140716 你不能不知道的iOS开发75种秘密武器:
https://zhuanlan.zhihu.com/p/19802486

SHA256:O4XUlL2xtLJN28j6yv2OjXikSDhhuC1IPBLd0EvA+ns

celery开机自启动配置及如何编写celery部分的app:
https://www.xz577.com/j/39845.html

https://pythonheidong.com/blog/article/182147/

区块链革命 PDF 高清版下载:
https://www.xz577.com/e/25265.html

硬链接与软链接:
https://blog.csdn.net/qq_28897525/article/details/80657465

git分支合并:
本地的分支合并的时候,一定是主分支去合并子分支, 比如 是 git checkout master,
切换到master分支,然后在master分支上面执行 git merge 1.0.0/feature/lb-fix-no-upload-bug,
就是master把 1.0.0/feature/lb-fix-no-upload-bug 分支合并了.


celery守护进程启动模式:
https://docs.celeryproject.org/en/latest/userguide/daemonizing.html
https://github.com/celery/celery/blob/master/extra/generic-init.d/celeryd

Django中支持restful风格的框架:
tastypie和DRF
http://tastypieapi.org/
https://django-tastypie.readthedocs.io/en/latest/
odoogithub地址:
https://github.com/odoo/odoo
关于odoo的话题:
https://www.zhihu.com/topic/19718907/newest
国内企业:华炎魔方
https://www.steedos.com/company/about-us/
苏州欧度:
http://oudu.me/
java web学习网站:
https://how2j.cn/
sanic框架介绍:	
https://github.com/howie6879/Sanic-For-Pythoneer

优秀的项目:gitter
https://gitter.im/?utm_source=left-menu-logo
https://irc.gitter.im/
https://gitter.im/login

机器学习算法:
https://github.com/guofei9987/scikit-opt?utm_source=gold_browser_extension
Python实现的算法:
git@github.com:TheAlgorithms/Python.git

myBase Desktop 是一款用于分类存储管理任意格式资料的小型个人数据库软件:
http://www.wjjsoft.com/mybase_cn.html
破解教程:
http://www.32r.com/soft/39166.html
个人知识库搭建教程:
https://www.cnblogs.com/d2zs/p/12095889.html
http://www.eryajf.net/1040.html

#########################################
Sublime Text 3激活注册码 （亲测可用）

----- BEGIN LICENSE -----
Member J2TeaM
Single User License
EA7E-1011316
D7DA350E 1B8B0760 972F8B60 F3E64036
B9B4E234 F356F38F 0AD1E3B7 0E9C5FAD
FA0A2ABE 25F65BD8 D51458E5 3923CE80
87428428 79079A01 AA69F319 A1AF29A4
A684C2DC 0B1583D4 19CBD290 217618CD
5653E0A0 BACE3948 BB2EE45E 422D2C87
DD9AF44B 99C49590 D2DBDEE1 75860FD2
8C8BB2AD B2ECE5A4 EFC08AF2 25A9B864
------ END LICENSE ------​

########################################

Python 常见文件格式 .py .pyc .pyw .pyo .pyd 之间的主要区别:
http://forum.digitser.cn/thread-1758-1-1.html

Sublime Text3 添加右键快捷方式:
https://www.jb51.net/article/130391.htm