#!/usr/bin/env python3
# Created by: Remy Skelton
# Date: Sep. 22,2023
# This program calculates the area and circumference of a circle


import math


def main():
    print("For a circle with a radius of 17.46cm:")
    print()
    print("The area is: {:.2f}cm^2".format(math.pi * (17.46**2)))
    print("The circumference is: {:.2f}cm".format(2 * math.pi * 17.46))


if __name__ == "__main__":
    main()
