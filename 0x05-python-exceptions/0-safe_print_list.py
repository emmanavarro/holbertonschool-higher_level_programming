#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elements in my_list[0:x]:
            print("{}".format(elements), end="")
            count += 1
    except IndexError:
        print("INVALID INDEX")
    finally:
        print()
        return count
