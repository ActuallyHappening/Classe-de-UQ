import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

# Print a welcome message appropriate for all patrons
print("Welcome to the St Lucia science museum interactive display!")

# Print a statement explaining the patron types and prompt the user to enter their patron type
enthusiast = input("Are you: \n 1) A rookie? \n 2) An enthusiast? \n ")
if enthusiast == "1":
    enthusiast = False
elif enthusiast == "2":
    enthusiast = True
else:
    # raise ValueError()
    enthusiast = True


def print_enthusiast(msg: str = ""):
    """Only prints the message if the user is an enthusiast"""
    if enthusiast:
        print(msg)


def print_rookie(msg: str = ""):
    """Only prints the message if the user is a rookie"""
    if not enthusiast:
        print(msg)


def nl(num: int):
    """Prints a number of newlines to the screen for legibility"""
    print("\n" * (num - 1))


nl(2)

# Print an introduction about remote sensing in agriculture
print_enthusiast(
    "Remote sensing in agriculture is the use of satellites, aircraft or drones to collect information about crops, \
farmland, soil, and more broadly the ground level environment, which saves farmers collecting this data on the ground themselves and informs evidence-based environmental and agriculture decision-making."
)
print_rookie(
    "Remote sensing in agriculture is the use of satellites or drones to collect information about a farmers crops, \
informing farmers and saving them time and money."
)
print_enthusiast(
    "This works by capturing data from light reflected from the sun (usually) across \
different parts of the EM spectrum, usually red and near infrared (NIR) bands, and sometimes \
blue and green bands."
)
print_rookie(
    "This is usually achieved by pointing a camera down towards the Earth somewhere you are interested in and \
recording what you see. Cameras can often spot things that the naked eye would miss, such as a slight lack of water."
)

nl(1)

print_enthusiast(
    "To interpret and summarise the data collected, the concept of a Vegetation Index was created."
)
print_enthusiast(
    '"Vegetation indices are mathematical formulas that use specific image bands to assess plant health. \
Image bands are specified wavelength ranges within the electromagnetic spectrum captured by the drone\'s camera. \
Each band corresponds to a different part of the spectrum (e.g., visible, infrared) that allows us to detect \
different characteristics about plant health." \
(“Understanding Vegetation Indices,” 2024)'
)
print_rookie(
    "To interpret the many images taken, scientists have developed Vegetation Indexes (abbreviated as VIs), \
which provide a convenient summary of the data and can produce visual images for people to analyse."
)
print("Vegatation Indexes (VIs) are usually defined between -1 and 1.")


def learn_about_vis():
    """Prompt the user to choose which VI they would like to learn about"""

    nl(1)
    print(
        tabulate(
            [[1, "NDVI"], [2, "gNDVI"], [3, "EVI"], [4, "SAVI"], [5, "NDWI"]],
            headers=["Reference", "Vegetation Index (VI)"],
        )
    )
    nl(1)
    vi = input("Which VI would you like to learn more about?: ")
    nl(1)

    if vi == "1":
        # NDVI
        print("NDVI stands for Normalized Difference Vegetation Index")
        print_rookie(
            "NDVI is an industry standard vegetation index (VI) that assesses plant health. Higher NDVI values indicate healthier, denser vegetation (e.g. NDVI = 0.6), while lower values suggest stress, drought or spare plant cover (e.g. NDVI = 0.1)"
        )
        print_enthusiast(
            "NDVI is an industry standard vegetation index that that assesses plant health by comparing the difference between near-infrared and red bands of the electromagnetic spectrum. \
NDVI measures the chlorophyll content and photosynthetic activity of plants. Higher NDVI values indicate healthier, denser vegetation, while lower values suggest stress, drought, or sparse plant cover."
        )
        print_enthusiast("")
        print_enthusiast(
            tabulate(
                [
                    ["-1 to 0", "Non-vegetated surfaces"],
                    ["0 to 0.2", "Spare vegetation"],
                    ["0.2 to 0.5", "Healthy vegetation"],
                    ["0.5 to 0.9", "Dense, healthy vegetation"],
                ],
                headers=["NDVI Value Range", "Interpretation"],
            )
        )
        print_enthusiast("")
        print("(“Understanding Vegetation Indices,” 2024)")
    elif vi == "2":
        # gNDVI
        print("gNDVI stands for Green Normalized Difference Vegetation Index.")
        print(
            "gNDVI is a variation of NDVI that uses green reflectance instead of red reflectance."
        )
        print(
            "The green band improves the index's ability to detect healthy vegetation, as healthy plants reflect more green light."
        )
        print_enthusiast(
            "gNDVI is useful for landscapes with dense canopies due to a high sensitivity to chlorophyll."
        )
        print("(“Understanding Vegetation Indices,” 2024)")

    elif vi == "3":
        # EVI
        print("EVI stands for Enhanced Vegetation Index.")
        print(
            "EVI is a vegetation index (VI) that quantifies vegetation greenness and vigor."
        )
        print_enthusiast(
            "Like NDVI, EVI uses data from the visible and near-infrared (NIR) parts of the spectrum."
        )
        print(
            "Unlike NDVI, EVI uses the blue band from light detected, which helps reduce atmostpheric interference and enhances sensitivity in densely vegetated areas."
        )
        print(
            "EVI is therefore better in dense vegetation, tropical forests, and is less affected by cloud and shadow."
        )
        print("(L, 2024)")
    elif vi == "4":
        # SAVI
        print("SAVI stands for Soil Adjusted Vegetation Index.")
        print(
            "SAVI is a vegetation index that minimizes the influence of soil brightness when assessing plant health."
        )
        print(
            "Bright or reflective soils can lead to inaccurate readings of plant health by reflecting more light when the soil is exposed."
        )
        print_enthusiast(
            "The SAVI equation includes a soil adjustment factor, which is effective for areas with spares vegetation or bare soil."
        )
        print("(“Understanding Vegetation Indices,” 2024)")
    elif vi == "5":
        # NDWI
        print(
            "The Normalized Difference Water Index (NDWI) is used to highlight open water features in a satellite image, allowing a water body to “stand out” against the soil and vegetation."
        )
        print_enthusiast("The NDWI index was proposed by McFeeters in 1996.")
        print(
            "Its primary use today is to detect and monitor slight changes in water content of the water bodies."
        )
        print_enthusiast(
            "Taking advantage of the NIR (near-infrared) and GREEN (visible green) spectral bands, the NDWI is capable of enhancing the water bodies in a satellite image."
        )
        print(
            "The downside of the index is that it is sensitive to built structures, which can lead to overestimation of water bodies."
        )

        print_enthusiast("")
        print_enthusiast(
            tabulate(
                [
                    ["-1 to -0.3", "Drought, non-aqueous surfaces"],
                    ["-0.3 to 0", "Moderate drought, non-aqueous surfaces"],
                    ["0 to 0.2", "Flooding, humidity"],
                    ["0.2 to 1", "Water surface"],
                ],
                headers=["NDWI Value Range", "Interpretation"],
            )
        )
        print_enthusiast("")
        print("(EOS Data Analytics, 2017)")

    nl(1)
    user_input = input(
        "Would you like to learn about any other VI? \n Yes) 1 \n  No) 2 \n"
    )
    if user_input == "1":
        learn_about_vis()


learn_about_vis()

nl(2)

# Introduce LAI and the role that some VIs can play in predicting LAI
print("Related to VIs is the Leaf Area Index (abbreviated LAI).")
print_rookie(
    "LAI measures how much leaf surface there is compared to ground area. \
This is useful to know as it can be used to estimate overal crop productivity."
)
print_enthusiast(
    "LAI is a measure of plant canopy density and can be used to estimate photosynthesis, transpiration and overall productivity. \
LAI measures how much leaf surface is available to intercept light."
)
print(
    "For example, LAI=3 means that if you laid down all the leaves in a field flat, \
there would be three times as much leaf area as ground area."
)

nl(2)


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


# If you want to see the linearized version of plta(), uncomment and run
# def plta_linear_model():
#     """Run this function to see the linearized data plus model"""
#     plt.plot(np.log(gNDVIa), np.log(LAI), "ko", markersize=5)
#     plt.xlabel("ln gNDVI")
#     plt.ylabel("ln LAI")
#     print(f"M: {m}, C: {c}")
#     plt.plot(np.log(gNDVIa), m * np.log(gNDVIa) + c)
#     plt.grid()
#     plt.show()
#     return
# plta_linear_model()


# m, c = 4.1327, 2.4981
def gNDVI_LAI_model(gNDVI):
    """This is the model of LAI given gNDVI"""
    e = np.e
    return gNDVI**m * e**c


def plta():
    """This will display the plotted gNDVI versus LAI data with the model"""
    plt.plot(gNDVIa, LAI, "ko", markersize=5)
    plt.plot(np.sort(gNDVIa), gNDVI_LAI_model(np.sort(gNDVIa)))
    plt.xlabel("gNDVI")
    plt.ylabel("LAI")
    plt.title("gNDVI versus LAI")
    plt.grid()
    plt.show()


if enthusiast:
    # Display a graph of the model you developed for LAI vs gNDVI.
    # Your graph should display your fitted model and the data. Describe
    # and explain the graph
    print("Here is a graph of gNDVI versus LAI.")
    print(
        "This graph shows the relationship between the VI gNDVI and LAI. It approximately follows a growing power law relationship as gNDVI increases."
    )
    print("A power law model for the data is plotted on top as a solid line.")
    plta()

    nl(2)

    # Identify one or two limitations of the model
    print(
        "As this is a power function, the behaviour past gNDVI < 0 isn't very accurate to the data. If it is even defined, the LAI balloons positively, \
such that completely dead vegetation (e.g. gNDVI = -0.5) has a very positive LAI which isn't reasonable."
    )
    print("Therefore this model is only reasonable for gNDVI > 0.")

# Print a statement about why LAI provides important information for agriculture
print(
    "As gNDVI increases, the LAI increases, which allows prediction of crop development based only on remote sensing data."
)
print(
    '"Leaf area index (LAI) and biomass are important indicators of crop development and the availability of this information \
during the growing season can support farmer decision making processes." (Kross et al., 2015)'
)

nl(2)


# gNDVI over time data
gNDVIb = np.array(
    [0.381, 0.348, 0.408, 0.542, 0.727, 0.801, 0.806, 0.760, 0.831, 0.748]
)
DOY = np.array([150, 169, 173, 180, 193, 200, 211, 217, 231, 235])


def pltb():
    plt.plot(DOY, gNDVIb)
    plt.xlabel("Day of Year")
    plt.ylabel("gNDVI")
    plt.title("gNDVI over Time")
    plt.grid()
    plt.show()


# trapezoidal rule approximation for AUC
def trapezoid_area(y1, y2, width):
    """Area of a trapezoid"""
    lower = min(y1, y2)
    higher = max(y1, y2)
    return lower * width + 0.5 * (higher - lower) * width


# Print a statement explaining how/why VIs change over time, and why cumulative VI can be important for
# understanding certain aspects of crop health and yield.
print_enthusiast(
    "Cumulative VIs are VIs summed over time. \
For example, the cumulative gNDVI could be the sum of gNDVI values every day over one harvest cycle."
)
print_enthusiast(
    "Cumulative NDVI has been shown to corrolate with overall crop yield (Exploring NDVI as a Predictor of Corn Yield, 2022). \
The previous graph of LAI versus gNDVI predicted increased LAI versus cumulative gNDVI, and as LAI is related to biomass, \
this model also corroberates with cumulative NDVI being a predictor of crop yield."
)
print_rookie(
    "Cumulative Vegetative Indexes (VIs) are a measure of how much VI there is in total over some time frame. \
For example, over a season of 80 days, the cumulative gNDVI would be the sum of each gNDVI value every day."
)
print_rookie(
    "Cumulative NDVI has been shown to be a predictor of crop yield, making it an important metric for \
farmers to understand from remote sensing data (Exploring NDVI as a Predictor of Corn Yield, 2022)."
)
print_enthusiast(
    '"By better understanding the relationship between NDVI metrics [e.g. cumulative gNDVI] and crop yield, \
stakeholders in the agricultural industry can make more informed decisions and optimize resource use, \
ultimately leading to increased productivity and sustainability." (Exploring NDVI as a Predictor of Corn Yield, 2022)'
)

nl(2)


if enthusiast:
    # Display a graph of gNDVI over time. Describe and explain your
    # graph, including how cumulative gNDVI relates.
    print("This is a graph of gNDVI measured using remote sensing over a span 83 days.")
    print(
        "The area under the curve (AUC) is the cumulative gNDVI for the harvest season shown, which would have units 'gNDVI days'."
    )
    pltb()

    auc = 0
    i = 0
    while i < len(DOY) - 1:
        left = gNDVIb[i]
        right = gNDVIb[i + 1]
        width = DOY[i + 1] - DOY[i]
        auc = auc + trapezoid_area(left, right, width)
        i = i + 1

    # Print a statement including the calculated cumulative gNDVI for a
    # crop season.
    print(
        f"Using the trapezoidal approximation for the AUC, the cumulative gNDVI for the crop season previously shown was {auc} gNDVI days."
    )

    nl(2)

# Print an appropriate farewell message.
print("Thankyou for using St Lucia's science museum's interactive display!")
print(
    "We hope you now have an appreciation of the nuances and importance of Vegetation Indexes, LAI, and their benefits to global agriculture."
)
