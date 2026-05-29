# Dimensional analysis

dimensions = {
    "m": {"M": 1, "L": 0, "T": 0},
    "a": {"M": 0, "L": 1, "T": -2},
    "F": {"M": 1, "L": 1, "T": -2},
    "E": {"M": 1, "L": 2, "T": -2},
    "v": {"M": 0, "L": 1, "T": -1},
    "p": {"M": 1, "L": 1, "T": -1},

    }


# defining the dimension checker
def DimensionChecker():
    choice = input("Do you want to check the dimensions of a certain physical quantity or do you want to find the physical quantity having certain dimensions? (PQ/Dimensions) ").lower()
    if choice == "pq":
        PQ = input("Enter physical quantity ")
        print(dimensions.get(PQ))
    elif choice == "dimensions":
        M = int(input("Enter Mass "))
        L = int(input("Enter Length "))
        T = int(input("Enter Time "))
        for quantity, dimension in dimensions.items():
            if {"M": M, "L": L, "T": T} == dimension:
                print(quantity)
                break
        else:
            print("Not found")
    else:
        print("Error")

DimensionChecker()

# version 1.0. The next version should hopefully try and expand this for equations in general, like F=ma.
