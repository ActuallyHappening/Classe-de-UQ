import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

# gNDVI and LAI data
gNDVIa = np.array(
    [
        0.899,
        0.826,
        0.595,
        0.628,
        0.542,
        0.448,
        0.390,
        0.343,
        0.662,
        0.646,
        0.666,
        0.675,
        0.711,
        0.789,
        0.798,
        0.778,
        0.916,
        0.899,
        0.759,
        0.554,
        0.674,
        0.469,
        0.409,
        0.470,
        0.425,
        0.796,
        0.902,
        0.905,
        0.888,
        0.894,
    ]
)
LAI = np.array(
    [
        6.778,
        5.766,
        1.632,
        2.427,
        1.222,
        0.435,
        0.335,
        0.142,
        2.050,
        1.749,
        2.393,
        3.406,
        3.690,
        3.732,
        4.895,
        5.623,
        5.749,
        6.142,
        4.377,
        1.523,
        1.548,
        0.251,
        0.510,
        0.527,
        0.318,
        6.276,
        7.113,
        6.611,
        7.975,
        9.213,
    ]
)

(p1x, p1y) = (-0.114, 2.027)
(p2x, p2y) = (-1.071, -1.928)
m = (p2y - p1y) / (p2x - p1x)
# Sub (p1x, p1y)
c = p1y - m * p1x
# M: 4.1327 C: 2.4981
def plt_linear_model():
	"""Run this function to see the linearized model"""
	plt.plot(np.log(gNDVIa), np.log(LAI), "ko", markersize=5)
	plt.xlabel("ln gNDVI")
	plt.ylabel("ln LAI")

	print(f"M: {m}, C: {c}")

	plt.plot(np.log(gNDVIa), m*np.log(gNDVIa) + c)

	plt.grid()
	plt.show()
	return;
# plt_linear_model()

def gNDVI_LAI_model(gNDVI):
	return gNDVI ** m * np.e ** c

plt.plot(gNDVIa, LAI, "ko", markersize=5)
plt.plot(np.sort(gNDVIa), gNDVI_LAI_model(np.sort(gNDVIa)))
plt.grid()
plt.show()


# gNDVI over time data
gNDVIb = np.array(
    [0.381, 0.348, 0.408, 0.542, 0.727, 0.801, 0.806, 0.760, 0.831, 0.748]
)
DOY = np.array([150, 169, 173, 180, 193, 200, 211, 217, 231, 235])

# table of VIs to display
print(
    tabulate(
        [[1, "NDVI"], [2, "gNDVI"], [3, "EVI"], [4, "SAVI"], [5, "NDWI"]],
        headers=["Reference", "Vegetation Index"],
    )
)
