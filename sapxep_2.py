def nhapphantu(lim):
    count = 0
    l1 = []
    while(count < lim):
        l1.append(int(input("Nhập phần tử: ")))
        count += 1
    return l1

def sapxep(x):
    for i in range (0, len(x)-1):
        for j in range (i+1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x

def main():
    lim = int(input("Nhập số phần tử: "))
    num = nhapphantu(lim)

    print("Ban đầu:")
    print(num)

    print("Dữ liệu của mảng sau khi sắp xếp:")
    print(sapxep(num))

if __name__== "__main__":
    main()