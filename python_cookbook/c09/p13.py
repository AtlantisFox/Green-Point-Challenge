
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



if __name__ == '__main__':

    # Test.noinstance()

    Test.singleton()







