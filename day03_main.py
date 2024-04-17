#day03: Python数据类型转换

"""
对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可
    Python数据类型转换可分为两种：
        1.隐式类型转换 - 自动完成
        2.显式类型转换 - 需要使用类型函数来转换


以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
int(x [,base]) : 将x转换为一个整数
long(x [,base] ) : 将x转换为一个长整数
float(x)  : 将x转换到一个浮点数
complex(real [,imag]) : 创建一个复数
str(x) : 将对象 x 转换为字符串
repr(x) : 将对象 x 转换为表达式字符串
eval(str) : 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)  : 将序列 s 转换为一个元组
list(s） ： 将序列 s 转换为一个列表
set(s) ： 转换为可变集合
dict(d) ： 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) ： 转换为不可变集合
chr(x) ： 将一个整数转换为一个字符
unichr(x) ： 将一个整数转换为Unicode字符
ord(x) : 将一个字符转换为它的整数值
hex(x) : 将一个整数转换为一个十六进制字符串
oct(x) : 将一个整数转换为一个八进制字符串

"""

#隐式类型转换
"""
在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。

"""
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:", type(num_int))
print("num_flo 数据类型为:", type(num_flo))

print("num_new 值为:", num_new)
print("num_new 数据类型为:", type(num_new))

#显式类型转换
#int()
x = int(1)    # x 输出结果为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3

print("x=", x, " y=", y, " z=", z)


#float() , int() 中 x , y , z 内存会被python内置的内存垃圾收集器回收内存；
x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2
print("x=", x, " y=", y, " z=", z, " w=", w)


#str()
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

print("x=", x, " y=", y, " z=", z)