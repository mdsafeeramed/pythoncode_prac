# 31) Find the minimum number in list without max function.
mylist_num = [1001, 100, 20, 60, 5, 10]
mini = mylist_num[0]
for x in mylist_num:
    if x < mini:
        mini = x
print(f"Question 31 naswer is : {mini}")
# 32) Find the second maximum number in list without max function
mylist_num = [10, 100, 20, 60]
firstmax = 0
for x in mylist_num:
    if x > firstmax:
        firstmax = x
secondmax = 0
for x in mylist_num:
    if x < firstmax and x > secondmax:
        secondmax = x
print(f"Question 32 answer is : {secondmax}")
# 33) Find the maximum number in list without max function but using sort and indexing inbuilt/ slicing command.
mylist_num = [10, 100, 20, 60]
mylist_num.sort()
print(f"question 33 answer is : {mylist_num[-1]}")
# 34) Find the second maximum number in list without max function but using sort and indexing/slicing inbuilt command.
mylist_num = [10, 100, 20, 60]
mylist_num.sort()
print(f"question 34 answer is : {mylist_num[-2]}")
# 35) Find maximum value using mAX function inbuilt command
mylist_num = [10, 100, 20, 60]
myres35 = max(mylist_num)
print(f"Question 35 answer is : {myres35}")
# 36) Find minimum value using mIN function inbuilt command
mylist_num = [10, 100, 20, 60]
res36 = min(mylist_num)
print(f"Question 36 answer is : {res36}")
# 37) convert List into tuple using tuple inbuilt function.
mylist_con = [1, 2, 3, 4, 5]
myres37 = tuple(mylist_con)
print(f"Question 37 answer is : {myres37}")
# 38) convert List into tuple using for loop.
mylist_con = [1, 2, 3, 4, 5]
myres38= tuple(x for x in mylist_con)
print(f"Question 38 answer is : {myres38}")
# 39) convert list in to tuple using astric key * and comma ,
mylist_con = [1, 2, 3, 4, 5]
myres39 = (*mylist_con,)
print(f"Question 39 answer is : {myres39}")
# Dictionary
# 40) Basic Dictionary print statements
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
print("Question 40 answer are :  ")
print(f"    full dict output: {mydict}")
print(f"    only keys output: {mydict.keys()}")
print(f"    values output: {mydict.values()}")
print(f"    item output: {mydict.items()}")
print(f"    only single key: {mydict['key1']}")

# 41) For loop to convert Dictionary items in form of tuples in list
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
myres41= []
for x in mydict.items():
    myres41.append(x)
print(f"Question 41 answer is : {myres41}")

# 42) For loop to convert Dictionary only keys in form of list
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
myres42= []
for x in mydict.keys():
    myres42.append(x)
print(f"Question 42 answer is : {myres42}")
# 43) For loop to convert Dictionary only values in form of list
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
myres43= []
for x in mydict.values():
    myres43.append(x)
print(f"Question 43 answer is : {myres43}")
# 44) Add new key and values to the existing dictionary.
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
mydict["key4"] = "+net"
print(f"question 44 answer is : {mydict}")
# Function
# 45) Write a function to add given number (*args)
def add_multi_arg(*args):
    total = 0
    for x in args:
        total = x + total
    return total
res45 = add_multi_arg(1, 2, 3, 4, 5)
print(f"Question 45 answer is : {res45}")
# 46) Write a function for even numbers.
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_num(myval:list):
    myres= []
    for x in myval:
        if x % 2 == 0:
            myres.append(x)
    return myres

res46 = even_num(mylist)
print(f"Question 46 answer is : {res46}")
# 47) Write a function for odd numbers
def odd_num(myval:list):
    myres= []
    for x in myval:
        if x % 2 != 0:
            myres.append(x)
    return myres

res47 = odd_num(mylist)
print(f"Question 47 answer is : {res47}")
# 48) Write a function to take **kwargs and perform unpacking of dictionary
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
def kwargs_test(**kwargs):
    myres = []
    for x, y in kwargs.items():
        myres.append(x)
        myres.append(y)
    return myres

res48 = kwargs_test(key1="test1", key2="test2")
print(f"Question 48 answer is : {res48}")
