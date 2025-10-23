# Add to this cell to complete the program

import numpy as np
import matplotlib.pyplot as plt

# Patient's medication schedule: 1 = took dose, 0 = missed dose
schedule = np.array([1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1])

# Create an array to store the concentrations for each day
concentration = np.zeros(len(schedule))

# Fill in the rest of your program below

for i, remembered in enumerate(schedule):
    current = 0
    if i > 0:
        current = concentration[i - 1]
    if bool(remembered):
        concentration[i] = current + 5 - 2
    else:
        concentration[i] = current - 2
    if concentration[i] > 10:
        print(f"{i} days later, the concentration is effective at {concentration[i]}")
    else:
        print(
            f"{i} days later, the concentration is not effective at {concentration[i]}"
        )

print(f"{concentration=}")
