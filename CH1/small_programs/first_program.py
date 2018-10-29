#!/usr/bin/python3

"""
   This is first program to print some basic operation on integers, it has error handler for data type as well as
   calculate some basics, it is more or less, just simple procedural way of python code. It will output sum , # numbers
   entered, mean.
   call program by python first_program.py > result.txt < test.txt, for UNIX use chmod +x first_program.py then
    ./first_program.py > result.txt < test.txt
"""

print("Type integer for some basic calculation, followed by Enter or simply type Enter to finish")

total = 0  # initialise sum
count = 0  # initialise the number of items

while True:

    try:
        user_input = input()
        if user_input:  # it will return False upon ""- enter, of counter, else True
            user_input = int(user_input)  # check data type is correct
            count += 1
            total += user_input
    except ValueError as e:
        print(" Not an INTEGER, AGAIN PLEASE")
        continue # return back to while start to user correct data type from input
    except EOFError as e:
        break

    if count:  # it will return False upon 0, of counter, else True
        print("mean: ", total/count, "# of Numbers: ", count, "Sum: ", total )