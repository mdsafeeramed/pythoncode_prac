# 21) Write a function to merge Two equal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e']
mylist2 = [0, 1, 2, 3, 4]
max1 = max(len(mylist1), len(mylist2))
def merge_two_equal(mylist1:list, mylist2:list):
    myres= []
    for x in range(max1):
        myres.append((mylist1[x], mylist2[x]))
    return myres

res11 = merge_two_equal(mylist1, mylist2)
print(f"Question 21 answer is : {res11}")

# 22) merge two unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
max1 = max(len(mylist1), len(mylist2))
mytup = []
for x in range(max1):
    while True:
        try:
            mytup.append((mylist1[x], mylist2[x]))
        except IndexError:
            if(len(mylist1)) < max1:
                mylist1.append(0)
            if(len(mylist2)) < max1:
                mylist2.append(0)
            mytup.append((mylist1[x],mylist2[x]))
        break

print(f"question 22 answer is : {mytup}")


# 23) write a function to merge two unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
max1 = max(len(mylist1), len(mylist2))

def merge_two_unequal_list(mylist1:list, mylist2:list):
    mytup = []
    for x in range(max1):
        while True:
            try:
                mytup.append((mylist1[x], mylist2[x]))
            except IndexError:
                if(len(mylist1)) < max1:
                    mylist1.append(0)
                if(len(mylist2)) < max1:
                    mylist2.append(0)
                mytup.append((mylist1[x],mylist2[x]))
            break
    return mytup

res23 = merge_two_unequal_list(mylist1, mylist2)
print(f"Question 23 answer is: {res23}")

# 24) merge three unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]
max1 = max(len(mylist1), len(mylist2), len(mylist3))
myval = []
for x in range(max1):
    if (len(mylist1)) < max1:
        mylist1.append(0)
    if (len(mylist2)) < max1:
        mylist2.append(0)
    if (len(mylist3)) < max1:
        mylist3.append(0)
    myval.append((mylist1[x], mylist2[x], mylist3[x]))

print(f"Question 24 answer is : {myval}")
# 25) Write a function to merge three unequal lists and result should be in list of tuple like [(a, 0)…etc]
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]
max1 = max(len(mylist1), len(mylist2), len(mylist3))
def merge_three_unequal_list(mylist1, mylist2, mylist3):
    myval = []
    for x in range(max1):
        if (len(mylist1)) < max1:
            mylist1.append(0)
        if (len(mylist2)) < max1:
            mylist2.append(0)
        if (len(mylist3)) < max1:
            mylist3.append(0)
        myval.append((mylist1[x], mylist2[x], mylist3[x]))
    return myval

res25 = merge_three_unequal_list(mylist1, mylist2, mylist3)
print(f"Question 25 answer is : {res25}")

# 26) Use ZIP inbuilt function to merge three unequal lists(Note ZIP return in form of objects, use for loop to extract results)
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]
myzip = zip(mylist1, mylist2, mylist3)
print("Question 26 answer are:   ")
print(f"    ZIP OBJECT: {myzip}")
myres= []
for x in myzip:
    myres.append(x)
print(f"    After for loop: {myres}")

# direct for loop with zip
myres1 = []
for x in zip(mylist1, mylist2, mylist3):
    myres1.append(x)

print(f"    direct for loop with zip: {myres1}")

# sepearte the tuple
myres2 = []
for x, y, z in zip(mylist1, mylist2, mylist3):
    myres2.append(x)
    myres2.append(y)
    myres2.append(z)

print(f"    Extract tuples in zip: {myres2}")
# 27) Use ZIP inbuilt function to merge three unequal lists and results should be tuple in list.
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]
myres1 = []
for x in zip(mylist1, mylist2, mylist3):
    myres1.append(x)

print(f"question 27 answer is: {myres1}")
# 28) Tuple unpacking from tuples under list which has 2-digit format.
mytuples = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
myres28 = []
for x, y in mytuples:
    myres28.append(x)
    myres28.append(y)
print(f"Question 28 answer is : {myres28}")
# 29) Tuple unpacking from tuples under list which has 3-digit format.
mytuples = [(1, 'a', 11), (2, 'b', 12), (3, 'c', 13), (4, 'd', 14)]
myres29 = []
for x, y, z in mytuples:
    myres29.append(x)
    myres29.append(y)
    myres29.append(z)
print(f"Question 29 answer is : {myres29}")
# 30) Find the maximum number in list without max function.
mylist_num = [10, 100, 20, 60]
firstmax = 0
for x in mylist_num:
    if x > firstmax:
        firstmax = x
print(f"Question 30 answer is : {firstmax}")