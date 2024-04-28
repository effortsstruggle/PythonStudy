#day19 Python3 模块
""""""

"""
    模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
    
1. import
    1.import 语句:
        使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
                import module1[, module2[,... moduleN]
    
    2.当解释器遇到import语句时，若模块在当前搜索路径，模块就会被导入。
    3.一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。
    4.当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？
        这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。
        这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
        搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在 sys 模块中的 path 变量
    4.使用” 模块名称.函数名 “ 调用模块中的函数。
    5.若经常使用一个函数中的函数，可以赋值给一个别名，以方便调用。
        别名 = 模块名称.函数名
        
2. from... import...
    1.from 语句:
        语法：from module import name1[, name2[,... nameN]]
        作用：从模块中导入指定的对象或函数至当前命名空间，可以用别名来表示。
3. from … import * 语句
    1.from 语句:
        语法：from module import *
        作用：从模块中导入所有对象或函数至当前命名空间，可以用别名来表示。
        
4. import module 与 from module import * 的区别
    import module : 不会把被导入的"模块的名称(module)"放在当前的字符表中。(需要 module.函数 或 module.变量 )
    form module import * : 会把被导入的模块的名称放在当前的字符表中，可以直接使用模块中的函数或变量。（不需要 module.函数或 module.变量 ）
    
5. __name__属性
    1.当一个模块被直接运行时，其 __name__ 属性被设置为 __main__ 。
    2.当一个模块被导入时，其 __name__ 属性被设置为模块的名字。
    3.在一个模块中，如果要判断当前模块是否被直接运行，可以用 __name__ 属性。  
    4.在一个模块中，如果要判断当前模块是否被导入，可以用 __name__ 属性。
    5. 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入其他模块。
        说明： __name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
6. dir函数
    dir() 函数可以查看一个模块里定义的所有名称，包括模块里的函数、类、变量等；默认为当前模块。
7. 标准模块(可在Python安装目录查询)
    1.Python 标准库包含了许多模块，可以直接使用。
    2.常用的标准库模块有：  math、random、datetime、collections、os、
                        numpy、pandas、matplotlib、scipy、sympy、    
                        json、re、urllib、csv、xml、logging、unittest、
                        multiprocessing、threading、asyncio、socket、
                        ssl、select、mmap、crypt、curses、tkinter、turtle、
                        asyncio、asyncio
8. 包(可以理解为目录)
    1.包是一种组织模块的方式，它可以将相关模块组织在一起，并提供一个公共的接口。避免不同包的模块命名冲突。
    2.包的结构：
        包名/模块名.py
        包名/__init__.py
        包名/子包名/模块名.py
        包名/子包名/__init__.py
        包名/子包名/子包名/模块名.py
        包名/子包名/子包名/__init__.py
        包名/子包名/子包名/子包名/模块名.py
        包名/子包名/子包名/子包名/__init__.py
        包名/子包名/子包名/子包名/子包名/模块名.py
        包名/子包名/子包名/子包名/子包名/__init__.py
        包名/子包名/子包名/模块名.py
        ...
    3.包的导入：
        import 包名.模块名 
        import 包名.子包名.模块名
        ...
    4.从一个包中导入* ：
         from sound.effects import * 
      导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
      使用 from Package import specific_submodule 这种方法永远不会有错。事实上，这也是推荐的方法。
      
    5.无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
"""

#标准库模块导入
"""
    1.import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
    2.sys.argv 是一个包含命令行参数的列表。
    3.sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
"""

import sys
import day17_main

print("命令行参数如下：")
for i in sys.argv:
    print(i)

print(" Python 解释器自动查找所需模块的路径的列表 : ", sys.path)

day17_main.greet("test 模块导入...")

