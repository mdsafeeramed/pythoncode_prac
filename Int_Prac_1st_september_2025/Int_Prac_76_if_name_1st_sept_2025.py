# 76) if __name__ == "main()"
# The if __name__ == "__main__" idiom is a Python construct that helps control code execution in scripts.(standalone script)
# It’s a conditional statement that allows you to define code that runs only when the file is executed as a script,
# not when it’s imported as a module.

# When you run a Python script, the interpreter assigns the value "__main__" to the __name__ variable.
# If Python imports the code as a module, then it sets __name__ to the module’s name instead.
# By encapsulating code within if __name__ == "__main__", you can ensure that it only runs in the intended context(only in script).


def add(*args):
    num = sum(args)
    return num

def sub(*args):
    total = 0
    for x in args:
        total = x - total
    return total
print(f"Question 76 answer are : {__name__}")

if __name__ == "__main__":
    res1 = add(1,2, 3, 4, 5)
    res2 = sub(1, 2, 3, 4, 5)
    print(f"Question 76 answer are : ")
    print(f"    if__name__ : {__name__}")
    print(f"    add : {res1}")
    print(f"    sub : {res2}")