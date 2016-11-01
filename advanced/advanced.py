#迭代
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
# 	print(key)
# for value in d.values():
# 	print(value)
# for k,v in d.items():
# 	print(k,v)

# from collections import Iterable
# print(isinstance('abc', Iterable))

# for i, value in enumerate(['A', 'B', 'C']):
# 	print(i,value)

# for x, y in [(1, 1), (2, 4), (3, 9)]:
# 	print(x,y)

# #列表生成式
# list(range(1, 11))
# #计算结果生成列表
# [x * x for x in range(1, 11)]
# #增加条件
# [x * x for x in range(1, 11) if x % 2 == 0]
# #全排列
# [m + n for m in 'ABC' for n in 'XYZ']
# #当前目录下文件和目录
# import os
# [d for d in os.listdir('.')]
# #list中所有字符串变小写
# L = ['Hello', 'World', 'IBM', 'Apple']
# [s.lower() for s in L]

#斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# fib(15)

#杨辉三角
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0);
#         L = [L[i-1] + L[i] for i in range(len(L))]
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# from collections import Iterable
# from collections import Iterator
# print(isinstance([], Iterable))
# print(isinstance(iter([]), Iterable))
# print(isinstance(iter([]), Iterator))


# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# #字符串转float
# def str2float(s):
#    def fn(x, y):
#         return x * 10 + y    
#     def str2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     s1 = s.split('.')   # 字符串方法，分个字符串
#     s2 = s1[0] + s1[1]  # 字符串转小数点无非只有2个参数，可以使用+号把字符串连接起来
#     s3 = 10 ** len(s1[1])   # 用10乘以小数点后面几位数的次冥
#     return reduce(fn, map(str2num, s2)) / s3

# print('str2float(\'123.456\') =', str2float('123.456'))