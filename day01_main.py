
#day01: 基础语法
""""""


#Python代码书写：

"""
    常用书写规则：

    1.循环控制，分支控制，不需要加括号；
    2.函数加括号

"""

#python2.x中使用，字符编码
# coding=utf-8

#1.python交互式编程
#python交互式编程客户端 ，执行 cmd -> 运行 python 即可进入交互式编程客户端

#2.脚本式编程
#通过脚本参数调用解释器开始执行脚本，直到脚本执行完毕。当脚本执行完成后，解释器不再有效；


#3.打印输出
print("Hello world!")
print("欢迎来到Python世界!")  #Python 2.x 代码中若出现中文，需要在该文件中指定编码格式。 Python3.x中编码默认使用UTF-8

#4.python标识符
#标识符由字符、数字、下划线组成；
#不能以数字开头；
#以“单下划线”开头（如：_foo），代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用from *** import *而导入；
#以“双下划线”开头（如：__foo)，代表类的私有成员；
#以双下划线开头和结尾（如：__foo__）,代表python里特殊方法专用的标识，如__init__()代表类的构造函数；

#5.Python保留字
# and   （逻辑与）	    exec	    not （逻辑非）
# assert	finally	    or （逻辑或）
# break	    for （for循环）	        pass
# class （类）	    from	    print
# continue	global	    raise
# def	    if	        return
# del	    import	    try
# elif	    in	        while
# else	    is	        with
# except	lambda	    yield、

#6.行和缩进
""" 
    python和其他语言最大的区别：python的代码块不使用大括号{}来控制类，函数以及其他逻辑判断。python最具特色的就是用缩进来写模块。
    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
"""
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")

#7.多行语句
#Python语句中一般以“新行”作为语句的结束符。但可是使用“\”将一行的语句分为多行显示，如下所示：
one = "one"
two = "two"
three = "three"
total = one + \
        " " + \
        two + \
        " " + \
        three
print(total)
#语句中包含[]、{}、()括号，就不需要使用多行连接符。
days = ["Mondy", "Tuesday", "Wednesday",
        "Thursday", "Friday"]
print(days)


#8.Python引号
#Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的。
#其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print(word)
print(sentence)
print(paragraph)

#9.Python 注释
# python中单行注释采用 # 开头。
# python 中多行注释使用三个单引号 ''' 或三个双引号 """。

''' 
这是多行注释，这是多行注释；
这是多行注释，这是多行注释；
这是多行注释，这是多行注释；
'''
#10. Python空行
"""
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
"""

#11. 等待用户输入
#下面的程序执行后就会等待用户输入，按回车键后就会退出：
input("按下 enter 键退出，其他任意键显示...\n")

#12.Python同一行显示多条语句
#Python同一行使用多条语句，语句之间使用分号（;）分割，以下是一个简单实例：
import sys #导入模块
x = 'runoob'; sys.stdout.write(x + '\n')

#13.多个语句构成代码组
"""
缩进相同的一组语句构成一个代码块，我们称之代码组
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
"""
