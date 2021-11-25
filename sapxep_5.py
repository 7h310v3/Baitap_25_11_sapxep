import random
num = []
tangdan = []
giamdan = []

lim = int(input("Nhập số phần tử cần tạo: "))
b = int(input("Nhập giới hạn giá trị của phần tử: "))

#Tạo dữ liệu
count = 0
while(count < lim):
    num.append(int(random.uniform(0, b)))
    count += 1

#Tăng dần
for i in range (0, len(num)-1):
    for j in range (i+1, len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]
    tangdan.append(num[i])

#Giảm dần
for i in range (0, len(num)-1):
    for j in range (i+1, len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
    giamdan.append(num[i])

#Ban đầu
print("Ban đầu:")
print(num)

#Chọn
choicex = int(input("Nhập 1 để sắp xếp tăng dần, 2 để sắp xếp giảm dần: "))
while(choicex != 1 and choicex != 2):
    choicex = int(input("Nhập 1 để sắp xếp tăng dần, 2 để sắp xếp giảm dần: "))

if(choicex ==  1):
        print("Dữ liệu của mảng sau khi sắp xếp tăng dần:")
        print(tangdan)
else:
    print("Dữ liệu của mảng sau khi sắp xếp giảm dần:")
    print(giamdan)

