# 基本类型： int-整型， str-字符串，float-浮点型，bool-布尔型

# 1. str(), 函数，将数据转换成zfc
int1 = 10000
print(int1, type(int1))
sl = str(int1)
print(sl, type(sl))
# 将float转换为str
f1 = 5.235
print(f1, type(f1))
s2 = str(f1)
print(s2, type(s2))
# True 转化字符串，相当于"True"
print(str(True), type(str(True)))
# 2. int(),函数，将数据转化额为整数
# 将float转化为int，取整数位，在一定范围内
f2 = 8.999999999
i1 = int(f2)
print(i1, type(i1))
# 将str转化为int
str1 = "963852"
i2 = int(str1)
print(i2, type(i2))
# ValueError: invalid literal for int() with base 10: ' j456789'
# value: 值，error：错误
# str2 = "j456789"
# i3 = int(str2)
# print(i3, type(i3))
# 将bool转化成int
fa = False
i4 = int(fa)
print(i4, type(i4))


# float(),函数将数据转化为float型
# int转化为float, 带上小数点
print(float("5.666"), type(float(890)))
# str转化为float
print(float("5.666"), type(float(5.666)))
print(float("5")), type(float(5))
# bool转化为float
print(float(True), type(float(True)))

# 4. bool():函数，可以将其他数据转化为布尔值
# 字符串如果是""相当于False,长度大于0是True
string = ""
print(bool(string))
# len():可以计算字符串的长度
print(len(string))
# int转化为bool值，只有0是Flase, 其他都是True
int100 = -10000
print(bool(int100))
print("--------")
# float转化为bool值，只有0.0是False, 其他都是True
f100 = -1.23
print(bool(f100))

































