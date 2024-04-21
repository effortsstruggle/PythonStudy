#day16 Lambda表达式
""""""
"""
    Python 使用 lambda 来创建匿名函数。

    lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。
    匿名函数不需要使用 def 关键字定义完整函数。
    lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，例如在 map()、filter()、reduce() 等函数中。

    lambda 函数特点：
        lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
        lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。
        
    lambda 语法格式：    
        lambda arguments: expression
    1.lambda是 Python 的关键字，用于定义 lambda 函数。
    2.arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
    3.expression 是一个表达式，用于计算并返回函数的结果。  
    
"""

#lamada表达式无参数
f = lambda: "Hello, world!"
print(f())  # 输出: Hello, world!

#lamada表达式有参数
g = lambda x: x + 10
print(g(5))  # 输出: 15

#lamada表达式有多个参数
h = lambda x, y: x + y
print(h(5, 10))  # 输出: 15

#lamada表达式有默认参数
i = lambda x, y=10: x + y
print(i(5))  # 输出: 15
print(i(5, 20))  # 输出: 25

#lamada表达式作为参数传递给其他函数、

#使用 lambda 函数与 map() 一起，计算列表中每个元素的平方：
lst = [1, 2, 3, 4, 5]
mp = map(lambda x: x ** 2, lst) # map(func, iterable)：允许将一个函数应用到一个可迭代对象（如：列表，元组等）的每个元素上，并返回一个新的序列。
lst = list(mp)
print(mp)
print(lst)  # 输出: [2, 4, 6, 8, 10]

#使用 lambda 函数与 filter() 一起，筛选偶数：
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter(func, iterable)：过滤序列，返回一个由所有符合条件元素组成的新列表。
print(even_numbers)  # 输出：[2, 4, 6, 8]

#使用 lambda 函数与 reduce() 一起，计算列表中元素的乘积：
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])   #reduce(func, iterable)：对可迭代对象（如：列表，元组等）的元素进行累积操作，返回最终结果。
print(product)  # 输出：40320