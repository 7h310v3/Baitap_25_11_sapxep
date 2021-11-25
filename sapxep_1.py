num = [2, 5, 9, 8, 4, 3, 7, 3, -5]

def tangdan(num):
    for i in range (0, len(num)-1):
        for j in range (i+1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
    return num

def main():
    print("Ban đầu:")
    print(num)

    print("Dữ liệu của mảng sau khi sắp xếp:")
    print(tangdan(num))


if __name__== "__main__":
    main()