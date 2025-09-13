import sys



# youtube link  https://www.youtube.com/watch?v=igvoTek4efQ&t=318s
# Open the command and go to C:\Users\arssa\PycharmProjects\Python_course_Learning\PythonBasic\Int_Prac_1st_july_2024\paramets_from_cli.py  to execute file.
# syntax  python .\<filename.py> <parameter1> <parameter2> <parameter3>
# Note: in import sys .\<filename.py> consider as parameter zero [0]
# <parameter1> consider as parameter zero [1]
# <parameter2> consider as parameter zero [1]
# whatevere we pass from cli or in python itself in always string.

# simple program
# note: .\<filename.py> consider as parameter zero [0]

print(sys.argv)
if len(sys.argv) < 3:
    print('Usage: python .\<filename.py parameter1 <parameter2> <parameter3>')
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    print(f"Total of p1, p2, p3 : {a+b+c}")

