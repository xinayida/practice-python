# import logging
# logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# # logging.info('n = %d' % n)
# print(10 / n)


import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)