#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: September 2019
# This program calculates the sum of two integers


def main():
    # this function calculates the sum of two integers

    # input
    first_integer = int(input("Enter the first number to add (Integer): "))
    second_integer = int(input("Enter the second number to add (Integer): "))

    # process
    sum = first_integer + second_integer

    # output
    print("")
    print("The sum is {}".format(sum))


if __name__ == "__main__":
    main()
