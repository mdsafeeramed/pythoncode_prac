# 31) For loop to convert Dictionary items in form of tuples in list
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
mydict_list = []
for x in mydict.items():
    mydict_list.append(x)

print(f"Question 31 answer is : {mydict_list}")
# 32) For loop to convert Dictionary only keys in form of list
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
mydict_list = []
for x in mydict.keys():
    mydict_list.append(x)

print(f"Question 32 answer is : {mydict_list}")
# 33) For loop to convert Dictionary only values in form of list
mydict = {"key1": "java", "key2": "python", "key3": "C++"}

mydict_list = []
for x in mydict.values():
    mydict_list.append(x)

print(f"Question 33 answer is : {mydict_list}")

# 34) Add new key and values to the existing dictionary.
mydict = {"key1": "java", "key2": "python", "key3": "C++"}
mydict["key4"] = ".Net"
print(f"Question 34 answer is : {mydict}")

# Function
# 35) Write a function to add given number (*args)

def add_sum(*args):
    total = 0
    for x in args:
        total = x + total
    return total

res35 = add_sum(1, 2, 3, 4, 5)
print(f"Question 35 answer is : {res35}")

# 36) Write a function for even numbers.
mrange = range(1, 21)
def num_even(mcode):
    myresult = []
    for x in mcode:
        if x % 2 == 0:
            myresult.append(x)
    return myresult

res36 = num_even(mrange)
print(f"Question 36 answer is : {res36}")

# 37) Write a function for odd numbers

mrange = range(1, 21)
def num_odd(mcode):
    myresult = []
    for x in mcode:
        if x % 2 != 0:
            myresult.append(x)
    return myresult

res37 = num_odd(mrange)
print(f"Question 37 answer is : {res37}")

# 38) Write a function to take **kwargs and perform unpacking of dictionary

def dict_kwargs(**kwargs):
    myunpack = []
    for x in kwargs.items():
        myunpack.append(x)
    return myunpack

res38 = dict_kwargs(key1="test1", key2="test2")
print(f"Question 38 answer is : {res38}")


