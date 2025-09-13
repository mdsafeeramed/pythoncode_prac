# 61) I/O file using with open.
with open("1st_sept_2025.txt", mode='w+') as saf:
    saf.writelines("Learning python1 \n")

with open("1st_sept_2025.txt", mode='a+') as saf:
    saf.writelines("Learning python2 \n")

with open("1st_sept_2025.txt", mode='r+') as saf:
    content = saf.readlines()

print(f"Question 61 answer is : {content}")

# NOTES:
# re.compile
# The re.compile() method in Python is used to compile a regular expression pattern into a regex object.
# Compiling a pattern makes it more efficient when we need to use the same pattern several times,
# as it avoids re-compiling the pattern each time.

# r raw string
# An ‘r’ before a string tells the Python interpreter to treat backslashes as a literal (raw) character.
# Normally, Python uses backslashes as escape characters.
# Prefacing the string definition with ‘r’ is a useful way to define a string where you need the backslash to be an
# actual backslash and not part of an escape code that means something else in the string.

# re.search
# re.search() function scans through a string, looking for the first location where the regular expression pattern produces a match.
# It returns a match object if a match is found, otherwise returns None.

# re.findall
# re.findall() function returns all non-overlapping matches of a pattern in a string as a list of strings.
# If the pattern has capturing groups, it returns a list of tuples.

# 62) Write a class to regexp using re.findall
mystring1 = "This the IP address 10.129.108.212, 10.129.108.213, 10.129.108.214, 10.129.108.212"
import re
res62 = re.findall(r'\d+.\d+.\d+.\d+', mystring1)
print(f"Question 62 answer is : {res62}")

# 63) Write a class to regexp using re.findall and re.compile.
mystring1 = "This the IP address 10.129.108.212, 10.129.108.213, 10.129.108.214, 10.129.108.212"
pat1= re.compile(r'\d+.\d+.\d+.\d+')
res63 = re.findall(pat1, mystring1)
print(f"Question 63 answer is : {res63}")
# 64) Write a class to regexp using re.search, re.compile using and output span, group..etc
# note: group, span is available only when we use re.search command
mystring1 = "This the IP address 10.129.108.212, 10.129.108.213, 10.129.108.214"
pat1= re.compile(r'(\d+).(\d+).(\d+).(\d+)')
res64 = re.search(pat1, mystring1)
print(f"Question 63 answer are : ")
print(f"    Full ouput : {res64}")
print(f"    SPAN : {res64.span()}")
print(f"    groups: {res64.groups()}")
print(f"    group : {res64.group()}")
print(f"    group one : {res64.group(1)}")

# 65) Write a program to look how manytime IP address are repeated/count
mystring1 = "This the IP address 10.129.108.212, 10.129.108.213, 10.129.108.214, 10.129.108.212"
pat1= re.compile(r'\d+.\d+.\d+.\d+')
res65 = re.findall(pat1, mystring1)
# import counter from collection module
from collections import Counter

count= Counter(res65)
print(f"Question 65 answer are : ")
for x, y in count.items():
    if y > 1:
        print(f"    Ip adress: {x} and count : {y}")

# 66) write a program to grep word from the given string
s = "My favorite fruits are apple, banana, and mango."

res = re.findall(r'\b\w*e\b', s)
print(f"Question 66 answer are:  ")
print(f"    re.findall : {res}")

s = "My favorite fruits are apple, banana, and mango."
res = re.search(r'\b\w*e\b', s)

print(f"    re.search:  ")
if res:
    print(f"    {res.group()}")
else:
    print("    Not found.")

# 67) write a program to grep $ follwed with amount
s = "Price: $30, Discount: $5"

res = re.findall(r'\$(\d+)', s)
print(f"Question 67 answer is : {res}")

# 68) Program to print half triangles using *
# for example
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
print(f"Question 68 answer is: ")
row = 5
for x in range(row):
    for y in range(x+1):
        print("*", end=" ")
    print(" ")
# note: end=" " will continue in same line(does not go to new line)
# print(" ") this statement is for give space and go to new line for next for loop.

# 69) Program to print half triangles using * in reverse order
# for example
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

print(f"Question 69 answer is: ")
row = 5
for x in range(row, 0, -1):
    for y in range(x):
        print("*", end= " ")
    print(" ")

# 70) Write program to Floyd's Triangle of number with height 5
# for ex: 1
#         2 3
#         4 5 6
#         7 8 9 10
#         11 12 13 14 15

print(f"Question 70 answer is : ")
row = 5
count = 1
for x in range(row):
    for y in range(x+1):
        print(count, end= " ")
        count+= 1
    print(" ")

# 71) Program to print half pyramid a using numbers
# for example
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print(f"Question 71 answer is : ")
row = 5
count = 1
for x in range(row):
    for y in range(x+1):
        print(count, end= " ")
        count+= 1
    count = 1
    print(" ")
# 72) A recursive function in Python is a function that calls itself within its definition.
# This technique is useful for solving problems that can be broken down into smaller, self-similar subproblems.
# A recursive function typically has two parts: a base case and a recursive case.
# The base case is a condition that stops the recursion, while the recursive case calls the function itself with a modified input.

def factorial(n):
    if n == 0:
        return 1
    else:
        r = n * factorial(n-1)
    return r

res72 = factorial(3)
print(f"Question 72 answer is : {res72}")