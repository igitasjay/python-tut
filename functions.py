global_var = "global variable"
def print_5_times(parameter = "param", loop_amount = 5):
    counter = 0
    print(global_var)
    while counter < loop_amount:
        print(loop_amount, parameter)
        counter += 1

def shouter (string = "default",  number = 5):
    if number > 10:
        print("you are too loud")
    else:
        counter = 0
        while counter < number:
            print(string.upper())
            counter += 1
    return "done"

stuff = shouter("custom", 11)
print(stuff)