# Python functools模块完全攻略（看了无师自通）


"""
functools 模块中主要包含了一些函数装饰器和便捷的功能函数。在 Python 的交互式解释器中先导入 functools 模块，然后输入 [e for e in dir(functools) if not e.startswith('_')] 命令，即可看到该模块所包含的全部属性和函数：
>>> [e for e in dir(functools) if not e.startswith('_')]
['MappingProxyType', 'RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'WeakKeyDictionary', 'cmp_to_key', 'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod', 'recursive_repr', 'reduce', 'singledispatch', 'total_ordering', 'update_wrapper', 'wraps']


在functools 模块中常用的函数装饰器和功能函数如下：
functools.cmp_to_key(func)：将老式的比较函数（func）转换为关键字函数（key function）。在 Python 3 中比较大小、排序都是基于关键字函数的，Python 3 不支持老式的比较函数。
@functools.lru_cache(maxsize=128, typed=False)：该函数装饰器使用 LRU（最近最少使用）缓存算法来缓存相对耗时的函数结果，避免传入相同的参数重复计算。同时，缓存并不会无限增长，不用的缓存会被释放。其中 maxsize 参数用于设置缓存占用的最大字节数，typed 参数用于设置将不同类型的缓存结果分开存放。
@functools.total_ordering：这个类装饰器（作用类似于函数装饰器，只是它用于修饰类）用于为类自动生成比较方法。通常来说，开发者只要提供 __lt__()、__le__()、__gt__()、__ge__() 其中之一（最好能提供 __eq__() 方法），@functools.total_ordering装饰器就会为该类生成剩下的比较方法。
functools.partial(func, *args, **keywords)：该函数用于为 func 函数的部分参数指定参数值，从而得到一个转换后的函数，程序以后调用转换后的函数时，就可以少传入那些己指定值的参数。
functools.partialmethod(func, *args, **keywords)：该函数与上一个函数的含义完全相同，只不过该函数用于为类中的方法设置参数值。
functools.reduce(function, iterable[, initializer])：将初始值（默认为 0，可由 initializer 参数指定）、迭代器的当前元素传入 function 函数，将计算出来的函数结果作为下一次计算的初始值、迭代器的下一个元素再次调用 function 函数……依此类推，直到迭代器的最后一个元素。
＠functools.singledispatch：该函数装饰器用于实现函数对多个类型进行重载。比如同样的函数名称，为不同的参数类型提供不同的功能实现。该函数的本质就是根据参数类型的变换，将函数转向调用不同的函数。
functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)：对 wrapper 函数进行包装，使之看上去就像 wrapped（被包装）函数。
@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)：该函数装饰器用于修饰包装函数，使包装函数看上去就像 wrapped 函数。
通过介绍不难发现，functools.update_wrapper 和 ＠functools.wraps 的功能是一样的，只不过前者是函数，因此需要把包装函数作为第一个参数传入；而后者是函数装饰器，因此使用该函数装饰器修饰包装函数即可，无须将包装函数作为第一个参数传入。

"""

from functools import *

# 以初始值(默认为0)为x,以当前序列元素为y,x+y的和 作为下一次的初始值
print(reduce(lambda x,y:x + y,range(5)))  # 10
print(reduce(lambda x,y:x + y,range(6)))  # 15

# 设置初始值为10
print(reduce(lambda x,y:x + y,range(6),10))  # 25
print("\n--------------")


class User:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Username={username}".format(username=self.name)

# 定义一个老式的大小比较函数,User的name越长,该User越大
def old_cmp(u1,u2):
    return len(u1.name) - len(u2.name)

my_data = [User("Kotlin"),User("Swift"),User("Go"),User("Java")]

# 对my_data排序,需要关键字参数(调用cmp_to_key将old_cmp转换为关键字参数)
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print("----------------------")

@lru_cache(maxsize=32)
def factorial(n):
    print("~~计算{n}的阶乘~~".format(n=n))
    if n== 1:
        return 1
    else:
        return n*factorial(n-1)

# 只有这行会计算,然后会缓存5,4,3,2,1的阶乘
print(factorial(5))
print(factorial(3))
print(factorial(5))
print("------------------")
# int函数默认将10进制的字符串转换为整数
print(int("12345"))
print(type(int("12345")))

# 为int函数的base参数指定参数值
basetwo = partial(int,base=2)

basetwo.__doc__ = "将二进制的字符串转换成整数"
# 相当于执行base为2的int()函数
print(basetwo("10010"))  # 8
print(int("10010",2))  # 8


"""
上面程序中第3行代码调用reduce()函数来计算序列的"累计"结果,在调用该函数时传入的
第一个参数(函数)决定了累计算法,此处使用的累计算法是"累加".

程序第18行代码调用cmp_to_key()函数将老式的大小比较函数(old_cmp)转换为关键字参数,
这样该关键字参数即可作为列表对象的sort()方法的参数.

程序的第21行代码调用@lru_cache对函数结果进缓存,后面程序第一次执行factorial(5)时
将会看到执行结果.但接下来调用factorial(3),factorial(5)时都不会看到执行结果,因为
它们的结果已经被缓存起来


程序第 36 行代码调用 paitial() 函数为 int() 函数的 base 参数绑定值“2”，这样程序以后调用该函数时实际上就相当于调用 base 为 2 的 int() 函数。
所以，上面程序中最后两行代码的本质是完全一样的。

partialmethod() 与 partial() 函数的作用基本相似，区别只是 partial() 函数用于为函数的部分参数绑定值；
而 partialmethod() 函数则用于为类中方法的部分参数绑定值。如下程序示范了 partialmethod() 函数的用法：

"""

from functools import *

class Cell:
    def __init__(self):
        self._alive = False

    # @property装饰器指定该方法可以使用属性语法访问
    @property
    def alive(self):
        return self._alive

    def set_state(self,state):
        self._alive = bool(state)

    # 指定set_alive()方法就是将set_state()方法的state参数指定为True
    set_alive = partialmethod(set_state,True)
    # 指定set_dead() 方法就是将set_state()方法的state参数指定为False
    set_dead = partialmethod(set_state,False)

c = Cell()
print(c.alive)

# 相当于调用c.set_state(True)
c.set_alive()
print(c.alive)

# 相当于调用c.set_state(False)
c.set_dead()
print(c.alive)


"""
上面程序定义了一个 Cell（细胞）类，在该类中定义了一个 set_state() 方法，
该方法用于设置该细胞的状态。程序接下来使用 partialmethod() 函数为 set_state() 方法绑定了参数值；
将 set_state() 方法的参数值绑定为 True 之后赋值给了 set_alive() 方法；
将 set_state() 方法的参数值绑定为 False 之后赋值给了 set_dead() 方法。

因此，程序调用 c.set_alive() 就相当于调用 c.set_state(True)；程序调用 c.set_dead() 就相当于调用 c.set_state(False)。

下面程序示范了@total_ordering类装饰器的作用:

"""
from functools import *

@total_ordering
class User:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Username={username}".format(username=self.name)

    # 根据是否有name属性来决定是否可比较
    def _is_vaild_operand(self,other):
        return hasattr(other, "name")

    def __eq__(self,other):
        if not self._is_vaild_operand(other):
            return NotImplemented

        # 根据name判断是否相等(都转成小写比较,忽略大小写)
        return self.name.lower() == other.lastname,lower()

    def __lt__(self,other):
        if not self._is_vaild_operand(other):
            return NotImplemented

        # 根据name判断是否相等(都转成小写比较,忽略大小写)
        return self.lastname.lower() < other.lastname.lower()

# 打印被装饰之后的User类中的__gt__方法
print(User.__gt__)
print(User.__ge__)
print(User.__le__)
print(User.__ne__)

"""
上面程序定义了一个 User 类，并为该类提供了 __eq__、__lt__ 两个比较大小的方法。程序中使用 ＠total_ordering 装饰器修饰了该 User 类，这样该装饰器将会为该类提供 __gt__、__ge__、__le__、__ne__ 这些比较方法。上面程序中最后一行输出了 User 类的 __gt__ 方法。运行该程序，可以看到如下输出结果：
<function _gt_from_lt at 0x00000000028C2D90>

从上面的输出结果可以看到，此时的 __gt__ 方法是根据 __lt__ 方法“生产”出来的。

但如果将上面程序中 ＠total_ordering 注释掉，再次运行该程序，则可以看到如下输出结果：
<slot wrapper '__gt__' of 'object' objects>

从上面的输出结果可以看到，此时该 __gt__ 方法其实来自父类 object。
"""

"""
@singledispatch函数装饰器的作用是根据函数参数类型转向调用另一个函数,从而实现函数
重载的功能.例如:如下程序示范了该函数装饰器的用法:

"""

from functools import *

@singledispatch
def test(arg,verbose):
    if verbose:
        print("默认参数为:",end=" ")
    print(arg)

# 限制test函数第一个参数为int型的函数版本.全看这里的这个注册的函数是啥
@test.register(int)
def _(argu,verbose):
    if verbose:
        print("整型参数为:",end=" ")
    print(argu)

test("Python",True)
# 调用第一个参数为int型的版本
test(20,True)
test({},True)


"""
上面程序中第 2 行代码使用 ＠singledispatch 装饰器修饰了 test() 函数，接下来程序即可通过 test() 函数的 register() 方法来注册被转向调用的函数。第 8 行代码使用 @test.register(int) 修饰了目标函数，这意味着如果 test() 函数的第一个参数为 int 类型，实际上则会转向调用被 ＠test.register(int) 修饰的函数。

使用 ＠singledispatch 装饰器修饰之后的函数就有了 register() 方法，该方法用于为指定类型注册被转向调用的函数。

程序中 ① 号代码在调用 test() 函数时第一个参数是 str 类型，因此程序依然调用 test() 函数本身；程序中 ② 号代码在调用 test() 函数时第一个参数是 int 类型，因此将会转向调用被 ＠test.register(int) 修饰的函数。

运行上面程序，可以看到如下输出结果：
默认参数为：Python
整型参数为：20

程序还可继续使用@test.register()装饰器来绑定被转向调用的函数.例如如下代码:
"""

# 限制test函数第一个参数为list型的函数版本
@test.register(list)
def _(argb,verbose=False):
    if verbose:
        print("列表中所有元素为:")
    for i,elem in enumerate(argb):
        print(i,elem,end=" ")

test([20,10,16,30,14],True)
print("\n---------------------------")

"""
上面第 2 行代码显示 test() 函数的第一个参数是 list 时将转向调用被 ＠test.register(list) 修饰的函数。而上面程序中 ③ 号代码在调用 test() 函数时第一个参数是 list 对象，因此这行代码将会转向调用被 ＠test.register(list) 修饰的函数。运行上面代码，将看到如下输出结果：
0 20 1 10 2 16 3 30 4 14
---------------
"""

"""
此外,程序也可使用register(类型,被转向调用的函数)方法来执行绑定.这种放肆与前面使用函数装饰器的本质是一样的.
只不过这种语法没有修饰被转向调用的函数,因此额外多传入一个参数,例如如下代码:

"""

print("\n---------------------")
# 定义一个函数,不使用函数装饰器修饰
def nothing(arg,verbose=False):
    print("~~None参数~~")

# 当test函数第一个参数为None类型时,转向为调用nothing函数
test.register(type(None),nothing)
test(None,True)
print("\n---------------")

"""
上面程序中指定调用 test() 函数的第一个参数为 None 类型时，程序将会转向调用 nothing 函数。而 ④ 号代码在调用 test() 函数时第一个参数是 None，因此这行代码将会转向调用 nothing 函数。运行上面代码，可以看到如下输出结果：
~~None参数~~

---------------

此外，＠singledispatch 也允许为参数的多个类型绑定同一个被转向调用的函数：只要使用多个 ＠ 函数名.register() 装饰器即可。例如如下代码：
"""
from decimal import Decimal

# 限制test函数第一个参数为float或Decimal型的函数版本
@test.register(float)
@test.register(Decimal)
def test_num(arg,verbose=False):
    if verbose:
        print("参数的一半为:",end=" ")
    print(arg/2)

"""
程序中使用@test.register(float),@test.register(Decimal)修饰test_num函数,这意味着程序在
调用test()函数时,无论第一个参数是float类型还是Decimal类型,其实都会转向调用test_num函数.


当程序为@singledispatch函数执行绑定之后,程序就可以通过该函数的dispatch类型方法来找到
该类型所对应转向的函数.例如如下代码:
"""
# test_dispatch(类型)即可获取它转向的函数
# 当test()函数第一个参数为float时将转向到调用test_num
print(test_num is test.dispatch(float))  # True
# 当test()函数第一个参数为Decimal时将转向到调用test_num
print(test_num is test.dispatch(Decimal))

# 直接调用test并不等于test_num
print(test_num is test)

"""
由于程序在调用test()函数时无论第一个参数是float还是Decimal,都会转向调用test_num函数,
因此test.dispatch(float)和test.dispatch(Decimal)其实就是test_num函数.运行上面代码,将
看到如下输出结果:
True
True
False

此外，如果想访问 ＠singledispatch 函数所绑定的全部类型及对应的 dispatch 函数，
则可通过该函数的只读属性 registry 来实现，该属性相当于一个只读的 dict 对象。例如如下代码：

"""

print("\n-------------------")
# 获取test函数所绑定的全部类型
print(test.registry.keys())

print("\n-------------------")
# 获取test函数为int类型绑定的函数
print(test.registry[int])


"""
运行上面代码，可以看到如下输出结果：
dict_keys([<class 'object'>, <class 'int'>, <class 'list'>, <class 'NoneType'>, <class 'decimal.Decimal'>, <class 'float'>])
<function _ at 0x0000025910082730>
"""

"""
@wraps(wrapped_func)函数装饰器与update_wrapper()函数的作用是一样的.都用于让包装函数
看上去就像被包装函数(主要就是让包装函数的__name__,__doc__)属性与被包装函数保持一致.
区别是@wraps函数装饰器直接修饰包装函数,因此不需要传入包装函数作为参数,而update_wrapper()
则需要同时传入包装函数,被包装函数作为参数.

如下程序示范了@wraps()函数装饰器的用法:

"""
from functools import wraps

def fk_decorator(f):
    # 让wrapper函数看上去就像f函数
    @wraps(f)
    def wrapper(*args,**kwargs):
        print("调用被装饰函数")
        return f(*args,**kwargs)
    return wrapper


@fk_decorator
def test():
    """test函数的说明信息"""
    print("执行test函数")
test()
print(test.__name__)
print(test.__doc__)

"""
程序中的第5行代码的作用是让被包装函数wrapper就像f函数.程序使用@fk_decorator
修饰test()函数,因此在调用test()函数时,实际上是调用fk_decorator的返回值wrapper
函数(这是前面的函数装饰器的功能).

也就是说,上面程序中最后三行看上去是访问test函数,实际上是访问wrapper函数.由于程序
使用@wraps(f)修饰了wrapper函数,因此该函数看上去就像test函数.所以,程序在输出test.__name__
和test.__doc__时(注意此处的test其实是wrapper函数),输出的依然是test函数名,描述文档.

运行上面代码，将看到如下输出结果：
调用被装饰函数
执行test函数
test
test函数的说明信息
<<<<<<< HEAD
这是个啥?
https://gio.ren/w/AovVzzoz
=======

>>>>>>> develop-1.0.0
如果注释掉程序中第 5 行代码，此时将不能让 wrapper 函数看上去像 test 函数。如果再次运行该程序，将看到如下输出结果：
调用被装饰函数
执行test函数
wrapper
None
<<<<<<< HEAD
加入齐塔
https://qiita.com/registration
=======


>>>>>>> develop-1.0.0
"""

