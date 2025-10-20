import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

# Print a welcome message appropriate for all patrons
print("Welcome to the St Lucia science museum interactive display!")

debugging = True

# Print a statement explaining the patron types and prompt the user to enter their patron type
enthusiast = input("Are you: \n 1) A rookie? \n 2) An enthusiast? \n ")
if enthusiast == "1":
    enthusiast = False
elif enthusiast == "2":
    enthusiast = True
else:
    raise ValueError()


def print_both(msg: str):
    print(msg)


def print_enthusiast(msg: str):
    if enthusiast:
        print(msg)


def print_rookie(msg: str):
    if not enthusiast:
        print(msg)


# Print an introduction about remote sensing in agriculture
print(
    "Remote sensing in agriculture is the use of satellites, aircraft or drones to collect information about crops, \
farmland and soil, which saves farmers collecting this data on the ground themselves."
)
# It works by capturing data from reflected or emitted energy - most often light from the sun - across
# different parts of the electromagnetic spectrum (like visible, infrared, or thermal)
# most commonly the red and near-infrared (NIR) bands, because
# Healthy plants absorb red light (for photosynthesis)
# Healthy plants strongly reflect NIR light (due to leaf structure)
print(
    "This works by recording the reflected energy (usually from the sun). \
The data collected in remote sensing still needs to be processed and interpreted, however, which is where \
Vegetation Indexes (VIs) come in."
)
print_enthusiast(
    '"The most commonly used vegetation indices utilize the information contained in the red and near-infrared (NIR)\
canopy reflectances or radiances," (Fang and Liang)\
because healthy plants absord red light (for photosynthesis) and strongly reflect NIR light (due to leaf structure).'
)


def learn_about_vis():
    """Prompt the user to choose which VI they would like to learn about"""

    print()
    print(
        tabulate(
            [[1, "NDVI"], [2, "gNDVI"], [3, "EVI"], [4, "SAVI"], [5, "NDWI"]],
            headers=["Reference", "Vegetation Index"],
        )
    )
    vi = input("Which VI would you like to learn more about?: ")

    if vi == "1":
        # NDVI
        print()
    elif vi == "2":
        # gNDVI
        print()
    elif vi == "3":
        # EVI
        print()
    elif vi == "4":
        # SAVI
        print()
    elif vi == "5":
        # NDWI
        print()
    if input("Would you like to learn about any other VI? (N/y): ").lower() == "y":
        learn_about_vis()


learn_about_vis()

# Introduce LAI and the role that some VIs can play in predicting LAI
print("Related to VIs is the Leaf Area Index (abbreviated LAI).")
print_rookie("LAI measures how much leaf surface there is compared to ground area.")
print_enthusiast(
    "LAI is a measure of plant canopy density and can be used to estimate photosynthesis, transpiration and overall productivity.\
    LAI measures how much leaf surface is available to intercept light."
)
print("For example, LAI=3 means there is three times as much leaf area as ground area.")


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

# Given two points visually on the line of best fit,
# calculate the gradient and y-intercept of the resulting line of best fit
(p1x, p1y) = (-0.114, 2.027)
(p2x, p2y) = (-1.071, -1.928)
m = (p2y - p1y) / (p2x - p1x)
# Sub (p1x, p1y)
c = p1y - m * p1x


# M: 4.1327 C: 2.4981
def plta_linear_model():
    """Run this function to see the linearized data plus model"""
    plt.plot(np.log(gNDVIa), np.log(LAI), "ko", markersize=5)
    plt.xlabel("ln gNDVI")
    plt.ylabel("ln LAI")

    print(f"M: {m}, C: {c}")

    plt.plot(np.log(gNDVIa), m * np.log(gNDVIa) + c)

    plt.grid()
    plt.show()
    return


if debugging:
    plta_linear_model()


def gNDVI_LAI_model(gNDVI):
    """This is the model of LAI given gNDVI"""
    return gNDVI**m * np.e**c


def plta():
    """This will display the plotted gNDVI versus LAI data with the model"""
    plt.plot(gNDVIa, LAI, "ko", markersize=5)
    plt.plot(np.sort(gNDVIa), gNDVI_LAI_model(np.sort(gNDVIa)))
    plt.xlabel("gNDVI")
    plt.ylabel("LAI")
    plt.grid()
    plt.show()


if enthusiast:
    # Display a graph of the model you developed for LAI vs gNDVI.
    # Your graph should display your fitted model and the data. Describe
    # and explain the graph
    print("Here is a graph for gNDVI versus LAI")
    plta()
    # Identify one or two limitations of the model
    print("TODO limitations of the model")

# Print a statement about why LAI provides important information for agriculture
print(
    '"Leaf area index (LAI) and biomass are important indicators of crop development and the availability of this information \
    during the growing season can support farmer decision making processes." (Kross et al., 2015)'
)

# gNDVI over time data
gNDVIb = np.array(
    [0.381, 0.348, 0.408, 0.542, 0.727, 0.801, 0.806, 0.760, 0.831, 0.748]
)
DOY = np.array([150, 169, 173, 180, 193, 200, 211, 217, 231, 235])


def pltb():
    plt.plot(DOY, gNDVIb)
    plt.grid()
    plt.show()


# pltb()


# trapezoidal rule approximation for AUC
def trapezoid_area(y1, y2, width):
    """Area of a trapezoid"""
    lower = min(y1, y2)
    higher = max(y1, y2)
    return lower * width + 0.5 * (higher - lower) * width


auc = 0
i = 0
while i < len(DOY) - 1:
    left = gNDVIb[i]
    right = gNDVIb[i + 1]
    width = DOY[i + 1] - DOY[i]
    auc = auc + trapezoid_area(left, right, width)
    i = i + 1
# print(
#     f"Using the trapezoidal approximation for the AUC, the cumulative gNDVI for the crop season previous show is {auc} gNDVI days."
# )
