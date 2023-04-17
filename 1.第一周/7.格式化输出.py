# 格式化字符串
# 输出的到文件中,open():打开一个文件，第一个参数是文件名字，第二参数是操作文件方式，w : write 写入
file1 = open("data.txt", "w")
# "".replace("：", "\n")
print("通知：明天你们好像没课", file=file1)

# 1. %s: 占位符，可以拼接字符串型数据,拼接数据前判断是否为字符串, 不是字符串就转换数据类型,
# str(), 实际上可以拼接任何数据类型
name = "擎天柱"
print("汽车人首领：%s" % name)
number = 12345678901   # int
print("我的电话号码：%s" % number)
age = 19
gender = 86.5
print("%s的年龄是%s， 专业课成绩是%s" % (name, age, gender))
# %6.3s: 里面的6表示拼接的字符串所站的位数， .3 表示取拼接的字符串前三个，如果占的位置不够，
# 会自动变成与字符串本身长度一样的位置
word = "abcdefghijklmn"
print("%s" % word)
print("%.3s" % word)
print("%6.4s" % word)
print("%4.5s" % word)
print(len(word))

# %d: 可以拼接整型数据，拼接数字类型数据可以，字符串不行，纯数字的字符串也会报错
print("肖战电话：%d" % number)
f1 = 6.235
print("拼接小数：%d" % f1)
s1 = "980"
#
# print("拼接字符串：%d" % s1)
# %02d:里面0表示在数位前面不够2的时候前面添加0，2表示占两个位置，当数字大于位置的时候，按数字长度占位
year = 2004
month = 2
day = 8
print("李幸恣的生日：%d-%d-%d" % (year, month, day))
print("李幸恣的生日：%10d-%02d-%02d" % (year, month, day))

# 3. %f:可以拼接浮点型数据,默认保留小数点后6位，不够位，补0
pi = 3.14
print("Π的值是：%f" % pi)
zs = 100
print("拼接整数看看：%f" % zs)

# %.3f: .3表示保留小数点后3位，四舍五入
pai = 3.1415926
print("π后保留2位: %.3f" % pai)

# %x, %o:拼接十六进制，拼接八进制
















