# Uses Euler ’s method to model the turtle population .
import numpy as np
import matplotlib.pyplot as plt

# Initialise variables .
maxt = 30
Hpops = np.zeros(int(maxt + 1))
Ypops = np.zeros(int(maxt + 1))
Apops = np.zeros(int(maxt + 1))

stepsize = 1
times = np.arange(0, maxt + stepsize, stepsize)

for i in range(1, np.size(times)):
    dH = -Hpops[i - 1] + 77.4 * Apops[i - 1]
    dY = 0.675 * Hpops[i - 1] - 0.230434 * Ypops[i - 1]
    dA = 0.000434 * Ypops[i - 1] - 0.191 * Apops[i - 1]
    Hpops[i] = Hpops[i - 1] + stepsize * dH
    Ypops[i] = Ypops[i - 1] + stepsize * dY
    Apops[i] = Apops[i - 1] + stepsize * dA
# Output the graph.
plt.plot(times, Hpops / 1e6, "bx", markersize=8, label="Hatchlings")
plt.plot(times, Ypops / 1e6, "r+", markersize=8, label="Youths")
plt.plot(times, Apops / 1e6, "gs", markersize=6, label="Adults")
plt.plot(times, (Hpops + Ypops + Apops) / 1e6, "ko", markersize=6, label="Total")
plt.xlabel("Time (years)")
plt.ylabel("Number of turtles ( millions )")
plt.grid(True)
plt.legend()
plt.show()
