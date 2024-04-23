#day09 Python List 补充（day02 中 List）
""""""
"""
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
1.Python有6个序列的内置类型，但最常见的是列表和元组。
2.序列都可以进行的操作包括 索引，切片，加，乘，检查成员。此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
3.列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表的数据项不需要具有相同的类型
    
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5 ]
    list3 = ["a", "b", "c", "d"]
    
Python列表运算符
    len([1, 2, 3])                              ： 获取列表长度
    [1, 2, 3] + [4, 5, 6]	                    ： 列表组合
    ['Hi!'] * 4	                        	    ： 重复打印列表
    3 in [1, 2, 3]	True	                    ： 元素是否存在于列表中
    for x in [1, 2, 3]: print x	                ： 列表迭代

Python列表截取
    L[2]	读取列表中第三个元素
    L[-2]	读取列表中倒数第二个元素
    L[1:]	从第二个元素开始截取列表
    
Python列表函数&方法
    cmp(list1, list2)   比较两个列表的元素
    len(list)           列表元素个数
    max(list)           返回列表元素最大值
    min(list)           返回列表元素最小值
    list(seq)           将元组转换为列表
    
    list.append(obj)                                在列表末尾添加新的对象
    list.count(obj)                                 统计某个元素在列表中出现的次数
    list.extend(seq)                                在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list.index(obj)                                 从列表中找出某个值第一个匹配项的索引位置
    list.insert(index, obj)                         将对象插入列表
    list.pop([index=-1])                            移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list.remove(obj)                                移除列表中某个值的第一个匹配项
    list.reverse()                                  反向列表中元素
    list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序

"""
#访问列表
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

#更新列表
list1.append('Google')   ## 使用 append() 添加元素
list1.append('Runoob')
print(list1)

#删除列表
print("before deleting value : ", list1)
del list1[2]
list1.remove(2000)
print("After deleting value : ", list1)