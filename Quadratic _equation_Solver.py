import math

def quadratic_solver():
    try:
        a = float(input("Enter the Coffeciant of A: "))
        b = float(input("Enter the Coefficiant of B: "))
        c = float(input("Enter the coefficinat of C: "))

        dicriminent = b**2 - 4*a*c

        if dicriminent > 0:
            root1 = (-b + math.sqrt(dicriminent)) / (2*a)
            root2 = (-b - math.sqrt(dicriminent)) / (2*a)
            print(f"The roots are real and distinct: {root1:.2f} and {root2:.2f}")

        elif dicriminent == 0:
            root = -b / (2*a)
            print(f"The root is real and repeated: {root:.2f}")

        else:
            # complex roots
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(-dicriminent) / (2*a)
            print(f"The roots are complex: {real_part:.2f} ± {imaginary_part:.2f}i")

    except ValueError:
        print("Please enter the valid inputs for the knowing the Coefficnats")
quadratic_solver()        