#day22 Python3错误和异常
""""""

"""
    Python 有两种错误很容易辨认：语法错误和异常。
    Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    
    语法错误
        Python 的语法错误或者称之为解析错误
    异常
        即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
    异常处理
        异常处理是程序运行中出现异常时，程序的正常流程被打乱，程序的执行被迫中断，并转而执行异常处理代码。
        Python 提供了 try/except 语句来处理异常。
        try :
            可能发生异常的语句
        except 异常类型 :
            异常发生时执行的代码
        except (异常类型1, 异常类型2,...) : 
            异常发生时执行的代码
        except (异常类型1, 异常类型2,...) : 
            异常发生时执行的代码
        except: （忽略异常名称，将其当作通配符使用）
            其他异常类型发生时执行的代码
        else:[可选] 
            异常没有发生时执行的代码
        finally:[可选]
            无论异常是否发生，都会执行的代码。
            
        如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中；
        如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。
        
    抛出异常
        raise 语句用于手动触发异常。raise 后面可以跟着一个异常类型，或者一个异常实例。
        
    用户自定义异常
        1.程序员可以定义自己的异常类，来表示程序运行中可能出现的错误。
        2.自定义异常类需要继承自 Exception 类。
        3.自定义异常类可以包含一个或多个参数，用于传递异常的相关信息。
        4.当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
        
    定义清理行为 ： finally 子句可以用于定义清理行为，无论异常是否发生，它都会被执行。
    预定义的清理行为 ： Python 提供了一些预定义的清理行为，比如文件关闭、释放资源等。   
                    关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
                        with open("myfile.txt") as f:
                            for line in f:
                                print(line, end="")
                    以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
"""