#day17 Python装饰器
""""""
"""
    装饰器（decorators）是 Python 中的一种高级功能，它允许不修改原有函数或类的代码基础上，动态地修改函数或类的行为；
    装饰器本质上是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
    装饰器的语法使用 @decorator_name 来应用在函数或方法上。
    Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。
    
    装饰器的应用场景：
        日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
        性能分析: 可以使用装饰器来测量函数的执行时间。
        权限控制: 装饰器可用于限制对某些函数的访问权限。
        缓存: 装饰器可用于实现函数结果的缓存，以提高性能
        
    基本语法：
      无参数装饰器
        # 定义装饰器
        def decorator_function(original_function):
            def wrapper(*args, **kwargs):
                # 这里是在调用原始函数前添加的新功能
                before_call_code()
               
                result = original_function(*args, **kwargs)
               
                # 这里是在调用原始函数后添加的新功能
                after_call_code()
               
                return result
            return wrapper #warpper内部函数
            
        # 使用装饰器 -- 通过@符号，应用在函数定义之前
        @decorator_function
        def target_function(arg1, arg2):
            pass  # 原始函数的实现  
            
        #解析：
            decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个内部函数 wrapper，在 wrapper 函数内部，你可以执行一些额外的操作，然后调用原始函数 func，并返回其结果。

            1.decorator_function 是装饰器，它接收一个函数 original_function 作为参数。
            2.wrapper 是内部函数，它是实际会被调用的新函数，它包裹了原始函数的调用，并在其前后增加了额外的行为。
            3.当我们使用 @decorator_function 前缀在 target_function 定义前，Python会自动将 target_function 作为参数传递给 decorator_function，
            然后将返回的 wrapper 函数替换掉原来的 target_function。
            
        # 调用装饰器，装饰后的函数
            target_function(arg1,arg2); -- 每次调用target_function，实际上是调用装饰后的函数
            
    带参数的装饰器
    
    类装饰器
        除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数
"""

"""
    repeat 函数是一个带参数的装饰器，它接受一个整数参数 n，然后返回一个装饰器函数。
    该装饰器函数内部定义了 wrapper 函数，在调用原始函数之前重复执行 n 次。
    因此，greet 函数在被 @repeat(3) 装饰后，会打印三次问候语
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")



"""
    类装饰器
"""
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前/之后执行的代码
        result = self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        return result


@DecoratorClass
def my_function():
    pass

if __name__ == '__main__':
    print("程序在自身运行.")
else:
    print("程序在另一个模块运行.")
