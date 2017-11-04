import time
from functools import wraps

"""
为类和静态方法提供装饰器
"""

# a simple decorator that calc pragrame  time
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r
    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > n:
            n -= 1


if __name__ == '__main__':
    s = Spam()
    s.instance_method(1000000)

    Spam.class_method(1000000)

    Spam.static_method(1000000)