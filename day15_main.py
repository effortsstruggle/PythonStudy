#day15 Python函数
""""""

"""
1.Python定义函数规则：
    1.函数代码块以 def 关键词开头 + 函数标识符名称 + 圆括号 ()。
    2.任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    3.函数的第一行语句可以选择性地使用文档字符串 --- 用于存放函数说明。
    4.函数内容以冒号 : 起始，并且缩进。
    5.return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
2.函数格式如下：
    def 函数名（参数列表）:
        函数体
        
    默认情况下，参数值 和 参数名称 是按函数声明中定义的顺序匹配起来的。
    
3.函数调用:
    函数名（参数列表）

4.参数传递：
    在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的
    如：
        a=[1,2,3]
        a="Runoob"

    以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
    
    可更改(mutable)与不可更改(immutable)对象:
        1.在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
        2.不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
        3.可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

    python 函数的参数传递：
        1.不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
        2.可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

    总结：python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
    
参数:
    调用函数时可使用的正式参数类型：
        1.必需参数 -- 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
        2.关键字参数 -- 关键字参数和函数调用关系紧密，函数调用"使用关键字参数"来确定传入的参数值。
                1.关键字参数可以不按顺序传入，函数可以解析出参数名和参数值。 
                2.关键字参数可以有缺省值  
               def printme( str ):
                   print (str)
                   return
                printme( str = "菜鸟教程")      
                
        3.默认参数 -- 默认参数可以简化调用者的代码，如果没有传入相应的参数，则使用默认参数的值。
            def printinfo( name, age = 35 ):
               print ("名字: ", name)
               print ("年龄: ", age)
               return
            printinfo( age=50, name="runoob" )
            print ("------------------------")
            printinfo( name="runoob" )
            
        4.不定长参数 -- 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
            def printinfo( arg1, *vartuple ):
               print ("输出: ")
               print (arg1)
               for var in vartuple:
                  print (var)
            加了星号 * 的参数 会以元组(tuple)的形式导入，存放所有未命名的变量参数。
            
            
            def printinfo( arg1, **vardict ):
               print ("输出: ")
               print (arg1)
               for key, value in vardict.items():    # 遍历字典
                  print ("%s : %s" % (key, value))
            printinfo(1, a=2,b=3)
            加了两个星号 ** 的参数 会以字典的形式导入，字典的键为参数名，值为参数值。
            
            def f(a,b,*,c):   # * 后面的参数必须用关键字传入
                return a+b+c
            f(1,2,c=3) 
            声明函数时，参数中星号 * 可以单独出现 , 单独出现星号 *，则星号 * 后的参数必须用关键字传入
            
5.匿名函数:
    1.匿名函数又称为 lambda 函数，它是一个表达式，可以用来创建小函数。
    2.所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    3.lambda 只是一个表达式，函数体比 def 简单很多。
    4.lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
    5.lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    6.虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。
    
    语法： 
        lambda 参数列表:表达式
    示例:
        # 匿名函数作为参数传递
        add = lambda x, y: x + y
        print(add(1, 2)) # 输出 3
        
        # 匿名函数也可以作为返回值返回
        def build(x, y):
            return lambda: x + y
        add_two = build(2, 3)
        print(add_two()) # 输出 5
6.return 语句:
    1.return 语句是函数的结束语句，函数执行到此语句时，函数就执行完毕，并将结果返回。
    2.return 语句可以带一个表达式，这个表达式的计算结果将作为函数的返回值。
    3.如果函数没有 return 语句，或者 return 语句没有带表达式，则返回 None。
    4.return 语句可以用在循环、条件语句和其他控制流结构中，可以提前结束函数的执行。
    
7.强制位置参数
    1.在 Python 中，位置参数是指在函数调用时，按照函数定义中参数的顺序传入参数值。
    2.强制位置参数是指，在函数定义中，通过指定参数名，将参数强制设定为位置参数。
    3.强制位置参数的好处是，可以提高函数的可读性，并减少出错的可能性。
    4.强制位置参数的语法如下：
        def 函数名(参数名1, 参数名2, /, 参数名3, 参数名4):
            函数体
            
    示例：
        def my_function(a, b, /, c, d): # / 表示强制位置参数,可以按顺序传入参数，也可使用关键字传入
            return a + b + c + d
        print(my_function(1, 2, 3, 4)) # 输出 10
        print(my_function(1, 2, d=3, c=4)) # 输出 10
"""

# 定义一个函数
def my_function(x, y):
    """
    值相加
    """
    # 函数体
    result = x + y
    return result

# 调用函数
res_ = my_function(10,20)
print(res_)  # 30

def max_num(a, b):
    """
    两个数比较，返回较大的数
    """
    if a > b:
        return a
    else:
        return b
#调用函数
res_ = max_num(10,20)
print(res_)  # 20



def test_func(a, b):
    """
    测试函数
    """
    a = (5, 6, 7)
    b[0] = 2
    print("a =", a)
    print("b =", b)

a , b = (1, 2, 3), [4, 5, 6]
test_func(a, b)
print("a =", a)
print("b =", b)


def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)

printinfo(70, 60, 50)


def printinfo2(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)
# 调用printinfo 函数
printinfo2(1, a=2, b=3)


def my_function(a, b, /, c, d):  # / 表示强制位置参数,可以按顺序传入参数，也可使用关键字传入
    return a + b + c + d


print(my_function(1, 2, 3, 4))  # 输出 10
print(my_function(1, 2, d=3, c=4))  # 输出 10