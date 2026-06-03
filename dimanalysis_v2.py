# Dimensional analysis database
# Each physical quantity has its dimensional values for Mass (M), Length (L), Time (T)
dimensions = {
    "m": {"M": 1, "L": 0, "T": 0},  # mass
    "a": {"M": 0, "L": 1, "T": -2}, # acceleration
    "F": {"M": 1, "L": 1, "T": -2}, # force
    "E": {"M": 1, "L": 2, "T": -2}, # energy
    "v": {"M": 0, "L": 1, "T": -1}, # velocity
    "p": {"M": 1, "L": 1, "T": -1}, # momentum
    "t": {"M": 0, "L": 0, "T": 1},  # time
    "P": {"M": 1, "L": 2, "T": -3}, # power
    "g": {"M": 0, "L": 1, "T": -2}, # gravitational acceleration (same as 'a')
    "W": {"M": 1, "L": 2, "T": -2}, # work (same as energy 'E')
     "ρ": {"M": 1, "L": -3, "T": 0},          # density
    "Pr": {"M": 1, "L": -1, "T": -2},        # pressure
    "τ": {"M": 1, "L": 2, "T": -2},          # torque
    "I": {"M": 1, "L": 2, "T": 0},           # moment of inertia
    "ω": {"M": 0, "L": 0, "T": -1},          # angular velocity
    "α": {"M": 0, "L": 0, "T": -2},          # angular acceleration
    "Lv": {"M": 1, "L": 2, "T": -1},         # angular momentum
    "f": {"M": 0, "L": 0, "T": -1},          # frequency
    "T": {"M": 0, "L": 0, "T": 1},          # period
    "x": {"M": 0, "L": 1, "T": 0},          # Displacement
}

# Dimension checker: find dimensions of a quantity, or find quantity by dimensions
def DimensionChecker():
    choice = input("Do you want to check the dimensions of a certain physical quantity, "
                   "or do you want to find the physical quantity having certain dimensions? (PQ/Dimensions) ").lower()
    if choice == "pq":
        PQ = input("Enter physical quantity (use standard notation/abbreviations; F, m, a, etc.): ")
        print(dimensions.get(PQ))
    elif choice == "dimensions":
        M = int(input("Enter Mass exponent: "))
        L = int(input("Enter Length exponent: "))
        T = int(input("Enter Time exponent: "))
        target = {"M": M, "L": L, "T": T}
        for quantity, dimension in dimensions.items():
            if dimension == target:
                print(quantity)
                break
        else:
            print("Not found")
    else:
        print("Invalid choice.")

# Run the dimension checker
DimensionChecker()

# The equationParser can only handle singular quantities on the LHS, say F=ma
def equationParser():
    LHS = []    # list of symbols on left‑hand side
    RHS = []    # list of symbols on right‑hand side
    equality = False
    equation = input("Enter equation: ")
    for ch in equation:
        if ch == "=":
            equality = True
            continue
        if not equality:
            LHS.append(ch)
        elif ch in dimensions:      # only add known symbols (skip '*', etc.)
            RHS.append(ch)
        # else ignore unknown characters (like '*')
    print(LHS)
    print(RHS)
    return LHS, RHS

LHS, RHS = equationParser()

# Dimensional analysis of the equation
def DimensionalAnalysis(LHS, RHS):
    # Add up dimensions on the left‑hand side
    Dimensions_LHS = dimensions.get(LHS[0])   # could be None if symbol unknown
    # Sum dimensions on the right‑hand side
    Dimensions_RHS = {'M': 0, 'L': 0, 'T': 0}
    for q in RHS:
        dim = dimensions.get(q)
        if dim is None:
            print(f"'{q}' is not in the database.")
            break
        Dimensions_RHS["M"] += dim["M"]
        Dimensions_RHS["L"] += dim["L"]
        Dimensions_RHS["T"] += dim["T"]

    # Check dimensional consistency
    if Dimensions_LHS == Dimensions_RHS:
        print("Equation is dimensionally consistent.")
    else:
        print("Equation is dimensionally inconsistent.")

    return Dimensions_LHS, Dimensions_RHS

# Run the analysis
Dimensions_LHS, Dimensions_RHS = DimensionalAnalysis(LHS, RHS)
print("LHS dimensions:", Dimensions_LHS)
print("RHS dimensions:", Dimensions_RHS)

# Limitations:
# It can only handle single-letter LHS equations.
# It has no way to decipher multi-letter quantities, say K.E or "rho"
# Not sure how to deal with exponents and division

# v3, then, would fix that.
