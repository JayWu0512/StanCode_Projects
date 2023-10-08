"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

sc001_list = []
sc101_list = []


def main():
    """
    Step 1: discriminate which class, SC001 or SC101
    Step 2: change upper case to lower case
    Step 3: boundary condition, if there is no data, print "no class scores were entered."
    Step 4: set the breakpoint
    Step 5: sc001 condition
    Step 6: sc101 condition
    Step 7: considering "no score entered".
    Step 8: print max, min, average.
    """

    a = input("Which class? ")
    a = a.lower()
    # turn into lower case, avoid case sensitive

    if a == "-1":
        print('No class scores were entered.')
        # boundary condition
    else:
        while True:
            if a == "-1":
                break
                # set the breakpoint

            elif a == "sc001":
                b = int(input('Score: '))
                sc001_list.append(b)
                a = input("Which class? ")
                a = a.lower()
                # enter next class, if set outside elif, it needs to enter class twice initially.

            elif a == "sc101":
                b = int(input('Score: '))
                sc101_list.append(b)
                a = input("Which class? ")
                a = a.lower()
                # enter next class, if set outside elif, it needs to enter class twice initially.

        print('=============SC001=============')
        if len(sc001_list) == 0:
            print('No score for SC001.')
        else:
            print('Max(001): ' + str(max(sc001_list)))
            print('Min(001): ' + str(min(sc001_list)))
            print('Avg(001): ' + str(average_sc001()))
        print('=============SC101=============')
        if len(sc101_list) == 0:
            print('No score for SC101.')
        else:
            print('Max(101): ' + str(max(sc101_list)))
            print('Min(101): ' + str(min(sc101_list)))
            print('Avg(101): ' + str(average_sc101()))


def average_sc001():
    return float(sum(sc001_list)/len(sc001_list))


def average_sc101():
    return float(sum(sc101_list)/len(sc101_list))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
