# sets
set1 = {1,2,"Jeet","4"}
print(type(set1))
print(set1)
print(len(set1))


list1 = [1,2,3,4,5,1,3,4]
set2 = set(list1)
print(set2)
print(len(set2))

set3 = {1,2,3,4,5}
set3.add(6)
set3.add(4)
print(set3)

set3.discard(3)
print(set3)

set3.clear()
print(set3)

set4 = {1,2,3,4,5}
set5 = set4.copy()
print(set5)


#set operations
set6 = {1,2,3,4,5}
set7 = {4,5,6,7,8}
print(set6.union(set7))
print(set6.intersection(set7))
print(set6.difference(set7))
print(set6.symmetric_difference(set7))

#dictionary
dict1 = {"name":"Jeet","age":27,"city":"Pune"}
print(dict1)
print(dict1["name"])
print(dict1.get("age"))

dict1["profession"] = "Engineer"
print(dict1)

dict1.pop("city")
print(dict1)

dict1.clear()
print(dict1)

dict2 = {"name":"Jeet","age":27,"city":"Pune"}
dict3 = dict2.copy()

print(dict3)

for key, value in dict2.items():
    print(key, value)
    
for key in dict2.keys():
    print(key)
    
for value in dict2.values():
    print(value)
    
for i, item in enumerate(dict2.items()):
    print(i, item)
    
list = ["abhishek","jeet","sachin","pratik","abhishek","jeet"]
frequency = {}
for i in list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)