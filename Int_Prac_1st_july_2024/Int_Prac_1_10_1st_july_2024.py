# 1) Reserve the given string using inbuilt modules.
mystring = "abcdefgh"
mystring = mystring[::-1]
print(f"Question 1 answer is : {mystring}")

# 2) Replace the single character with replace inbuilt command
mystring = "Happily life"
mystring = mystring.replace("f", "v")
print("Question 2 answer are: ")
print(f"    Question 2 answer  with inbuilt replace command : {mystring}")

# b) Write code without using inbuilt command
mystring = "Happily life"
mystring_list = list(mystring)
for x in range(len(mystring_list)):
    if mystring_list[x] == "f":
        mystring_list[x] = "z"
mystring = "".join(mystring_list)
print(f"    Question 2 answer without inbuilt command: {mystring}")

# 3) Change all ‘s’ characters in the given string
Mystring2 = "Sam is learning"
mystring = list(Mystring2)
for x in range(len(mystring)):
    if mystring[x] == "S":
        mystring[x] = "Z"
mystring = "".join(mystring)
print(f"Question 3 answer without inbuilt command is : {mystring}")

# 4) Change all ‘s’ characters in the given string using replace inbuilt module.
Mystring2 = "Sam is learning"
mystring = Mystring2.replace("S", "J")
print(f"Question 4 answer with inbuilt replace command: {mystring}")

# 5) Write a function to reverse the string without using inbuilt reverse function.
Mystring = "Geeksforgeeks"

def rev_stri(mycase):
    myrev = ""
    for x in mycase:
        myrev = x + myrev
    return myrev

res1 = rev_stri(Mystring)
print(f"Question 5 answer function without inbuilt reverse function is : {res1}")

# 6) Write a function to reverse the words without using inbuilt reverse function.
Mystring = "I am Studying"

def rev_words(mycode):
    mywords = ""
    for x in mycode.split(" "):
        mywords = x + " " + mywords
    return mywords

res2 = rev_words(Mystring)

print(f"Question 6 answer function without inbuilt reverse function is : {res2}")
# 7) Write a function to get Index number for each character in given string(normal)
Mystring = "abcdefgh"

def my_index(mycode):
    myindex = []
    for x in range(len(Mystring)):
        myindex.append(x)
        myindex.append(Mystring[x])
    return myindex

res3 = my_index(Mystring)
print(f"Question 7 answer is : {res3}")


# 8) Write a function to get Index number for each character in given string in to tuple in list.
Mystring = "abcdefgh"

def my_index_tup(mycode):
    myindex = []
    for x in range(len(Mystring)):
        myindex.append((x, Mystring[x]))
    return myindex

res4 = my_index_tup(Mystring)
print(f"Question 8 answer is : {res4}")

# 9) Write a function for fizzbuzz scenario.
mrange = range(1, 31)
def fuzzbuzz(mycode):
    myresults = []
    for x in mycode:
        if x % 5 == 0 and x % 3 == 0:
            myresults.append("FIZZBUZZ")
        elif x % 3 == 0:
            myresults.append("FIZZ")
        elif x % 5 == 0:
            myresults.append("BUZZ")
        else:
            myresults.append(x)
    return myresults

res5 = fuzzbuzz(mrange)
print(f"Question 9 answer is : {res5}")

# 10) Merge Two equal lists and result should be in list of tuple like [(a, 0)…etc]
Mylist1 = ['a', 'b', 'c', 'd', 'e']
Mylist2 = [0, 1, 2, 3, 4]
max1= max(len(Mylist1), len(Mylist2))
myresult = []
for x in range(max1):
    myresult.append((Mylist1[x], Mylist2[x]))
print(f"Question 10 answer is : {myresult}")