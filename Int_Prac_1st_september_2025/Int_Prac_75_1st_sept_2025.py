# 75) Take parameters from CLI to run script from CLi prompt.
    # syntax  python .\<filename.py> <parameter1> <parameter2> <parameter3>
    # Note: in import sys .\<filename.py> consider as parameter zero [0]
    # <parameter1> consider as parameter zero [1]
    # <parameter2> consider as parameter zero [1]
    # whatever we pass from cli or in python itself in always string.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
print(f"Question 75 answer is : {num1+num2+num3}")

