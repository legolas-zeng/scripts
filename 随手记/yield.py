# coding=utf-8

'''
如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。
通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取
'''
# 生成器
def read_file(fpath):
   BLOCK_SIZE = 1024
   with open(fpath, 'rb') as f:
       while True:
           block = f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return

# for a in read_file("C:\\Users\Administrator.000\Desktop\\new 4.txt"):
#     print(a)

'''
直接调用生成器函数不会返回结果，而是会返回一个generator对象<generator object read_file at 0x0000019FC5DA8C00>。
'''
# a = read_file("C:\\Users\Administrator.000\Desktop\\new 4.txt")
# print(a)

# 异步生成器

async def read_files(path):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
'''
直接调用异步生成器函数也不会返回结果，会返回一个async_generator对象。
'''
a = read_files("C:\\Users\Administrator.000\Desktop\\new 4.txt")
print(a)
