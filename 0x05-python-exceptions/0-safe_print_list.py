#!/usr/bin/python3
def safe_print_list(my_list=[], var=0):
    vara = 0
    for i in range(0, var):
        try:
            print(f'{my_list[i]}', end="")
            vara += 1
        except (IndexError):
            continue
    print()
    return (vara)
