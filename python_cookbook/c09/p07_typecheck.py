from inspect import signature
from functools import wraps

"""
利用装饰器强制函数上的类型检查
"""

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # if in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)

            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

if __name__ == '__main__':

    spam(1,'hello', 3)

    spam(1, 'hello', 'world')
    # TypeError: Argument z must be <class 'int'>

