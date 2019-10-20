#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This program can calculate if a year is a leap year or not


def main():
    # This function can calculate if a year is a leap year or not

    # Input
    year = int(input("Enter a year here: "))
    print("")

    # Process
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Your year is a leap year.")
            else:
                print("Your year is not a leap year.")
        else:
            print("Your year is a leap year.")
    else:
        print("Your year is not a leap year.")


if __name__ == "__main__":
    main()
