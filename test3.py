"""
 * Project name(项目名称)：Python函数装饰器
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:40
 * Version(版本): 1.0
 * Description(描述)： 
 """


def funA(fn):
    # 定义一个嵌套函数
    def say(args):
        fn(args)
        print("funA:", args)
        # fn(args)

    return say


@funA
def funB(args):
    print("funB:", args)


if __name__ == '__main__':
    funB(123)
