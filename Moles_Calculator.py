# mole concept calculator
molar_mass_dictionary = {
    "H" : 1,
    "He" : 4,
    "Li" : 7,
    "Be" : 8,
    "B" : 11,
    "C" : 12,
    "N" : 14,
    "O" : 16,
    "F" : 19,
    "Ne" : 20,
    "Na" : 23,
    "Mg" : 24,
    "Al" : 26,
    "Si" : 28,
    "P" : 31,
    "S" : 32,
    "Cl" : 35.5,
    "Ar" : 40,
    "K" : 39,
    "Ca" : 40,
    "Sc" : 42,
    "Ti" : 45,
    "V" : 51,
    "Cr" : 52,
    "Mn" : 55,
    "Fe" : 56,
    "Co" : 56.8,
    "Ni" : 59,
    "Cu" : 63.5,
    "Zn" : 65.4,
    "H2O" : 18,
    "H2SO4" : 98,
    "CaCO3" : 100,
    "NaCl" : 58.5}

i=1
while i == 1:
    element = input("Enter element/compound: ")
    if element in molar_mass_dictionary:
        molar_mass = molar_mass_dictionary[element]
        choice = input("Do you want to find mass or moles? ")
        if choice.lower() == "moles":
            mass = float(input("Enter mass in grams: "))
            moles = mass / molar_mass
            print(f"{mass} g of {element} = {moles} moles")
        elif choice.lower() == "mass":
            moles = float(input("Enter moles: "))
            mass = moles * molar_mass
            print(f"{moles} of {element} = {mass} g")
        else:
            print("Error ")
    else:
        print("Element not found")
