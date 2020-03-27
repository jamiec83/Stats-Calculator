from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def median(num):
    try:
        num_value = len(num)
        number_list = [num[i] for i in range(num_value)]
        number_list.sort()
        if num_value % 2 == 0:
            median_1 = number_list[int(num_value // 2)]
            median_2 = number_list[int(subtraction((num_value // 2), 1))]
            median_result = division(addition(median_1, median_2), 2)
        else:
            median_result = number_list[int(division(num_value, 2))]
        return median_result
    except ZeroDivisionError:
        print("Watch out: You are dividing by Zero!")
    except ValueError:
        print("Error: check your inputs")