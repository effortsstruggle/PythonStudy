#day10 Python 元组 补充（day02 中 元组）
""""""
"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号()，列表使用方括号[];元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    格式如下所示：
        tup2 = (value1, ..., valueN)
    
创建空元组 : tup1 = ()
元组中只包含一个元素时，需要在元素后面添加逗号 : tup1 = (50,)

Python元组运算符
    len((1, 2, 3))                              ： 获取元组长度
    (1, 2, 3) + (4, 5, 6)	                    ： 元组组合
    ('Hi!') * 4	                        	    ： 重复打印元组
    3 in (1, 2, 3)	True	                    ： 元素是否存在于元组中
    for x in (1, 2, 3): print x	                ： 元组迭代
    
Python元组截取
    L[2]	读取列表中第三个元素
    L[-2]	读取列表中倒数第二个元素
    L[1:]	从第二个元素开始截取列表
    
Python 无关闭分隔符
    任意无符号的对象，以逗号隔开，默认为元组
     print 'abc', -4.24e93, 18+6.6j, 'xyz'
     x, y = 1, 2
     print "Value of x , y : ", x,y
     
Python 元组内置函数
    cmp(tuple1, tuple2)     比较两个元组元素。
    len(tuple)              计算元组元素个数。
    max(tuple)              返回元组中元素最大值。
    min(tuple)              返回元组中元素最小值。
    tuple(seq)              将列表转换为元组。
"""

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")

#访问元组
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])


#修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合；
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
tup4 = tup1 + tup2
print(f"连接tup1+tup2 :{tup4}")

#删除元组
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

print(tup1)
del tup1
# print("After deleting tup : ",tup1)
