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

def choicex(x):
    choicex = int(input("Nhập 1 để sắp xếp tăng dần, 2 để sắp xếp giảm dần: "))
    while(choicex != 1 and choicex != 2):
        choicex = int(input("Nhập 1 để sắp xếp tăng dần, 2 để sắp xếp giảm dần: "))

    if (choicex == 1):
        print("Dữ liệu của mảng sau khi sắp xếp tăng dần:")
        print(tangdan(x))
    else:
        print("Dữ liệu của mảng sau khi sắp xếp giảm dần:")
        print(giamdan(x))

def main():
    lim = int(input("Nhập số phần tử cần tạo: "))
    b = int(input("Nhập giới hạn giá trị của phần tử: "))
    num = taodulieu(lim, b)

    print("Ban đầu:")
    print(num)

    choicex(num)
if __name__== "__main__":
    main()