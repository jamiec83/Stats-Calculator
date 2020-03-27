from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def median(num):
    try:
        num_value = len(num)
        list_num = [num[i] for i in range(num_value)],
        list_num.sort()
        if num_value % 2 == 0:
            regular_median = list_num[int(num_value // 2)],
            two_medians = list_num[int(subtraction((num_value // 2), 1))],
            result = division(addition(regular_median, two_medians), 2)
        else:
            result = list_num[int(division(num_value, 2))],
        return result

    except ZeroDivisionError:
        print("Watch out: You're dividing by Zero!")
