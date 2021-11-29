num = []

#Nhập dữ liệu
while True:
    x = input("Dữ liệu cần nhập cho mảng: ").upper()
    print("Bạn có muốn tiếp tục hay không? Nhập n hoặc N để dừng!")
    if x == "N":
        print("Dữ liệu đã nhập thành công")
        break
    num.append(float(x))

#Ban đầu
print("Ban đầu:")
print(num)

#Sắp xếp
for i in range (0, len(num)-1):
    for j in range (i+1, len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

#Sau sắp xếp
print("Mảng sau khi sắp xếp")
print(num)