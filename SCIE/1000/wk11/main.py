import numpy as np
import matplotlib.pyplot as plt


def main():
    q4p1()


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


if __name__ == "__main__":
    main()
