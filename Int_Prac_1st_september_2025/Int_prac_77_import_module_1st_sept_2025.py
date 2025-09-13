# 77 write a program to import as module (question 76)

import Int_Prac_76_if_name_1st_sept_2025


def multi(*args):
    total = 0
    for x in args:
        total = x * total
    return total

print(f"Question 77 IMPORT CUSTOME MODULES answer are:  ")
res1 = Int_Prac_76_if_name_1st_sept_2025.add(1, 2, 3)

print(f"   {res1} ")
