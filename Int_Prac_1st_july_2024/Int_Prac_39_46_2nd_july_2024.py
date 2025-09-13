# 39) write a class to convert tuples in list
mytuples = [(1, 'a', 11), (2, 'b', 12), (3, 'c', 13), (4, 'd', 14)]
class Tuple_List:
    def __init__(self, mytuples):
        self.mytuples = mytuples

    def con_tup_list(self):
        myresults = []
        for a, b, c in self.mytuples:
            myresults.append(a)
            myresults.append(b)
            myresults.append(c)
        return myresults

objc1 = Tuple_List(mytuples)
res39 = objc1.con_tup_list()
print(f"Question 39 answer is : {res39}")

# 40) Write a class first for two unequal list and inherit class for three unequal list (normal way)
mylist1 = ['a', 'b', 'c', 'd', 'e', 'f']
mylist2 = [0, 1, 2, 3]
mylist3 = [10, 11, 12, 13]


class TwoUneuqalList:
    def __init__(self, mylist1, mylist2):
        self.mylist1 = mylist1
        self.mylist2 = mylist2

    def Two_unequal_merge(self):
        myresults = []
        max1 = max(len(self.mylist1), len(self.mylist2))
        for x in range(max1):
            if len(self.mylist1) < max1:
                self.mylist1.append(0)
            if len(self.mylist2) < max1:
                self.mylist2.append(0)
            myresults.append((self.mylist1[x], self.mylist2[x]))
        return myresults


obj2 = TwoUneuqalList(mylist1, mylist2)
res40_1 = obj2.Two_unequal_merge()
print("Question 40 answers are : ")
print(f"    Question 40_1 answer without inheritance two list merger  : {res40_1}")


class InherTwoUnequalList(TwoUneuqalList):
    def __init__(self, mylist1, mylist2, mylist3):
        self.mylist3 = mylist3
        TwoUneuqalList.__init__(self, mylist1, mylist2)

    def three_unequal_list(self):
        myresults = []
        max1 = max(len(self.mylist1), len(self.mylist2), len(self.mylist3))
        for x in range(max1):
            if len(self.mylist1) < max1:
                self.mylist1.append(0)
            if len(self.mylist2) < max1:
                self.mylist2.append(0)
            if len(self.mylist3) < max1:
                self.mylist3.append(0)
            myresults.append((self.mylist1[x], self.mylist2[x], self.mylist3[x]))
        return myresults


obj3 = InherTwoUnequalList(mylist1, mylist2, mylist3)
res40_2 = obj3.Two_unequal_merge()
res40_3 = obj3.three_unequal_list()
print(f"    Question 40_2 with inheritance two list answer is : {res40_2}")
print(f"    Question 40_3 with inheritance three list answer is : {res40_3}")


# 41) Write a class first and inherit the main class using super ()
class student_details:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display_details(self):
        return f"FIRSTNAME : {self.firstname}, LASTNAME : {self.lastname}"


obj4 = student_details("Mohammed", "Hammad")
res41_1 = obj4.display_details()
print(f"Question 41 answers are : ")
print(f"    Question 41_1 answer without inheritance : {res41_1}")

class InheriStudentDetails(student_details):
    def __init__(self, firstname, lastname, age):
        self.age = age
        super().__init__(firstname, lastname)

    def new_display(self):
        return f"FIRSTNAME : {self.firstname}, LASTNAME : {self.lastname}, AGE : {self.age}"

obj5 = InheriStudentDetails("Mohammed", "Hammad", 12)
res41_2 = obj5.display_details()
res41_3 = obj5.new_display()
print(f"    Question 41_2 answer with inheritance old display with super function usages: {res41_2}")
print(f"    Question 41_3 answer with inheritance new display with super function usages: {res41_3}")

# 42) Write a class first and inherit the main class using super () and use __num private variables.
class private_num:
    def __init__(self, _num1, num2):
        self._num1 = 10
        self.num2 = num2

    def display_num(self):
        return f"Private Number : {self._num1}, Normal number : {self.num2}"

obj6 = private_num(20, 100)
res42_1 = obj6.display_num()
print(f"Question 42 answers are : ")
print(f"    Question 42_1 answer without inheritance : {res42_1}")

class InheriPrivatenum(private_num):
    def __init__(self, _num1, num2):
        self._num1 = 20
        super().__init__(_num1, num2)

    def new_display(self):
        return f"With Inheritance Private Number : {self._num1}, Normal number : {self.num2}"

obj7 = InheriPrivatenum(200, 100)
res42_2 = obj7.display_num()
res42_3 = obj7.new_display()
print(f"    Question 42_2 answer with inheritance using super class : {res42_2}")
print(f"    Question 42_3 answer with inheritance using super class : {res42_3}")


# 43) I/O file using with open.
with open("2nd_july_2024.txt", mode="w+") as saf:
    saf.writelines("I am learning python1 \n")
with open("2nd_july_2024.txt", mode="a+") as saf:
    saf.writelines("I am learning python2 \n")
with open("2nd_july_2024.txt", mode="r+") as saf:
    content = saf.readlines()

print(f"Question 43 answer is : {content}")

# 44) Write a class to regexp using re.findall
mystring1 = "This the IP address 10.129.108.212"
import re

res44 = re.findall(r'\d+.\d+.\d+.\d+', mystring1)
print(f"Question 44 answer is : {res44}")

# 45) Write a class to regexp using re.findall and re.compile.
mystring1 = "This the IP address 10.129.108.212"
pat1 = re.compile(r'\d+.\d+.\d+.\d+')
res45 = re.findall(pat1, mystring1)
print(f"Question 45 answer is : {res45}")


# 46) Write a class to regexp using re.search, re.compile using and output span, group..etc
# note: group, span is available only when we use re.search command
mystring1 = "This the IP address 10.129.108.212"
pat1 = re.compile(r'(\d+).(\d+).(\d+).(\d+)')
res46 = re.search(pat1, mystring1)
print(f"Question 46 answer are: ")
print(f"   re.search full output with object : {res46} ")
print(f"   span only : {res46.span()}")
print(f"   groups only : {res46.groups()}")
print(f"   group only : {res46.group()}")
print(f"   group zero only : {res46.group(0)}")
print(f"   group 1 : {res46.group(1)}")


# 47) Write program to Floyd's Triangle of number with height 5
# for ex: 1
#         2 3
#         4 5 6
#         7 8 9 10
#         11 12 13 14 15

print(f"Question 47 answer is : ")
height = 5
count = 1
for x in range(1, 6):
    for y in range(0, x):
        # print(count, end=" ") to print output in horizontal line, ny default python print in next line
        print(count, end=" ")
        count += 1
    print()


# 48) Program to print half pyramid a using numbers
# for example
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print(f"Question 48 answer is : ")
height = 5
count = 1
for x in range(5):
    for y in range(x+1):
        # print(count, end=" ") to print output in horizontal line, ny default python print in next line
        print(y+1, end=" ")
    print()


# 49) Take input from user, if they enter the number out of range ask user to re-enter the number in give range

print(f"Question 49 answer is : ")
sav1 = int(input("Enter the number from 1 to 10: "))
while True:
    if sav1 > 11:
        print("Please select the number from the give range ")
        sav1 = int(input("Enter the number from 1 to 10: "))
    else:
        print("hrrrrrrr  re !!!!! you have selected the right number ")
        break

