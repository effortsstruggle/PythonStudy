#day20 Python3 I/O
""""""

"""
1.输出格式美化
    Python输出值方式：
        1.表达式语句
        2.print()函数
        3.文件输出（write函数）
        4.标准输出文件（sys.stdout）
        5.错误输出文件（sys.stderr）
        
    输出格式美化： 
        使用str.format()方法，可以格式化输出值，使其更加美观。 
        !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化;
        : 后传入一个整数, 可以保证该域(输出内容)至少有这么多的宽度
        % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串；
        示例：
            print("Hello, {0}!".format("world")) #索引占用
            print("Hello, {name}!".format(name="world")) #关键字占用
            print('常量 PI 的值近似为： {}。'.format(math.pi))
            print('常量 PI 的值近似为： {!r}。'.format(math.pi)) #使用 repr() 转义特殊字符
            print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi)) #保留三位小数
            print('常量 PI 的值近似为 {0:.3e}。'.format(math.pi)) #用科学记数法表示
            print('{0:10s} ==> {1:10d}'.format(name, number))
            print('常量 PI 的值近似为：%5.3f。' % math.pi) #.左边宽度（5）, .右边精度（3）
            
    如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
        str()： 函数返回一个用户易读的表达形式。
        repr()： 产生一个解释器易读的表达形式。

2.读取键盘输入
    Python提供了input()函数用于从标准输入设备（通常是键盘）读取字符串，并将其转换为字符串类型。
    
3.读和写文件
    open() 将会返回一个 file 对象，基本语法格式如下:
        open(filename, mode)
    filename：包含了你要访问的文件名称的字符串值。
    mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    
    不同模式打开文件的完全列表：
        模式	描述
        r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
        rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
        r+	打开一个文件用于读写。文件指针将会放在文件的开头。
        rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
        w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
        ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
        
        模式  	    r	r+	w	w+	a	a+
        读	        +	+		+		+
        写		        +	+	+	+	+
        创建			        +	+	+	+
        覆盖			        +	+		
        指针在开始	+	+	+	+		
        指针在结尾					+	+
        
    
    file.write（ str ）        : 写入文件并返回写入的字符数；
    file.read()                  : 读取文件并返回字符串或字节对象,默认读取整个文件;(设置可选参数size, 则读取指定长度的字节)
    file.readline()              : 会从文件中读取单独的一行。换行符为 '\n' ; 如果返回一个空字符串, 说明已经已经读取到最后一行。
    file.readlines()             : 读取整个文件，并按行返回列表，各行之间自动添加换行符(设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割);
    file.close()                 : 关闭文件
    file.tell()                  : 返回当前文件指针的位置;(文件指针表示从文件开头开始的字节数偏移量)
    file.seek(offset, from_what) : 从指定位置（from_what）设置文件指针位置, from_what=0 表示开头, 1 表示当前位置, 2 表示文件末尾;
                                   offset 为正 ，向后移；为负，向前移；	
    file.flush()                 : 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
    file.fileno()                : 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
    file.isatty()                : 如果文件连接到一个终端设备返回 True，否则返回 False。
    file.next()                  : 返回文件下一行.( Python 3 中的 File 对象不支持 next() 方法。)
    file.truncate([size])        : 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
    file.writelines(sequence)    : 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
                       
                       
                              
    当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
        with open('/tmp/foo.txt', 'r') as f:
            read_data = f.read()


    文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。
    
4.pickle 模块
    Python的pickle模块实现了基本的数据序列和反序列化。(二进制)
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
    
    基本接口：
        dump(obj, file, [,protocol])
        dumps(obj, [,protocol])
        
    有了 pickle 这个对象, 就能对 file 以读取的形式打开:
        x = pickle.load(file)
    注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
    file: 类文件对象，有read()和readline()接口
"""
import math
import pprint, pickle

print("Hello, {0} {1}!".format("world", "python"))

# repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)



#输出格式化

#rjust 方法用于将字符串靠右对齐，并使用空格填充至指定长度
#还有类似的方法, 如 ljust() 和 center()。另一个方法 zfill(), 它会在数字的左边填充 0

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))

print()

for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))

print('常量 PI 的值近似为：%6.3f。' % math.pi)

#读取键盘输入
str = input("请输入：")
print("你输入的内容是: ", str)

#读和写文件
# 打开一个文件
f = open("./foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()

#文件对象的方法



# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

read_data_ = pickle.load(pkl_file)
pprint.pprint(read_data_)

read_data2_ = pickle.load(pkl_file)
pprint.pprint(read_data2_)

pkl_file.close()

