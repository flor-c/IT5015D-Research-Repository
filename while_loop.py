number = int(input("Please enter a number \n"))
counter = 0
total = 0

while counter <= number:
    total = total + counter
    counter += 1

print("\n n = ", number, " sum = ", total, "\n")

p = int(input("Please enter an increment \n"))
q = int(input("Please enter an ending number \n"))

contador = 10
numero = 10

starting_number = (10 % p) + 10

while contador < q:
    print(starting_number, end=", ")
    starting_number = starting_number + p
    contador += p

