# 73) Take input from user, if they enter the number out of range ask user to re-enter the number in give range

while True:
    user_input = int(input("enter the Number between 1 to 10: "))
    if user_input < 1:
        print(f" INVALID INPUT IT SHOULD BE BETWEEN 1 to 10")
        continue
    elif user_input > 10:
        print(f" INVALID INPUT IT SHOULD BE BETWEEN 1 to 10")
        continue
    else:
        print("Correct")
    break

