#day12 Python集合
""""""

"""
集合（set）是一个无序的不重复元素序列。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔 ， 或者也可以使用 set() 函数创建集合。

创建格式：
    parame = {value01,value02,...}
    或者
    set(value)
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

集合运算:
    set1 - set2 
    set1 | set2 
    set1 & set2 
    set1 ^ set2 
集合内置方法:
    add()	                        为集合添加元素
    clear() 	                    移除集合中的所有元素
    copy()	                        拷贝一个集合
    difference()	                返回多个集合的差集
    difference_update()	            移除集合中的元素，该元素在指定的集合也存在。
    discard()	                    删除集合中指定的元素
    intersection()	                返回集合的交集
    intersection_update()	        返回集合的交集。
    isdisjoint()	                判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
    issubset()	                    判断指定集合是否为该方法参数集合的子集。
    issuperset()	                判断该方法的参数集合是否为指定集合的子集
    pop()	                        随机移除元素
    remove()	                    移除指定元素
    symmetric_difference()	        返回两个集合中不重复的元素集合。
    symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
    union()	                        返回两个集合的并集
    update()	                    给集合添加元素
    len()	                        计算集合元素个数
"""

# 这里演示的是去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 快速判断元素是否在集合内
print('orange' in basket)
print('crabgrass' in basket)

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')

print(f"a:{a} , b:{b}")

# 集合a中包含而集合b中不包含的元素(差集)
print("a - b : ", a - b)

# 集合a或b中包含的所有元素（并集）
print("a | b : ", a | b)

# 集合a和b中都包含了的元素（交集）
print("a & b : ", a & b)

# 不同时包含于a和b的元素(a和b不同的数据)
print("a ^ b : ", a ^ b)


#添加元素
a.add("test")
print(f"a.add(test) : {a}")
#添加元素（参数可接受： 列表，元组，字典等）
a.update(("1", "3", "4"))
print(f"集合添加元组 : {a}")

#移除元素（元素不存在发生错误）
a.remove("1")
print(f"移除元素1 : {a}")
#移除元素（元素不存在不发生错误）
a.discard("5")
print(f"移除元素5 : {a}")
#随机删除元素（因为set无序，pop弹出最后一个元素，所以形成随机删除）
a.pop()
print(f"随机删除元素 : {a}")

#集合中元素个数
print(f"元素个数：{len(a)}")

#清空集合
a.clear()
print("清空后的集合 : ", a)

#判断元素是否在集合中
print("判断元素是否在集合中: ", "1" in a)


