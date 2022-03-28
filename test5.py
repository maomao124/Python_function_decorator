"""
 * Project name(项目名称)：Python函数装饰器
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:49
 * Version(版本): 1.0
 * Description(描述)： 
 """
import functools
import time


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('--[函数"%s"执行时间：%.4f ms]--' % (func.__name__, (end - start) * 1000))
        return res

    return wrapper


@log_execution_time
def f1():
    time.sleep(0.1)


@log_execution_time
def f2():
    print("hello")
    time.sleep(0.2)


@log_execution_time
def f3():
    print("hello")


if __name__ == '__main__':
    f1()
    f2()
    f3()
