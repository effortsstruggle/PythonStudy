#day14 Python迭代器与生成器
""""""
import sys         # 引入 sys 模块

"""
1.迭代器
    1.迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
    2.迭代器是一个可以记住遍历的位置的对象。
    3.迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    4.迭代器有两个基本的方法：iter() 和 next()。
    5.字符串，列表或元组对象都可用于创建迭代器：
    
2.自定义可迭代对象
    a.把一个类作为一个迭代器使用，需要在类中实现两个方法 __iter__() 与 __next__() 。
    b.如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。

    c.更多内容查阅：Python3 面向对象
        __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
        __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
        
        创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
    d.StopIteration
        StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
    
3.生成器   
    在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    1.yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
    
    2.跟普通函数不同的是:生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    
    3.当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式(如：yield a ，将a作为当前迭代的值返回)作为当前迭代的值返回;
    然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
    
    4.调用一个生成器函数，返回的是一个迭代器对象。
    
    生成器函数的优势：
        1.可以按需生成值，避免一次性生成大量数据并占用大量内存。
        2.生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。
"""

list_ = [1, 2, 3, 4]
print("for循环使用迭代器")
#创建迭代器对象
it1_ = iter(list_) #等同于list_.iter(list_)
for x in it1_:
    print(x, end="\n") #可以用来禁止换行

print("while循环使用迭代器")
#创建迭代器对象
it2_ = iter(list_)
while True:
    try:
        print(next(it2_))
    except StopIteration:
        print("停止迭代")
        break
        # sys.exit() #程序退出

print("自定义可迭代对象")
#创建一个迭代器
class MyClass:
    def __iter__( self ):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration #抛出异常

myclass = MyClass()
#创建迭代器对象
myClassIter = iter(myclass)

print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))
print(next(myClassIter))

myClassIter2 = iter(myclass)
#创建迭代器对象
for v in myClassIter2:
    print("for-v : ", v)

myClassIter3 = iter(myclass)
while True:
    try:
        print("while-v", next(myClassIter3))
    except StopIteration:
        break

#创建生成器函数
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# 创建生成器对象
generator = countdown(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1



#使用 yield 实现斐波那契数列：
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()