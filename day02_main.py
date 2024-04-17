#day02: 基本数据类型

#1.变量赋值
"""
    Python 中的变量赋值不需要类型声(弱类型，通过值来判断变量类型)。
    每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
    每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
    等号 = 用来给变量赋值。
    等号 = 运算符左边是一个变量名，等号 = 运算符右边是存储在变量中的值。例如：
"""
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

#2.多个变量赋值
a = b = c = 1 #多个对象指定一个值
d = e = f = 1, 2, "join" #多个对象指定集合
print(a, b, c)
print(d, e, f)

#3.标准数据类型
"""
    Numbers (数字)
    String (字符串)
    List (列表)
    Tuple (元组)
    Dictionary (字典)
"""

#4.Python数字
"""
数字数据类型用于存储数值。
他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
当你指定一个值时，Number 对象就会被创建：

可以使用del 删除单个或多个对象的引用，例如：
del var1
del var1,var2

Python支持四种不同的数字类型：
int（有符号整型） : 1 , -1
long（长整型，也可以代表八进制和十六进制）: 1000000000L ,-100000000L
float（浮点型） : 15.20 , 32.3e+18
complex（复数） : 复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
"""
var1 = 1
var2 = 10

del var1
var1 = "12345"
print(var1)


#5.Python字符串
"""
字符串或串(String)是由数字、字母、下划线组成的一串字符。

python的字串列表有2种取值顺序:
    1.从左到右索引默认0开始的，最大范围是字符串长度少1;
    2.从右到左索引默认-1开始的，最大范围是字符串开头;
    
若需要从字符串中获取一段子字符串，可使用[头下标:尾下标]，来截取相应字符串；
其中下标范围可以为[0,5]或[-6,-1]；
下标可以为空，表示取到头或尾；
包含头下标字符，不包含尾下标字符；

加号 + 是连接运算符，星号 * 是重复操作
"""


str = "Hello World!"
print(str)           # 输出完整字符串
print(str[0])        # 输出字符串中的第一个字符
print(str[2:5])      # 输出字符串中第三个至第六个之间的字符串
print(str[2:])       # 输出从第三个字符开始的字符串
print(str * 2)       # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

#6.Python列表
"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

加号 + 是连接运算符，星号 * 是重复操作
"""

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
list[0]=1 #合法赋值
print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

#7.Python元组
"""
元组是另一个数据类型，类似于 List（列表）。

元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
"""
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
tuple_dict = ({"k1": 1, "K2": 2}, {"K3": 3, "K4": 4})
# tuple[0]=1 非法

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组
print(tuple_dict)

#8.Python 字典
"""
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
"""

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


