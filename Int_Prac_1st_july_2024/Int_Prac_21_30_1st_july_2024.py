# 21) Find the minimum number in list without max function.
mylist_num = [10, 100, 5,  20, 60]
min1 = mylist_num[1]
for x in mylist_num:
    if x < min1:
        min1 = x
print(f"question 21 answer is : {min1}")

# 22) Find the second maximum number in list without max function
mylist_num = [10, 70, 100, 20, 60]
firstmax = 0
for x in mylist_num:
    if x > firstmax:
        firstmax = x
secondmax = 0
for x in mylist_num:
    if x < firstmax and x > secondmax:
        secondmax = x
print(f"Question 22 answer : {secondmax}")

# 23) Find the maximum number in list without max function but using sort and indexing inbuilt/ slicing command.
mylist_num = [10, 100, 20, 60]
mylist_num.sort()
print(f"Question 23 answer is : {mylist_num[-1]}")

# 24) Find the second maximum number in list without max function but using sort and indexing/slicing inbuilt command.
mylist_num = [10, 100, 20, 60]
mylist_num.sort()
print(f"Question 24 answer is : {mylist_num[-2]}")

# 25) Find maximum value using mAX function inbuilt command
mylist_num = [10, 100, 20, 60]
max1 = max(mylist_num)
print(f"question 25 answer is : {max1}")

# 26) Find minimum value using mIN function inbuilt command
mylist_num = [10, 100, 20, 60]
min1 = min(mylist_num)
print(f"question 26 answer is : {min1}")

# 27) convert List into tuple using tuple inbuilt function.
mylist_con = [1, 2, 3, 4, 5]
mylist_con = tuple(mylist_con)
print(f"Question 27 answer is : {mylist_con}")

# 28) convert List into tuple using for loop.
mylist_con = [1, 2, 3, 4, 5]
mylist_con = tuple(x for x in mylist_con)
print(f"Question 28 answer is : {mylist_con}")

# 29) convert list in to tuple using astric key * and comma ,
mylist_con = [1, 2, 3, 4, 5]
mylist_con = (*mylist_con,)
print(f"Question 29 answer is : {mylist_con}")

# Dictionary
# 30) Basic Dictionary print statements
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
print("Question 30 answer is : ")
print(f"   full output: {mydict}")
print(f"   item output: {mydict.items()}")
print(f"   keys output: {mydict.keys()}")
print(f"   values output: {mydict.values()}")
print(f"   mydict single key output: {mydict['key3']}")

