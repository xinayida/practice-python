# def is_odd(n):
#     return n % 2 == 1

# a = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# print(a)

# def not_empty(s):
#     return s and s.strip()

# a = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# print(a)

#### filter

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列

# # 打印100以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break


#####sorted

#返回函数

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())

#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


#匿名函数
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# f = lambda x: x * x
# print(f(5))

#装饰器
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('before call %s():' % func.__name__)
#         f = func(*args, **kw)
#         print('after call %s():' % func.__name__)
#         return f
#     return wrapper

# # @log('excute')
# @log
# def now():
#     print('2015-3-25')

# now()

# import functools
# def log(text = 'call'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log()
# def go():
#     print('1024')

# @log('eve')
# def gogo():
#     print('1025')

# go()

# gogo()

# import functools

# # 调用方式@log 或者 @log('xxxx')
# def log(args):
#     text = "" if callable(args) else args
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('before ' + text)
#             return func(*args, **kw)
#         return wrapper
#     return decorator(args) if callable(args) else decorator

# # 测试
# @log('xxx')
# def test1():
#     print('func1')

# @log
# def test2():
#     print('func2')

# test1()
# test2()


#偏函数 functools.partial
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# import functools
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))
