days_of_the_week = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print(days_of_the_week[1], end=" ")
print(days_of_the_week[4], end=" ")
print(days_of_the_week[-3])

list_1 = [23, 66, 23, 12]
list_2 = [1,19, 4, 8]
list_3 = ["land of ", "the ", "the long white cloud"]
list_sum = (sum(list_1) + sum(list_2))

print(list_1, list_2)
user_input = input("Type sum or average? \n")
if user_input.lower() == "sum":
    print("The sum of the item is: ", list_sum)

if user_input.lower() == "average":
    average = float(list_sum) / (len(list_1) + len(list_2))
    print("The average of the items in the list is: ", average)


# gets the smallest integer from list_2
list_2.sort()
print(list_2)
print(list_2[0])

