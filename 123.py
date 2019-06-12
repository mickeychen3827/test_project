# # print("asdasdasd")
# #
# # print("asdasdasd")
# """
# print("asdasdasd")
#
# print("asdasdasd")
#
# """
#
# # name="mickey"
# # num = 23
# # sal= 7500.65
# # per=88
#
# # print("我的名字是%s，我的学号是%d，我的工资是%.1f，我的胜率是%d%%" % (name,num,sal,per))
#
# # 非0为真，0为假
# # ret1 = 1 and 2  #第一个为真，接着看第二个，返回第二个结果；第一个为假，直接返回第一个结果。
# # ret2 = 1 and 0
# # ret3 = 0 and 2
# # ret4 = 1 or 2  #第一个为真，返回第一个结果；第一个为假，接着看第二个，返回第二个结果。
# # ret5 = 0 and 2
# # ret7 = not ret2
# # print(ret1,ret2,ret3,ret4,ret5,not ret2,ret7)
# # i = 1
# # while i < 6:
# #     print("*" * i)
# #     i += 1
# #
# # i = 1
# # total = 0
# # while i < 101:
# #     if i % 2 == 0:
# #         total = total + i
# #     i += 1
# # print(total)
# #
#
# # continue跳过本层本次循环    break终止本层本次循环    两层嵌套
# # i = 1
# # while i <= 2:
# #     j=1
# #     while j <= 4:
# #         if j == 3:
# #             j += 1
# #             break  # break  continue
# #         print(j)
# #         j += 1
# #     i += 1
# #
# # i2 = 1
# # while i2 <= 2:
# #     j2=1
# #     while j2 <= 4:
# #         if j2 == 3:
# #             j2 += 1
# #             continue  # break  continue
# #         print(j2)
# #         j2 += 1
# #     i2 += 1
# #
# # def add(a,b):
# #     print("a\t+\tb\t=\t",a+b)
# #     return a + b
# #
# # bdd  = add(11,22)
# # c = bdd + 22
# # print(c)
#
# # 全局变量  局部变量  当两者名字相同的时候，就近原则   全局作用域   局部作用域
# #   Ctrl + Q 就是查看函数文档
# # a = 100
# # def aa(a=300):
#
#    # a = 200
# #    print(a)
# #
# # aa()
#
# # 列表里面的元素，一旦追加、删除、清空都会影响原来的列表！
# #   列表  2种循环遍历  尾部、指定位置追加   尾部删除、指定位置删除、值删除
# # list0 = [[34],12,1,12,2,12,3,[56,67,89,90,4,9],12,[34],12,[56],[34],[32]]
# # print(list0[7:])  #切片
# # for i in list0:
# #    for j in i:
# #       print(j)
# i = 0
# # print(len(list0[i]))
# # while i <len(list0):
# #    j = 0
# #    while j < len(list0[i]):
# #       print(list0[i][j])
# #       j += 1
# #    i += 1
# # list0.append(33)
# # print (list0)
# #
# # list0.insert(0,111)
# # print (list0)
# #
# # list0.pop()
# # print(list0)
# #
# # list0.pop(1)
# # print(list0)
# #
# # # 清除第一次匹配成功的元素,从左往右
# # list0.remove(12)
# # print(list0)
# #
# # list0.clear()
# # print(list0)
#
# # 3个教室，安插任意8个老师
# # import random
# # school = [[],[],[]]
# # teacherlist = []
# # ii=1
# # while ii < 9:
# #    v = 'teacher'+str(ii)
# #    teacherlist.append(v)
# #    ii +=1
# # # print(teacherlist)
# # for teacher in teacherlist:
# #    num = random.randint(0,2)
# #    school[num].append(teacher)
# # print(school)
#
#
# # 字典的遍历
# #
# # dict1 = {"1":11,"2":22,"3":33,"4":44}
# #
# # dict11 = {"1":11,"2":22,"3":33,"4":44}
# # list11  = list(dict.items(dict11))
# # print(dict.keys(dict1))
# # print(dict.values(dict1))
# # print(dict.items(dict1))    dict类型的对象，可以转换为列表对象
# # print(list(dict1.keys()))  #封装类型
# # print(list(dict1.values()))
# # print(list(dict1.items())) #返回的是列表，但是每个元素都是元组
# #
# # for kv in dict1.items():
# #     print(kv[0],":",kv[1])
# # # a = 1
# # # del a
# # # print(a)
# #
# #
# # del dict1["4"]
# # print(dict1)
# #
# # dict1.clear()
# # print(dict1)
# #
# # # del dict11   删除整个字典
# # del list11[0]
# # print(list11)
# #
# # dict2 = {"1":11,"2":22,"3":33,"4":44}
# # i = 0
# # list0 = list(dict2.items())
# # while i < len(list0):
# #     print(list0[i][0],"+",list0[i][1])
# #     i += 1
#
# # f = open('C:\kkk.txt')
# # import os
# # # print(os.getcwd())
# # os.chdir(r"c:\Users\mickey\Desktop")
# # f = open("123123.txt","w")
# # f.write("dsfdfsdfsd")
# #
#
# #
# # t=(1,2,3)
# # l=[1,2]
# # type(t)
# # type(l)
# # print(id(t))
# # print(id(l))
# #
# t=(1,2,3)
# l=[1,2]
# # print(id(t))
# # print(id(l))
# #
# # while 1 in t:
# #     print("YES")
# #     break
# # while 1 in l:
# #     print("NO")
# #     break
# #
# # l[1]= 7
# # print(l)
# #哈希表代表是无序的
# # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# #
# # 我们可以使用 list() 转换来输出列表。
# #
# # 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# # l1=["a","b","c"]
# # l2=[1,2]
# # z = zip(l1,l2)
# # print(list(z))
# #
# # l11,l12=zip(*zip(l1,l2))   # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
# # print(list(l11))
# # print(list(l12))
# # print((l11))
# # print((l12))
#
# # list、tuple、str等类型的数据使⽤for...in...的循环语法从其中依次拿到数据进⾏使⽤，我们把这样的过程称为遍历，也叫迭代。
# # 我们把可以通过for... in ...这类语句迭代读取⼀条数据供我们使⽤的对象称之为可迭代对象（Iterable）
# # 可以使⽤isinstance()判断⼀个对象是否是 Iterable对象：  通过collections模块的Iterable类型来判断
# # 迭代是访问集合元素的⼀种⽅式。迭代器是⼀个可以记住遍历的位置的对象。迭代器对象从集合的第⼀个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# # from collections import Iterable
# # print(isinstance(l11,Iterable))
# # print(isinstance('abc',Iterable)) # str是否可迭代  True
# # print(isinstance(5,Iterable)) # 整数int是否可迭代  False   int整型不是iterable，即int整型不是可以迭代的  for    i    in    100:
# # print(isinstance('5',Iterable)) # str是否可迭代（区分上面的整数）  True
# # for    i    in  "45":
# #     pass
# #
# # dict1={"name":123}
# # print(dict1["name"])
# # name="myname"
# # dict11={name:123}
# # print(dict11["myname"])
# # print(dict11[name])
#
# # 创建字典的三种方法  工厂方法  通过（键，值）这样的序列（列表，元组）对建立
# # items = [('name', 'earth'), ('port', '80')]
# # dict2 = dict(items)
# # dict1 = dict((['name', 'earth'], ['port', '80']))
# # items = (('name', 'earth'), ('port', '80'))
# # dict2 = dict(items)
# # dict1 = dict([['name', 'earth'], ['port', '80']])
# # print(dict2)
# # print(dict1)
# # 字典可以直接加入和更新item，这一点连列表都做不到   list1[key1]=values  直接赋值
# dict1 = {}.fromkeys(('x', 'y','x11','x1'), -1)
# # dict={'x':-1,'y':-1}   内建方法
# dict2 = {}.fromkeys(('xsdsds', 'wefwerwy','x1'))
# # dict2={'x':None, 'y':None}
# # for i in dict1:
# #     print(i,end=": ")
# #     print(dict1[i])
# # print(dict2)
# # print(dict1)
#
# # del dict1["x"]
# # del l[0]
# # # 元组是不能删除
# # print(dict1)
# # print(l)
# #
# # # 在字典和列表中，pop()函数都是删除特定元素，并将删除的元素返回给指定的变量或丢弃,但是有不同，列表是根据位置剔除，字典根据key剔除
# #
# # dict1.pop("y")
# # print(dict1)
# # di = dict(x=1,y=2)
# # print(di)
# # get方法是字典特有，如果没有这个key，不会报错，也可以返回自定义信息
# # print(dict1.get(6,"error"))
# # dict.update(dict1)
# # print(dict2.update(dict1))   #覆盖，然后取并集
# # print(dict1)
# # print(dict2)
# #返回结果都是列表形式
# # dict.keys()
# # dict.values()
# # dict.items()
# # 遍历每个项目的另一种方法是由序列本身的偏移指数（索引）   因为是序列式容器，所以肯定可以用索引
# # s = "jfdksfhksjdfnjksdfn"
# #
# # for v in range(len(s)):
# #     print(s[v])
# # 遍历字典的2种方法
# # d = {"name":111,"sex":323,"sal":3423,"phone":13124342324}
# # for v in d:
# #     print(v,":",d[v])
# #
# # for i,j in d.items() :
# #     print(i,":",j)
# # import time
# # for i in range(1,101):
# #     print(i)
# #     time.sleep(1)
# #     if i == 4:
# #         pass
# #     if i == 5:
# #         print("is five !")
# #         continue
# #     if  i == 6:
# #         while True:
# #             print("如果执行到这段代码，就代表本层本次不执行而已")
# #             # break
# #              # break   如果执行到这段代码，就代表本层本次不执行而已
# #             exit()  #如果执行到这段代码那就代表要退出程序，后面所有代码都不执行。
# # else:
# #     print("it works!")   #如果for循环执行成功，那么就会执行else语句
# #
# # for i in range(3):
# #     print(i)
# #
# #
# # x= tuple([{1:2,3:6},{3:5,6:9}])
# # x= [{1:2,3:6},{3:5,6:9}]
# # x = tuple([{1:{3:6},2:{5:8}}])
# # print(type(x))
# # print(x)
# # x = [{1:2,3:6},{3:5,6:9}]
# # def f(x,y):
# #     print("第一个 %s 第二个%s" % (x,y))
# # f(*x)
# # z= {"x":{3:6},"y":{5:8}}
# # z["x"] = {4:4}
# # def f(x,y):
# #     # print("第一个 %s 第二个%s" % (x,y))
# #     print(x,y)  #形参要与键名称一一对应    *代表接收的意思
# # f(**z)
# #
# # def d(x,*a,**b):
# #     print(x)
# #     print(a)
# #     print(b)
# #
# # d(1,2,3,4,5,y=3,z="uujg")
#
# # import xdf as test
# # test.f(**test.z)
#
# # from xdf import f,z
# # f(**z)
#
# import re
# # 编译正则表达式模式，返回一个对象。可以把常用的正则表达式编译成正则表达式对象，方便后续调用及提高效率。
# r = r"\d{3,4}-?\d{8}"
# re1 = re.findall(r,"010-12345678")
#
# po = re.compile(r)
# p = po.findall("010-12345678")
#
# pk = re.compile(r"python",re.I)
# # print (pk.findall("python PYTHON PyThON"))
#
# p =  pk.match("python-gghjgjg")  #在开始的位置才会返回对象，否则返回none
# p1 =  pk.search("234234v python  jgghjgjg")
# p2 = pk.finditer("123123 python dfgdfgdfg")  #返回一个迭代器，不过不会把所有值都输出,__next__()方法可以读取match对象
# p3 = p2.__next__()
# # print (p.group(0))   #match返回的对象可以用group方法返回被re匹配的字符串
#
# s = r"m..k"
# r = re.sub(s,"jack","mnnk mivk mivc  mick  mnbk ")
# r = re.subn(s,"jack","mnnk mivk mivc  mick  mnbk ")
# # print (r)
#
# p4 = re.split(r"[\+\-\*]","123+456-111*321")
# print (p4)
# a = open(r"C:\Users\mickey\Desktop\test.txt",'r')  #为什么要加r，因为不加的话，地址路径会被理解为转义的意思
# print(a.read())
# a.close()

# b = open(r"C:\Users\mickey\Desktop\test.txt",'r+')  #为什么要加r，因为不加的话，地址路径会被理解为转义的意思
# print(b.read())  光标已经已经读到了末尾，所以后面写的时候直接从最后面写起
# b.write("\n哈哈哈哈哈哈哈哈哈")
# b.close()

# b = open(r"C:\Users\mickey\Desktop\test.txt",'r+')  #为什么要加r，因为不加的话，地址路径会被理解为转义的意思
# # print(b.read())
# b.write("gdfgdfgdfg\n")
# b.close()

# b = open(r"C:\Users\mickey\Desktop\test1.txt",'w')  #为什么要加r，因为不加的话，地址路径会被理解为转义的意思
# print(b.read())  --这个不能读，会报错
# b.write("5456767878676786\n")
# b.close()

# b = open(r"C:\Users\mickey\Desktop\test1.txt",'w+')  #为什么要加r，因为不加的话，地址路径会被理解为转义的意思
# print(b.read())
# b.write("5456767878676786\n")
# b.close()

import os
# os.mkdir('tester')
# os.makedirs('test/TEST/123')
# os.rmdir('tester')
# os.removedirs('test/TEST/123')
os.listdir('.')
print (os.listdir('/'))
os.chdir('/')
print (os.getcwd())


