# -*- coding: utf8 -*-


"""
    Author: Bc.Jakub Koreček, Msci,
    Email: N/A


    This is to exc. 2 in ch.1.

    We should create program that as a n input take numbers and calculate count, sum , min, max , mean.

    The solution is mine and is free to use any other student or school for learning Python.


"""

def Calculator():
    """
    This is just calculator which print all numbers into command line. There will be no input or return.

    Since, this is more learning, we do not use sum, min, max as built in function, instead we will find it manually.
    The only built in function to used is len()

    At first, we will have to order our list.

    We use build in function sort. The last and first member of list give us max resp min of the list.

    For sum, we use loop.


    :return:
    """

    list_of_numbers = []  # Initialize list for storing numbers.
    sum_value = 0
    min_value = max_value = None  # initialise sum variable, min_value, max_value

    while True:

        input_number = input('input number or Enter to finish:\t')  # Prompt.

        try:
            if input_number:
                input_number = float(input_number) # check if input is of correct type
                list_of_numbers.append(input_number) # store inputted numbers
                sum_value += input_number # update sum value

                if min_value is None or input_number < min_value:
                    min_value = input_number

                if max_value is None or input_number > max_value:
                    max_value = input_number

            else:

                count = len(list_of_numbers)   # get number of elements in list

                mean = sum_value/count # calculate mean

                print('Numbers:\t', list_of_numbers)
                print("count: ", count,"max: ",max_value ,"min: ",min_value, "mean: ", mean, "sum: ", sum_value )
                break

        except ValueError as e:
            print(e, '\n Wrong type of input!!!')
            continue
        except Exception as e:
            print(e, " \n Unhandled error in Calculator.")
            break

    return None # Not neccesary, since default is None , but for readability.


def main():

    Calculator() # call calculator

    return None


if __name__ == '__main__':
    main()