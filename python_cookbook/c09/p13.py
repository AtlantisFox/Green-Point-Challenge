import weakref


# 无实例
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Can not instantiate directly')


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok', x)


# 单例
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class SingleSpam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam (singleton)')


# 缓存实例
class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class CacheSpam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

# -------------
class Test(object):

    # 无实例
    @staticmethod
    def noinstance():
        Spam.grok(41)
        s = Spam()

    # 单例
    @staticmethod
    def singleton():
        a = SingleSpam()
        b = SingleSpam()
        if a == b:
            print('T')
        else:
            print('F')

    # 缓存
    @staticmethod
    def cache():
        a = CacheSpam('alpha')
        b = CacheSpam('beta')
        c = CacheSpam('alpha')

        if a is b:
            print('a is b')
        else:
            print('a is not b')

        if a is c:
            print('a is c')
        else:
            print('a is not c')



if __name__ == '__main__':

    # Test.noinstance()

    # Test.singleton()

    Test.cache()






