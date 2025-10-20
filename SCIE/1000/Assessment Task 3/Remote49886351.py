import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

# Print a welcome message appropriate for all patrons
print("Welcome to the St Lucia science museum interactive display!")

# Print a statement explaining the patron types and prompt the user to enter their patron type
enthusiast = input("Are you: \n 1) A rookie \n 2) An enthusiast")
if enthusiast == 1:
    enthusiast = False
elif enthusiast == 2:
    enthusiast = True

# Print an introduction about remote sensing in agriculture
print("""
Remote sensing in agriculture is the use of satellites, aircraft or drones to collect information about crops,
farmland and soil, which saves farmers collecting this data on the ground themselves.
""")
# It works by capturing data from reflected or emitted energy - most often light from the sun - across
# different parts of the electromagnetic spectrum (like visible, infrared, or thermal)
# most commonly the red and near-infrared (NIR) bands, because
# Healthy plants absorb red light (for photosynthesis)
# Healthy plants strongly reflect NIR light (due to leaf structure)
if enthusiast:
    print(
        """
"The most commonly used vegetation indices utilize the information contained in the red and near-infrared (NIR)
canopy reflectances or radiances," (Fang and Liang)
because healthy plants absord red light (for photosynthesis) and strongly reflect NIR light (due to leaf structure).
"""
    )

# Print an overview of vegetation indices and display the table of selected common VIs
print("""The data collected in remote sensing still needs to be processed and interpretted, however, which is where
Vegetation Indexes (VIs) come in.""")

# Prompt the user to choose which VI they would like to learn about

# table of VIs to display
print(
    tabulate(
        [[1, "NDVI"], [2, "gNDVI"], [3, "EVI"], [4, "SAVI"], [5, "NDWI"]],
        headers=["Reference", "Vegetation Index"],
    )
)

#  In comparison to the ground measurement
# method, remote-sensing method provides a practical
# method to estimate LAI at a large area with high temporal
# coverage.
# https://pdf.sciencedirectassets.com/277318/3-s2.0-C20091283602/3-s2.0-B9780080454054001907/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLWVhc3QtMSJIMEYCIQDxKn1l%2FBZ81s2BmpZtSBoRMM9xL%2FCPjY07g8LWvO1f8AIhAOP%2BFU6y9QH1L6q%2FIcrfdzTU8mEoENcI146jFC47uY8dKrwFCOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1Igx%2B%2Bgt9tJpsUjK32ssqkAUJxq4arCjc7TNJlzGJgR6adpOiwlDeNX3ibU2iZIDDcYNJYNxHv%2FAgWeCP5eL0JfEV3MvBwUHTZGkmZi2%2F33stj4W8RhG%2B%2Ba1qrXE9W14ZeQrg0n9lyf1blWtY7oLtYtIOoproLe2ylA99Udo%2BYMWJJ8r0DTtnxCetQ7RwiaGL7hAhYAUltOw%2BKEK%2BxnvcVvy8xC4L%2FpD12ki%2B%2BC0ApSBu23x%2FShUZd2%2F4IB1hWPckfqnzzXFTlOsjBu%2F%2BxxML7RkWnnR8IVcr%2BYtLGL3rUATjdaG5ZGV3dv7dB1%2FNpI9zCN6DgrHbCuipjRpxjQrFOKAqx2b22pSBCYJxa4U%2F08PR8%2F09QoK%2F76bFHgYI2nUCKmq0s7%2BQtNsGXsx60%2BIvvsPM1oKjbXimJf%2FSdB4BHvWVLqYLDhme9QZsWY9NbszNolbXd%2BHawzE9MOJObgXtJ0DkJjKRMsikcmpfERtIKNcphAXIX%2FQASSwKE%2FHUMHM%2FbnfYxNATryxLwl75okSvXPyk4P896oOhNuxUHkljcmIQ4P7NXCgI3QqkE%2BZBkxbVevjr4oaNPDYA90u4w03B6Vrym261xg5V7OWYTEPefFfc%2F9L5bzVe31KTSfjrHWJLfi3GPBXaLGVM8kJl5zstzhIbo7YSw3MDgVP%2F4U1LYHOR6vwnQImgCCFNd4rKnZ24lXyBrCDPD0b02itJXmpITKMYCAXCjoWwvc4TK7dibMuRVX0h%2B82yDvQlWR35stiUNiQYdheg2Py%2BzeuzkqIHkV6SSOJRIiQVG2YNlk2bc8a24P0fN6rpfQoS6zqp%2Bu0m7erTcCBh7HBKid0CKUVC0TemZf3pvGma7Z6hgvxeyKJV5JyO%2B1fPC42oJDoom40MnjCT9tbHBjqwAYC%2FEADxn%2BWiMByfRmH2eXnRmxOk%2B5S6QuSudqddYmWZxK49dPdP16VcFWDKMQaFX6uWKA%2BIYNp8RGRbecKq2qugMX9jWJ4J%2BTiOjlejLP0FAmVCYBetIx6Hukbjl%2Br0u2taQAckPSlBqu60GYv%2Ft7AT%2FUBrEOafaqXHR9M%2BcKECHhjsEfoNLJZD5eTxYpj3LFnBFKLrfDihgRsgiqnqsX99vSyOZlaUznv1wWCsQtEn&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251020T051935Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYQGDN3Z4I%2F20251020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=30e1b777a2e2b7616cd06370512e40dbc5d1df50d9a79429b596110171c41961&hash=2e71cabc580d55faa5a55a4cd25ea53cbc588d6f4e28bc456982dc2c187ac8d4&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=B9780080454054001907&tid=spdf-81aa5984-7a6b-4ba3-8de7-ec109834754a&sid=55b4d503184f55451b982f60287a9b3cc7d9gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1b105e56535253060e5501&rr=99160fa2ffdfd710&cc=au

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


# plta_linear_model()


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


# plta()


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
print(
    f"Using the trapezoidal approximation for the AUC, the cumulative gNDVI for the crop season previous show is {auc} gNDVI days."
)
