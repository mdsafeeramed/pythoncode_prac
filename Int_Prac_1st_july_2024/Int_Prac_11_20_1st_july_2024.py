# 11) Write a function to merge Two equal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e']
mylist2 = [0, 1, 2, 3, 4]

def merge_two_equal_list(mylist1, mylist2):
    max1 = max(len(mylist1), len(mylist2))
    myresult = []
    for x in range(max1):
        myresult.append((mylist1[x], mylist2[x]))
    return myresult

res1 = merge_two_equal_list(mylist1, mylist2)
print(f"Question 11 answer is : {res1}")

# 12) merge two unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]

max1 = max(len(mylist1), len(mylist2))
myresult = []
for x in range(max1):
    while True:
        try:
            myresult.append((mylist1[x], mylist2[x]))
        except IndexError:
            if len(mylist1) < max1:
                mylist1.append(0)
            if len(mylist2) < max1:
                mylist2.append(0)
        myresult.append((mylist1[x], mylist2[x]))
        break

print(f"Question 12 answer is : {myresult}")

# 13) write a function to merge two unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]

def megre_two_unequal_list(mylist1, mylist2):
    max1 = max(len(mylist1), len(mylist2))
    myresult = []
    for x in range(max1):
        while True:
            try:
                myresult.append((mylist1[x], mylist2[x]))
            except IndexError:
                if len(mylist1) < max1:
                    mylist1.append(0)
                if len(mylist2) < max1:
                    mylist2.append(0)
                myresult.append((mylist1[x], mylist2[x]))
            break
    return myresult

res3 = megre_two_unequal_list(mylist1, mylist2)
print(f"Question 13 answer is : {res3}")

# 14) merge three unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]

myresults = []
max1 = max(len(mylist1), len(mylist2), len(mylist3))
for x in range(max1):
    if len(mylist1) < max1:
        mylist1.append(0)
    if len(mylist2) < max1:
        mylist2.append(0)
    if len(mylist3) < max1:
        mylist3.append(0)
    myresults.append((mylist1[x], mylist2[x], mylist3[x]))

print(f"Question 14 answer is : {myresults}")
# 15) Write a function to merge three unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]

def merge_three_unequal_list(mylist1, mylist2, mylist3):
    myresults = []
    max1 = max(len(mylist1), len(mylist2), len(mylist3))
    for x in range(max1):
        if len(mylist1) < max1:
            mylist1.append(0)
        if len(mylist2) < max1:
            mylist2.append(0)
        if len(mylist3) < max1:
            mylist3.append(0)
        myresults.append((mylist1[x], mylist2[x], mylist3[x]))
    return myresults

res15 = merge_three_unequal_list(mylist1, mylist2, mylist3)
print(f"Question 15 answer is : {res15}")

# 16) Use ZIP inbuilt function to merge three unequal lists(Note ZIP return in form of objects, use for loop to extract results)
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]

mzip = zip(mylist1, mylist2, mylist3)
print("question 16 answer are:  ")
print(f"    ZIP object is : {mzip}")
print("    After for loop on mzip variable object: ")
for x in mzip:
    print(x)

# 17) Use ZIP inbuilt function to merge three unequal lists and results should be tuple in list.
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]

mzip = zip(mylist1, mylist2, mylist3)
mres = []
print("question 17 answer are:  ")
print(f"    ZIP object is : {mzip}")
for x in mzip:
    mres.append(x)
print(f"    After for loop on mzip variable object in tuples in list: {mres}")

# 18) Tuple unpacking from tuples under list which has 2-digit format.
mytuples = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
myres18 = []
for a, b in mytuples:
    myres18.append(a)
    myres18.append(b)

print(f"Question 18 answer is : {myres18}")

# 19) Tuple unpacking from tuples under list which has 3-digit format.
mytuples = [(1, 'a', 11), (2, 'b', 12), (3, 'c', 13), (4, 'd', 14)]

myres18 = []
for a, b, c in mytuples:
    myres18.append(a)
    myres18.append(b)
    myres18.append(c)

print(f"Question 19 answer is : {myres18}")

# 20) Find the maximum number in list without max function.
mylist_num = [10, 100, 20, 105, 60]
firstmax = 0
for x in mylist_num:
    if x > firstmax:
        firstmax = x
print(f"Question 20 answer : {firstmax}")

