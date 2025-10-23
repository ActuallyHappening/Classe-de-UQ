from math import log as ln, e


def MorphineModel(dose_amount: float, hours_since_last_dose: float) -> float:
    """
    Time since last dose is in units hours,
    result units is same as dose_amount
    """
    A = dose_amount
    B = -ln(2) / 2
    return A * e ** (B * hours_since_last_dose)


def patient():
    body_mass_kg = float(input("What is the mass in Kilograms (kg) of your patient: "))
    dose_amount_milligrams = body_mass_kg * 0.1
    print(f"You should provide {dose_amount_milligrams:.2f}mg of morphine.")

    hours_since_last_dose = float(input("How many hours have passed: "))
    if hours_since_last_dose < 24.0:
        morphine_milligrams_remaining = MorphineModel(
            dose_amount_milligrams, hours_since_last_dose
        )
        print(
            f"There is approximately {morphine_milligrams_remaining:.2f}mg of morphine remaining"
        )
    else:
        print("There is a negligible amount of morphine remaining")
    if input("Do you have another patient? (y/N): ").lower() in ["y", "yes", "1"]:
        patient()


patient()
