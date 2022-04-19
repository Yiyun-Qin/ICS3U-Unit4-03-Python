#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, calculating square from 0 to n


def main():
    # This function shows the square of the number

    # input
    square_string = input("Enter a positive integer: ")

    # process & output
    print("")
    try:
        square_number = int(square_string)
        for loop_counter in range(square_number + 1):
            answer = pow(loop_counter, 2)
            print("{0}² = {1}".format(loop_counter, answer))
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
