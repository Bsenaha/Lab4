# Number Analysis
def run():

    # ask 20 numbers
    num_list = []
    count = 0
    while count < 20:
        num = input('Enter a number: ')
        if not num.isdigit():
            print('Invalid, please enter an integer')
            continue
        num_list.append(int(num))
        count += 1

    # analysis and display
    num_list.sort()    # sort low to high

    # min, max
    low = num_list[0]
    high = num_list[-1]

    # sum
    total = sum(num_list)

    # avg
    avg = total / len(num_list)

    # display result
    print('\n\n============\nlowest number: ', low)
    print('highest number: ', high)
    print('sum: ', total)
    print('average: ', avg, '\n============\n')
    