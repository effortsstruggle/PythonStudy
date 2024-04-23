#day07 Python Number 补充（day02 中 Number）
""""""
"""
1.Python math模块 / cmath模块

Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
Python math 模块提供了许多对浮点数的数学运算函数。
Python cmath 模块包含了一些用于复数运算的函数。

cmath 模块的函数跟 math 模块函数基本一致 , 区别 :
    1. cmath 模块运算的是复数 ;
    2. math 模块运算的是数学运算 ;

要使用 math 或 cmath 函数必须先导入：
    import math

"""


"""
Math内容
    [ '__doc__', '__loader__', '__name__', '__package__',
      '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
      'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign',
      'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc',
      'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor',
      'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf',
      'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm',
      'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf',
      'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians',
      'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


cmath 内容
    ['__doc__', '__loader__', '__name__', '__package__',
     '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
     'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj',
     'isclose', 'isfinite', 'isinf', 'isnan', 'log', 'log10',
     'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin',
     'sinh', 'sqrt', 'tan', 'tanh', 'tau']
 
 
random 内容
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random',
     'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE',
     '_Sequence', '__all__', '__builtins__', '__cached__',
     '__doc__', '__file__', '__loader__', '__name__',
     '__package__', '__spec__', '_accumulate', '_acos', '_bisect',
     '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index',
     '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os',
     '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt',
     '_test', '_test_generator', '_urandom', '_warn', 'betavariate',
     'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate',
     'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate',
     'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample',
     'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
"""

"""
Python 数学函数
    abs(x)	返回数字的绝对值，如abs(-10) 返回 10
    ceil(x)	返回数字的上入整数，如 math.ceil(4.1) 返回 5
    cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
    exp(x)	返回e的x次幂(ex),如 math.exp(1) 返回2.718281828459045
    fabs(x)	以浮点数形式返回数字的绝对值，如 math.fabs(-10) 返回10.0
    floor(x)	返回数字的下舍整数，如 math.floor(4.9)返回 4
    log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    log10(x)	返回以10为基数的x的对数，如 math.log10(100)返回 2.0
    max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
    min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
    modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
    pow(x, y)	x**y 运算后的值。
    round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
    sqrt(x)	返回数字x的平方根

Python三角函数 
    acos(x)	返回x的反余弦弧度值。
    asin(x)	返回x的反正弦弧度值。
    atan(x)	返回x的反正切弧度值。
    atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
    cos(x)	返回x的弧度的余弦值。
    hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
    sin(x)	返回的x弧度的正弦值。
    tan(x)	返回x弧度的正切值。
    degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
    radians(x)	将角度转换为弧度


Python随机数函数 (random模块中)
    随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
    Python包含以下常用随机数函数：
        choice(seq)	从序列的元素中随机挑选一个元素，比如 random.choice(range(10))，从0到9中随机挑选一个整数。
        randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
        random()	随机生成下一个实数，它在[0,1)范围内。
        seed([x])	改变随机数生成器的种子 seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
        shuffle(lst)	将序列的所有元素随机排序
        uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。   


Python数学常量
    pi	数学常量 pi（圆周率，一般以π来表示）
    e	数学常量 e，e即自然常数（自然常数）。
"""


import cmath
import math
import random

print(f"math : {dir(math)}")
print(f"cmath : {dir(cmath)}")
print(f"random : {dir(random)}")



print("cmath.sqrt(-1) : ", cmath.sqrt(-1))
print("cmath.sqrt(9) : ", cmath.sqrt(9))
print("cmath.sin(1) : ", cmath.sin(1))
print("cmath.log10(100) : ", cmath.log10(100))
print("cmath.sin(45): ", cmath.sin(45))

print("math.sin(45): ", math.sin(45))

