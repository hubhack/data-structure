def A_Decorator(function):
    print('我是 外层A 添加的第一个功能')



    print('我是 外层A 添加的第二个功能')
    return function


@A_Decorator
def C_function(a, b):
    print('最后的结果是：{0}'.format(a + b))
C_function(1, 2)

