import numpy as np
import matplotlib.pyplot as plt


def main():
    # q4p1()
    q4p3()


def q4p1():
    """Question 4.1"""
    conc = np.array([0, 2, 4, 3, 0, 2, 2])
    time = np.array([0, 0.1, 0.5, 1.2, 1.4, 1.7, 2.0])

    plt.plot(time, conc)
    plt.xlabel("Time (hours)")
    plt.ylabel("Measured concentration m mol/L")

    area = 0
    i = 0
    while i < np.size(time) - 1:
        width = time[i + 1] - time[i]
        leftHeight = conc[i]
        area = area + width * leftHeight
        i = i + 1
    print(f"Area: {area}")

    plt.show()


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
      fahrenheit: The temperature in Fahrenheit (float or int).

    Returns:
      The equivalent temperature in Celsius (float).
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def q4p3():
    time = np.array([1260, 570, 270, 120, 60, 30, 15, 6, 3, 2, 1, 1])
    temp = np.array([120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142])
    plt.plot(time, temp)

    plt.show()


if __name__ == "__main__":
    main()
