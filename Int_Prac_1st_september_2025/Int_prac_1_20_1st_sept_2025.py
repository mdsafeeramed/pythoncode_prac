# 1) Reserve the given string using inbuilt modules.
mystring = "abcdefgh"
mystring = mystring[::-1]
print(f"Question 1 answer is : {mystring}")
# 2) Replace the single character with replace inbuilt command
mystring = "Happily life"
mystring = mystring.replace("f", "v")
print(f"Question 2 answer are : ")
print(f"    with inbuilt command : {mystring}")
# b) Write code without using inbuilt command
mystring = "Happily life"
mystring= list(mystring)
for x in range(len(mystring)):
    if mystring[x] == "f":
        mystring[x] = "z"
mystring = "".join(mystring)
print(f"    without inbuilt command: {mystring}")

# 3) Change all ‘s’ characters in the given string
mystring2 = "Sam is learning"
mystring2 = list(mystring2)
for x in range(len(mystring2)):
    if mystring2[x] == "S":
        mystring2[x] = "z"
mystring2 = "".join(mystring2)
print(f"Question 3 answer is : {mystring2}")

# 4) Change all ‘s’ characters in the given string using replace inbuilt module.
mystring2 = "Sam is learning"
mystring2 = mystring2.replace("S", "Y")
print(f"Question 4 answer is : {mystring2}")

# 5) Write a function to reverse the string without using inbuilt reverse function.
mystring = "Geeksforgeeks"
def rev_strin(mystr:str):
    mynew= ""
    for x in mystr:
        mynew = x + mynew
    return mynew

res5 = rev_strin(mystring)
print(f"Question 5 answer is : {res5}")

# 6) Write a function to reverse the words without using inbuilt reverse function.
mystring = "I am Studying"
def rev_words(mystr:str):
    mynew = ""
    for x in mystr.split(" "):
        mynew = x + " " + mynew
    return mynew

res6 = rev_words(mystring)
print(f"Question 6 answer is : {res6}")

# 7) Write a function to get Index number for each character in given string(normal)
mystring = "abcdefgh"
def ind_value(mystr:str):
    mynew= []
    for x in range(len(mystr)):
        mynew.append((mystr[x], x))
    return mynew

res7 = ind_value(mystring)
print(f"Question 7 answer is : {res7}")

# 8) a) Write a function to get Index number for each character in given string in to tuple in list.
def index_num(mystr:str):
    myres= []
    for x in range(len(mystr)):
        myres.append((x, mystring[x]))
    return myres

res8 = index_num(mystring)
print(f"Question 8 answer are : ")
print(f"    a answer is : {res8}")
#    b) Using inbulit command enumerate function
mystring5 = enumerate(mystring)
print(f"    b answer is: {mystring5}")
#    c) enumerate using for loop
mystring = "abcdefgh"
myres = []
for x, cha in enumerate(mystring):
    myres.append((x, cha))
print(f"    c answer is : {myres}")

# 9) Write a function for fizzbuzz scenario.
myrange = list(range(1, 31))

def fizzbuzz(myrange:list):
    myres= []
    for x in myrange:
        if x % 5 == 0 and x % 3 == 0:
            myres.append("FIZZBUZZ")
        elif x % 3 == 0:
            myres.append("FIZZ")
        elif x % 5 == 0:
            myres.append("BUZZ")
        else:
            myres.append(x)
    return myres

res9 = fizzbuzz(myrange)
print(f"Question 9 answer is : {res9}")

# 10) Write a function to reverse the list
mylist= [1, 2, 3, 4, 5]
def rev_list(mylist:list):
    myres = []
    for x in mylist:
        myres.insert(0, x)
    return myres

res10 = rev_list(mylist)
print(f"Question 10 anwser is : {res10}")

# 11) Write a function to reverse the tuple in list.
mylist = [(1,2), (1, 3), (1, 4)]
def rev_tup_list(mylist:list):
    myres= []
    for x in mylist:
        myres.insert(0, x)
    return myres

res11 = rev_tup_list(mylist)
print(f"Question 11 answer is : {res11}")

# 12) Write a function to reverse the tuples in tuple but result should be in list in tuples.
myvalues = ((1, 2), (1, 3), (1, 4))
def rev_tups(mylist:list):
    myres = []
    for x in mylist:
        myres.insert(0, x)
    return myres

res12 = rev_tups(myvalues)
print(f"Question 12 answer is : {res12}")
# 13) reverse list using inbuilt reverse command
myval = [1, 2, 3, 4, 5]
myval.reverse()
print(f"Question 13 answer is : {myval}")

# 14) concatenate or add the two list together using extend inbuild command.
myval1= ["apple", "banana", "grapes"]
myval2 = [1, 2, 3, 4, 5]
myval1.extend(myval2)
print(f"Question 14 answer is : {myval1}")

# 15) get the index number from the list using inbuilt comand index
myval1= ["apple", "banana", "grapes"]
myres = myval1.index("banana")
print(f"Question 15 answer is : {myres}")

# 16) Clear the list means empty the list using clear inbuilt method
myval2 = [1, 2, 3, 4, 5]
myval2.clear()
print(f"Question 16 answer is : {myval2}")
# 17) remove the specific element from the list using inbuilt command pop (position number or index number)
myval1= ["apple", "banana", "grapes"]
myval1.pop(2)
print(f"Question 17 answer is : {myval1}")
# 18) removes the first item with the specified value fron list using inbuilt command remove (specfied value/name)
myval1= ["apple", "banana", "grapes"]
myval1.remove("banana")
print(f"Question 18 answer is : {myval1}")
# 19) Return the number of times the value appears in the list using inbuilt command count
myval1= ["apple", "banana", "grapes", "apple"]
myres = myval1.count("apple")
print(f"Question 19 answer is : {myres}")
# 20) merge Two equal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e']
mylist2 = [0, 1, 2, 3, 4]
max1 = max(len(mylist1), len(mylist2))
myres= []
for x in range(max1):
    myres.append((mylist1[x], mylist2[x]))
print(f"Question 20 answer is : {myres}")
