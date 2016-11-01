# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# 如果默认参数是可变对象，重复调用时参数会记录下来之前的修改结果
# def add_end(L=[]):
#     L.append('END')
#     return L

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print(add_end())
# print(add_end())
# print(add_end(['a']))
# print(add_end())
# print(add_end())

#递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# result = fact(5)
# print(result)

#汉诺塔
def move(n, a, b, c):
    if n==1:
       print(a,'-->',c)
       return 
    move(n-1,a,c,b)
    print(a, '-->', c)
    move(n-1,b,a,c)

move(5,'A','B','C')