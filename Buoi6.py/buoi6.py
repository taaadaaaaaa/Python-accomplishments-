# tao ham - define function:
# a = 5
# b = 8
# result = a > b
# print(result)

# ly thuyet:
# def greater_than(a, b): # argument
#     result = a > b
#     return result

# y = greater_than(5, 8)
# print(y)

# ex1:
# def number_of_days(month):
#     if month in [1,3,5,7,8,10,12]:
#         result = 31
#     elif month == 2:
#         result = 28
#     else:
#         result = 30
#     return result
# ngay=input("Enter a random month here: ")
# y=str(number_of_days(ngay))
# print(y+" days")

# ex2:
# def what_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         year = True
#     else:
#         year= False
#     return year

# year= int(input("Nhap so nam: "))
# y = what_year(year)
# print(y)

# ex3:
def reverse_string(string):
    string_end= string [::-1]
    return string_end

print(reverse_string(input("Nhap một chuỗi vào đây: ")))

