#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(tp[0] * tp[1] for tp in my_list) / sum(tp[1] for tp in my_list)
