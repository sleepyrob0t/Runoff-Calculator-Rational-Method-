def get_runoff_coefficient(land_use):
    """Returns runoff coefficient based on land use type."""
    coefficients = {
        "pavement": 0.9,
        "urban": 0.7,
        "suburban": 0.5,
        "grass": 0.3,
        "forest": 0.1
    }
    return coefficients.get(land_use.lower(), None)

def calculate_runoff(C, I, A):
    """Calculates peak runoff using the Rational Method formula."""
    return C * I * A

# User inputs
land_use = input("Enter land use type (pavement, urban, suburban, grass, forest): ").strip().lower()
C = get_runoff_coefficient(land_use)

if C is None:
    print("Invalid land use type. Try again.")
else:
    I = float(input("Enter rainfall intensity (in/hr): "))
    A = float(input("Enter drainage area (acres): "))

    Q = calculate_runoff(C, I, A)
    print(f"\nEstimated peak runoff: {Q:.2f} cubic feet per second (cfs)")
