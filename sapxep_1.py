def nhapphantu(lim):
    count = 0
    lst = []
    while(count < lim):
        lst.append(int(input("Nhập phần tử: ")))
        count += 1
    return l1

def main():
    lim = int(input("Nhập số phần tử: "))
    num = nhapphantu(lim)
    print("Ban đầu:")
    print(num)

    print("Dữ liệu của mảng sau khi sắp xếp:")
    for i in range (0, len(num)-1):
        for j in range (i+1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
    print(num)

if __name__== "__main__":
    main()