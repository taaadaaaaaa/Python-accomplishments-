# chèn string:
# age = 18
# full_name = "Tran" + " " + "Duc" + " " + 'Anh'
# print(full_name)
# print("My name is " + str(full_name)+ str(age) + "tuoi")

# tính toán
# a = 3
# a**=3
# print(a)

# so sánh:
# i=6
# z=9
# print(i==z)

# class_list=["quan", "duc anh", "minh"]
# print(class_list)
# print(type(class_list))
# print(len(class_list))

# hàm slice:
# danh_sach_lop="tran duc anh"
# ten_dem=danh_sach_lop[5:-4]
# print(ten_dem)

# dùng vòng lặp while:
# gpa=8.0
# while gpa < 8.5:
#     print("Nam nay không được chơi game")
#     gpa += 0.1
# print("Nam nay được chơi game rồi")

# dùng vòng lặp while (vdu 1):
# number_of_times = int(input("Enter a number from 0 to 10"))
# while 0 < number_of_times < 11:
#     print("Tran Duc Anh")
#     number_of_times -= 1
#     print("Done")

# dùng vòng lặp while (vdu 2):
# limit=int(input("Enter a number from 0 to 10"))
# number=0
# sum=0
# while number <= limit and -1 < limit < 11:
#     sum += number
#     number += 1 
#     print(sum)

# dùng vòng lặp while:
# f3=int(input("Enter a number between 1 and 10")
# f1=0
# f2=1
# while f2 <= f3 and f3 < 11:
#     f3 = f1 + f2
#     f1=f2
#     f2=f3
#     f3 -= 0
#     print(f3)

# dùng vòng lặp for:
# a = [1,2,3,4,5,6,7]
# for symbol in a:
#     print(number)

# dùng vòng lặp for (vdu 1):
# for symbol in a:
#     print("hello")

# dùng vòng lặp for (vdu 2):
# a = [1,2,3,4,5,6,7]
# sum = 0
# for number in a:
#     sum += number
#     print(sum)

# dùng vòng lặp for (vdu 3):
# a = [2.4.6,8,10]
# length = 0
# for number in a:
#     length += 1
#     print(length)

# dùng vòng lặp for range:
# print(list(range(6)))
# print(list(range(-3,8,1)))
# print(list(range(3,-4,-1)))
# for i in range(6):
#     print(i)

# dùng vòng lặp for range(vdu 1):
# animals=["cow", "sheep", "chicken", "salmon"]
# for i in range(len(animals)):
#     print(animals[i])

# dùng vòng lặp for range (vdu 2):
for number in range(1,7,1):
    print(list(range(1,number)))

# list= [10,20,30,40,50]
# for number in range(-1,-6,-1):
#     print(list[number])