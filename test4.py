"""
 * Project name(项目名称)：Python函数装饰器
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:44
 * Version(版本): 1.0
 * Description(描述)： 
 """


# funA 作为装饰器函数
def funA(fn):
    print("hello world1")
    # fn()  # 执行传入的fn参数
    return "funA"


def funB(fn):
    print("hello world2")
    # fn()  # 执行传入的fn参数
    return "funB"


def funC(fn):
    print("hello world3")
    fn()  # 执行传入的fn参数
    return "funC"


@funA
@funB
@funC
def funD():
    print("funD")


if __name__ == '__main__':
    print(funD)
