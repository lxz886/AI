# 输入函数 print(): 打印输出

# 1. 输出函数
# 1) 输出变量或常量
print("梅花香自苦寒来")
say = "宝剑锋从磨砺出"
print(say)
print("贺俊霖", 17, 1000)
# 2) 每次print都会换行，这是一个参数： end， 默认为 end="\n"
# \n:换行符，让字符串在这个地方另起一行
print("咱们试试\n试试就试试", end="!!!!")
print("看看呗")
"""
\n 这种前面带 \ 后边跟字母或数字，叫做转义字符
\ 会将后边的字母或数字一起转义，赋予其他意义
\t 制表符,相当于一个tab键
\\表示\,使用\取消\的转义效果
"""
print("-----------")
print("姓名：丁程鑫\n年龄：20\n性别：男")

# print("\")
# len():计算字符串长度
print(len(" \ "))
print("\\")
print(len("\\"))
print("蔡文姬\\t瑶\\t大乔\t孙膑")
# 字符串前添加r也可以让字符串的转义字符串不再转义
print(r"姓名：孙膑\n年龄：66\n性别：男")
print("老话说得好：‘世上无难事，只要肯努力！’")
print("老话说得好：\"世上无难事，只要肯努力！\"")
# \u4e00-\u9fa5: 一，龥 所有汉字的编码范围在这个区间
print("\u4e01    \u9fa5")

# 2. input():输入函数，接收来自键盘输入的内容，数据类型是字符串

# name = input("宝，你叫什么名字：")
# print(name)
number = input("请输入您的余额: ")
print(number, type(number))
# 有时候需要数据类型的转换
number = int(number)
print(number, type(number))


















