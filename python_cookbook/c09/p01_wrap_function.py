import time
from functools import wraps

"""
包装器, 计时
"""


# 计时
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    """
    count down from n
    """
    while n > 0:
        n -= 1

# --------------------------------------------

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y


if __name__ == '__main__':
    countdown(100000)

    # 使用 @wraps编写装饰器时, 能够复制被装饰函数的元信息
    print('name ', countdown.__name__)
    print('doc', countdown.__doc__)

    # 使用 @wraps编写的装饰器, 能通过属性__wrapped__ 直接访问被包装函数
    countdown.__wrapped__(100)


    print(add(2, 3))
    # Decorator 1
    # Decorator 2


    print('\n')

    print(add.__wrapped__(2, 3))
    # Decorator 2
    #



