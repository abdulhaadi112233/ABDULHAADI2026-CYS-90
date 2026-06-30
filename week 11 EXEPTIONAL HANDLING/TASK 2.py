try:
    # Input matrix elements
    a = float(input("Enter element a: "))
    b = float(input("Enter element b: "))
    c = float(input("Enter element c: "))
    d = float(input("Enter element d: "))

    # Calculate determinant
    determinant = a * d - b * c

    # Raise ZeroDivisionError if determinant is 0
    if determinant == 0:
        raise ZeroDivisionError("Matrix is singular and its inverse does not exist.")

    # Calculate inverse
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    # Display inverse matrix
    print("\nInverse Matrix:")
    for row in inverse:
        print(row)

except ValueError:
    print("Error: Please enter numeric values only.")

except ZeroDivisionError as e:
    print("Error:", e)