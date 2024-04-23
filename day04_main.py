#day04 运算符
""""""
#1. Python解释器
"""
Linux/Unix的系统上，一般默认的 python 版本为 2.x，我们可以将 python3.x 安装在 /usr/local/python3 目录中。
安装完成后，我们可以将路径 /usr/local/python3/bin 添加到您的 Linux/Unix 操作系统的环境变量中，这样您就可以通过 shell 终端输入下面的命令来启动 Python3 。
$ PATH=$PATH:/usr/local/python3/bin/python3    # 设置环境变量
$ python3 --version
Python 3.4.0

"""
#1.1 python交互式编程
#python交互式编程客户端 ，执行 cmd -> 运行 python 即可进入交互式编程客户端

#1.2 脚本式编程
#通过脚本参数调用解释器开始执行脚本，直到脚本执行完毕。当脚本执行完成后，解释器不再有效；


#2.注释
#在 Python3 中，注释不会影响程序的执行，但是会使代码更易于阅读和理解。

#2.1 单行注释
#Python 中单行注释以 # 开头

#2.2 多行注释
#多行注释 用一对 三个单引号 ''' 或者 三个双引号 """ 将注释括起来

#3.运算符
"""
    Python支持以下类型的运算符：
        算术运算符 :  + , - , * , / , % (取余) , **(幂 - 返回x的y次幂) , // ( 取整除 - 往小的方向取整数 	 >>> 9//2 ，结果： 4   >>> -9//2 结果： -5 )
        比较（关系）运算符 : == , != , > , < , >= , <= , 
        赋值运算符 :  = , += , -= , *= , /= , %= , **=(幂赋值运算符) , //=(取整除赋值运算符) ,  
                    := (海象运算符 , 这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值 , Python3.8 版本新增运算符 )
        逻辑运算符 : and , or , not 
        位运算符 : 按位运算符是把数字看作二进制来进行计算的 
            & , | , ^(异或) , ~ ,  << (左移) , >> （右移）
        成员运算符 : 
            in :  如果在指定的序列中找到值返回 True，否则返回 False。
            not in : 如果在指定的序列中没有找到值返回 True，否则返回 False。
        身份运算符 : 用于比较两个对象的存储单元 ( 若值相同：它们就是引用自同一对象 )
            is :  判断两个标识符是不是引用自一个对象
            is not : 判断两个标识符是不是引用自不同对象
            
            is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
            
        运算符优先级 
        1 . (expressions...),[expressions...], {key: value...}, {expressions...} ： 括号表达式
        2 . x[index], x[index:index], x(arguments...), x.attribute ： 读取，切片，调用，属性引用
        3 . await x : await 表达式
        4 . ** : 乘方(指数)
        5 . +x, -x, ~x : 正，负，按位非 NOT
        6 . *, @, /, //, % : 乘，矩阵乘，除，整除，取余 
        7 . +, - : 加和减 
        8 . <<, >> : 移位
        9 . & : 按位与 AND
        10 . ^ : 按位异或 XOR
        11 . | : 按位或 OR
        12 . in,not in, is,is not, <, <=, >, >=, !=, ==  : 比较运算，包括成员检测和标识号检测
        13 . not x  : 逻辑非 NOT
        14 . and : 逻辑与 AND
        15 . or : 逻辑或 OR
        16 . if -- else : 条件表达式
        17 . lambda : lambda 表达式
        18 . :=  ： 赋值表达式
"""
#赋值运算符 - 海象运算符
# 传统写法
n = 10
if n > 5:
    print(n)

# 使用海象运算符
if (n := 10) > 5:
    print(n)

print("")
#成员运算符

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if a in list:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if b not in list:
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if a in list:
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

print("")

#身份运算符
# id() 函数用于获取对象内存地址。
a = 20
b = 20
if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")