# 拼接字符串的方法

# 1. 使用+拼接字符串
print("李白", "青莲居士")
print("李白" + "青莲居士")
name = "杜甫"
hao = "草堂居士"
print(name + hao)
n = "456"
m = "123"
print(n + m)
number = 456123
print("字符串" + str(number))
# 2.使用占位符 %s, %d, %f
book = "钢铁是怎样炼成的"
publish_year = 1933
price = 26.5
print("书名：%s, 出版日期：%d, 价格: %.2f" % (book, publish_year, price))
# 3. 使用format(), 函数拼接字符串， 在拼接的位置写{}
# 1）"{}" .format()
print("{} - {} - {}" .format(book, publish_year,  price))
# 3) 在{}中写入一个形参，在format()中用 形参=实参 进行传值
print("{pub}-{book}-{price}" .format(pub=publish_year, book=book, price=price))

# 4) 特别简单的用法，在字符串前添加f，{}直接写变量
print(f"{book} {publish_year }  {price}")











