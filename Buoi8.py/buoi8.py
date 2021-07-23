# # append:
# lst = [1,2,3,4,5,6]
# lst.append(7)
# lst.append(8)
# print(lst)

# # modify:
# lst[1] = 20
# print(lst)

# # Tupple:(immutable): ()
# tpl= (1,2,3,4)
# print(tpl)

# weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# # dictionary: {}
# info_lst= [("name", "Duc Anh"), ("age", 17), ("gender", "male")]
# info_dict = dict(info_lst)
# print(info_dict)
# info = {"name": "Duc Anh", "age": 17, "gender": "male"}
# print(info["name"])
# info["age"] = 18
# print(info["name"])

# stock_left = {"acer": 21, "apple": 30, "dell": 90, "asus": 17}
# print(stock_left["asus"])

# check dict:
# dic = {
#     'name':'duc',
#     'age':99
# }

# for key in dic:
#     print(dic[key])

# for value in dic.values():
#     print(value)

# for key, value in dic.items():
#     print(key, value)

# key = 'age'
# dic[key] += 1
# print(dic[key])

# ex1:
def check_appearance(lst):
    dic ={}
    for i in range(len(lst)):
        key = lst[i]
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    return dic

lst= [1,2,2,3,3,3]
check= check_appearance(lst)
print(check)