# # z= {"x":{3:6},"y":{5:8}}
# # z["x"] = {4:4}
# # def f(x,y):
# #     # print("第一个 %s 第二个%s" % (x,y))
# #     print(x,y)  #形参要与键名称一一对应    *代表接收的意思
# # if __name__ == "__main__":
# #     print (__name__)
# #     f(**z)
# # elif __name__ == "xdf":
# #    print (__name__)
# s = "^abb xabbbbx xabx  xabbx xax xbx x_x xAx x0x x12341341214134x x22x x3x x33x x$4x x$x x333x xx"
# # findall(string[, pos[, endpos]])在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# res = r"x"
# res = r"^x"
# res = r"x$"
# res = r"x[a-zA-Z0-9]x"
# res = r"x[^3]x"
# res = r"x[4$]x"  #元字符在[]里面无效
# res = r"\^abc"
# res = r"x\dx"
# res = r"x\wx"  #[a-zA-Z0-9_]
# res = r"x\d{3}x"
# res = r"x\d{1,2}x"
# res = r"x\d*x"
# res = r"x\d+x"
# res = r"x\d?x"
# res = r"x..x"   # 匹配任意所有单个字符,匹配几个字符就有几个点。
# res = r"xab+?" #非贪婪模式  若加问号？变为非贪婪模式  ？后面不能加字符
# # 正则表达式中用于表示匹配数量的元字符如下：
# # ? 　　重复0次或1次，等同于{0,1}
# # *　　重复0次或更多次，等同于{0,}
# # +　　重复1次或更多次，等同于{1,}
# # {n,} 重复n次及以上
# # 上面的表示匹配次数的元字符分为贪婪型和懒惰型2种类型。其表达式分别如下。
# # 贪婪型      懒惰型
# # *　　　　　   *?
# # +　　　　     +?
# # {n,} 　　 　{n,}?
# # 贪婪型的匹配会去抓取满足匹配的最长的字符串，这个也是正则表达式的默认的模式。当我们不需要最长的匹配的时候就需要使用懒惰模式。
# import re
# print (re.findall(res,s))
# # pr = re.findall(r"[t,w]h","https://docs.python.org/3/whatsnew/3.6.html")
# # print (pr)
#
#
#
# name = input("请输入文件名：")
# try:
#     f = open("12345.py")
#     print (uu)
# except FileNotFoundError:
#     print ("找不到文件")
# except NameError:
#     print ("测试一下")
# finally:
#     print ("ok")
# if name == "12345.py":
#     raise NameError("一切正常，多余的操作!")

import pymysql
# 打开数据库连接
dbo = pymysql.connect("127.0.0.1","root","123456","world" )
cur = dbo.cursor()
# cur.execute("insert into test values (1,'jack','1')")
# dbo.commit()
sql1 = "insert into test values (%s,%s,%s)"
# cur.execute(sql,(2,"mick","0"))
# dbo.commit()
# cur.executemany(sql1,[(3,"mickey","0"),(4,"key","0"),(5,"mi","0")])
# dbo.commit()

# cur.execute("delete from test where id >= 3")
# dbo.commit()

# cur.execute("update test set sex = 1 ")
# dbo.commit()

cur.execute("SELECT * FROM test")
# 使用 fetchone() 方法获取单条数据.
cur.scroll(2,"absolute")
# data = cur.fetchone()
data = cur.fetchmany(cur.execute("SELECT * FROM test"))
# data = cur.fetchmany(3)   从第三行开始
print (data)
dbo.close()





