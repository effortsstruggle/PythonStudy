#day23 Python3面向对象
""""""
"""
1.类定义
    语法格式如下：
        class ClassName:
            <statement-1>
            .
            .
            .
            <statement-N>
2.类对象
    类对象支持两种操作：属性引用和实例化。
    属性引用 : 类对象.属性名
    实例化 : 类名()
3.类的构造方法
     __init__() 构造方法，在对象创建时调用，用于对对象进行初始化。
     def __init__(self):
         self.data = []
4.类的属性
    类属性是指类级别的变量，可以通过类名.属性名来访问。
    类属性可以通过 self.属性名 来设置。
    类的私有属性：属性名称前面加上两个下划线 __ 。
    类的保护属性：属性名称前面加上单个下划线 _ 。
    类的公有属性：没有特殊的前缀。
    
5.类的方法
    1.在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
    2.类的方法是指类中定义的函数，可以通过实例对象.方法名() 来调用。
    3.类方法可以通过 @classmethod 装饰器来定义。
    4.实例方法可以通过 @staticmethod 装饰器来定义。
    
    类的私有方法：方法名称前面加上两个下划线 __ 。
    类的保护方法：方法名称前面加上单个下划线 _ 。
    类的公有方法：没有特殊的前缀。
    
6.self 代表类的实例，而非类本身。
    1.类的方法与普通的函数只有一个特别的区别——它们必须有一个 "额外的第一个参数名称" , 按照惯例它的名称是 self。
      self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的;
    2.在 Python中，self 是一个惯用的名称，用于表示类的实例（对象）自身。它是一个指向实例的引用，使得类的方法能够访问和操作实例的属性。

7.类的继承
    语法格式如下：
        class DerivedClassName(BaseClassName):
            <statement-1>
            .
            .
            .
            <statement-N>     
    1.子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
    2.BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用;
        class DerivedClassName(modname.BaseClassName):
8.类的多继承
    语法格式如下：
        class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
        .
        .
        .
        <statement-N>
    需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
    
9.方法重写
    class Parent:        # 定义父类
       def myMethod(self):
          print ('调用父类方法')
 
    class Child(Parent): # 定义子类
       def myMethod(self):
          print ('调用子类方法')
          
    c = Child()          # 子类实例
    c.myMethod()         # 子类调用重写方法
    super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
    
10.类的专有方法 (不是私有的)
    __init__()          : 构造方法，在对象创建时调用，用于对对象进行初始化。
    __del__()           : 析构方法，在对象销毁时调用，释放对象占用的资源。
    __repr__()          : 打印，转换
    __setitem__()       : 按照索引赋值
    __getitem__()       : 按照索引获取值
    __len__()           : 获得长度
    __cmp__()           : 比较运算
    __call__()          : 函数调用 （类装饰器）
    __add__()           : 加运算
    __sub__()           : 减运算
    __mul__()           : 乘运算
    __truediv__()       : 除运算
    __mod__()           : 求余运算
    __pow__()           : 乘方
    __str__()           : 输出字符串
11.运算符重载
    Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：
    class Vector:
        def __init__(self, x, y):
            self.x = x  
            self.y = y  

        def __str__(self):
            return '(%d, %d)' % (self.x, self.y)
            

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
    

    v1 = Vector(2,10)
    v2 = Vector(5,-2)
    print (v1 + v2)
"""


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


class Complex:
    # 定义构造方法
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

    # def speak(self):
    #     student.speak(self)

s = student('ken', 10, 60, 3)
s.speak()

sp_ = sample('Tim', 15, 70, 4, 'Python 程序设计')
sp_.speak()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1.__str__())