"""
 * Project name(项目名称)：Python函数装饰器
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:39
 * Version(版本): 1.0
 * Description(描述)： 
 """


# funA 作为装饰器函数
def funA(fn):
    print("hello world")
    fn()  # 执行传入的fn参数
    return "装饰器函数的返回值"


@funA
def funB():
    print("funB")


if __name__ == '__main__':
    print(funB)
