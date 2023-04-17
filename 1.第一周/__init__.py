# 2.使用 * 号打印一个三角形
for i in range(1, 8):
    for j in range(1, 8-i):
        print(" ", end="")
    for j in range(1, i+2):
        print(j, end=" ")
    print()

