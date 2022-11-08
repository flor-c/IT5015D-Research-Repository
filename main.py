# Name that Triangle (If Statement)

side_a = int(input("Enter the length of the first side \n"))
side_b = int(input("Enter the width of the second side \n"))
side_c = int(input("Enter the height of the third side \n"))

if side_a == side_b == side_c:
    print("Equilateral")

if side_a == side_b and side_a != side_c \
    or side_a == side_c and side_a != side_b \
    or side_b == side_c and side_b != side_a:
    print("Isosceles")

if side_a != side_b != side_c:
    print("Scalar")

