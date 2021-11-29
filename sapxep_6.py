import random

def taodulieu(lim, b):
    tao = []
    count = 0
    while(count < lim):
        tao.append(int(random.uniform(0, b)))
        count += 1
    return tao

def tangdan(x):
    for i in range (0, len(x)-1):
        for j in range (i+1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x

def giamdan(x):
    for i in range (0, len(x)-1):
        for j in range (i+1, len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
    return x

def main():
    lim = int(input("Nhập số phần tử cần tạo: "))
    b = int(input("Nhập giới hạn giá trị của phần tử: "))
    num = taodulieu(lim, b)

    print("Ban đầu:")
    print(num)

    print("Dữ liệu của mảng sau khi sắp xếp tăng dần:")
    print(tangdan(num))

    print("Dữ liệu của mảng sau khi sắp xếp giảm dần:")
    print(giamdan(num))

    choicex(num)
if __name__== "__main__":
    main()