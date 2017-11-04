from functools import wraps

"""
将装饰器定义为类的一部分
"""

class A:
    # 装饰器作为实例方法
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # 装饰器作为类方法
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# 作为实例方法
a = A()
@a.decorator1
def spam():
    pass


# 作为类方法
@A.decorator2
def grok():
    pass

if __name__ == '__main__':
    spam()
    grok()