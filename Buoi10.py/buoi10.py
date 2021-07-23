a = [1,2,3,4,5,6,7]
list1 = [i**2 for i in a]
list2 = [i for i in a if i % 2 == 0]
list3 = [i for i in a if i % 2 == 0 or i % 3 == 0]
list4 = [ i > 4 for i in a]
print(list1)
print(list2)
print(list3)
print(list4)

b = ["a", "b", "c", "aa", "abc", "aaa", "abcd"]
list1 = [ string for string in b if len(string) >= 2]
list2 = [ string for string in b if len(string) == 1]
list3 = [ string.capitalize for string in b]
list4 = [ string.replace("a", "@") for string in b]
list5 = [ string for string in b if string[0] == "a"]
list6 = [ string[0] == "a" for string in b ]
list7 = []
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)

ex1 = lambda a: a**2
ex2 = lambda a: a % 2 == 0 and a < 100
ex3 = lambda list1: sum(list1)
ex4 = lambda a: -1 if a < 0 else 0 if a == 0  else 1
list1= [1,2,3]
print(ex3(list1))
print(ex4(5))