import random

RANDOM_NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    invalid = False
    while not invalid:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            if number_of_quick_picks < 0:
                print("Please enter a positive number")
            else:
                invalid = True
        except ValueError:
            print("Please enter a positive number")

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(RANDOM_NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()