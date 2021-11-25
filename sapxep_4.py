def enter_num():
    l1 = []
    while True:
        x = input("Dữ liệu cần nhập cho mảng: ").upper()
        print("Bạn có muốn tiếp tục hay không? Nhập n hoặc N để dừng!")
        if x == "N":
            print("Dữ liệu đã nhập thành công")
            break
        l1.append(float(x))
    return l1

def sapxep(x):
    for i in range (0, len(x)-1):
        for j in range (i+1, len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
    print(x)

def main():
    num = enter_num()

    print("Ban đầu:")
    print(num)

    sapxep(num)

if __name__== "__main__":
    main()