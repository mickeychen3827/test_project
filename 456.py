#import functools
# f = lambda x,y:x*y
# print (f(4,7))
# l = range(1,6)
# g= functools.reduce(f,l)
# print (g)

# from functools import reduce
# g= reduce(lambda x,y:x+y,(1,2,3))
# print (g)

# reduce(function, iterable[, initializer])
# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（列表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

# 字典与函数结合实现switch效果
# x = int(input("x的值："))
# y = int(input("y的值："))
# d = {"+":x+y,"-":x-y,"*":x*y,"/":x/y}
# def f(o,x,y):
#     # d.get(o)(x, y, *a, **b)
#     print (d.get(o))
# f("*",x,y)
# s = "#dfg@dfgdf#g1231#2312#"
#
# print (s.capitalize())
# print (s.replace("2","-",2))
# print (s.split("#",3))
# l = [x for x in range(10)]
# print(list(filter(lambda x : x%2 == 0, l)))  #因为filter返回的是一个iterator，所以输出的时候需要用list进行转换。
#
# filter的主要作用是通过function对iterable(可迭代对象)中的元素进行过滤，并返回一个迭代器（iterator），
# 其中是function返回True的元素。如果function传入None，则返回所有本身可以判断为True的元素。

# l = [x for x in range(0,10)]
# print(list(filter(None, l)))
#
# 输入是0~9，filter的第一个参数传入了None，
# 所以在迭代过程中，0被判断为False从而被过滤，1~9被保留下来。这个方法可以替代for循环的数据拾取。

a =["3","2","4"]
b =["2","3"]
c =["19","5","3"]
print (list(zip(a,b,c)))
# g = map(None,a,b,c)
# print (list(g))
# 如果函数是 None，自动假定一个‘identity’函数,这时候就是模仿 zip()函数，
# l=[1,2,3]
# x=map(None,l)
# print(x)
# 这时候 None 类型不是一个可以调用的对象。所以他没法返回值。TypeError: 'NoneType' object is not callable
# map 和 zip 都可以实现并行遍历的效果
p = map(lambda x, y: y * x, [1, 3, 5, 7, 9], [2, 4, 6, 8])
print (list(p))
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# from functools import reduce
# q = reduce(lambda x, y: y + x,range(4))
# print (q)
# # 在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 functools 模块里，
# # 如果想要使用它，则需要通过引入 functools 模块来调用 reduce() 函数
# print ("*"*50)
# import xdf
# xdf.f(**xdf.z)


