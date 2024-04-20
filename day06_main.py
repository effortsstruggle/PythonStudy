#day05 python 控制结构


#1. Python 条件控制
"""
if 基本格式1 ：

    if 判断条件：
        执行语句……
        执行语句……
    else：
        执行语句……
        执行语句……

if 基本格式2 ：

    if 判断条件1:
        执行语句1……
    elif 判断条件2:
        执行语句2……
    elif 判断条件3:
        执行语句3……
    else:
        执行语句4……

"""

#2. Python 循环控制
"""
1.for循环 
基本格式 ：    
    for iterating_var in sequence:
        statements(s)
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
        
基本格式2 ：    
    for iterating_var in sequence:
        statements(s)
    else:
        statements(s)
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break ）的跳出而中断的情况下执行，while … else 也是一样。

    
2. while循环 
基本格式：
    while 判断条件(condition)：
        执行语句(statements)……
        
    Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务

3.嵌套循环 
基本格式：
    for iterating_var in sequence:
       for iterating_var in sequence:
          statements(s)
       statements(s)
       
       
    while expression:
        while expression:
            statement(s)
        statement(s)
4.break / continue / pass 语句    
    continue ： 跳出本次循环
    break ： 跳出整个循环 
    pass ：用来保持结构完整性（ 不做任何事情，一般用做占位语句。）
"""

count = 0
while count < 10 :
    print("count = %d" % count)
    count += 1

#for循环 遍历方式1 （常用）

for letter in 'Python':  # 第一个实例
    print("当前字母: %s" % letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print("当前水果: %s" % fruit)

#for循环 遍历方式2（通过序列索引迭代）

for count in range(0, 10):
    print("count = %d" % count)
    count += 1


fruits = ['banana', 'apple', 'mango']
len_ = len(fruits)
range_ = range(len_)
print(f"len_ = {len_} , range_ = {range_}")
for index_ in range_:
    print("当前水果 : %s" % fruits[index_])

#for循环 遍历方式3（循环使用else语句）

# for num in range(10, 20):   # 迭代 10 到 20 (不包含) 之间的数字
#    for i in range(2, num):  # 根据因子迭代
#       if num % i == 0:      # 确定第一个因子
#          j = num/i          # 计算第二个因子
#          print("%d 等于 %d * %d" % (num, i, j))
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       print("%d 是一个质数（素数）" % num) # 质数（素数） 只能整除1和它本身


#嵌套循环 （ 2~100的素数 ）

i_ = 2
while i_ < 100:
    isfalg_ = 0
    j_ = 2
    while j_ < i_:
        if i_ % j_ == 0:
            num_ = i_ / j_  # 计算第二个因子
            print("%d 等于 %d * %d" % (i_, num_, j_))
            isfalg_ = 0
            break
        else:
            isfalg_ = 1

        j_ += 1

    if isfalg_ or i_ == 2:
        print("%d 是一个质数（素数）" % i_)  # 质数（素数） 只能整除1和它本身

    i_ += 1