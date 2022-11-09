# Functions with Parameters

user_name = input("Please enter your name: ")
user_phone = input("Please enter your phone number: ")


def message(user_name, user_phone):
    print(f"Hello there, my name is ", user_name, "and my phone number is ", user_phone)


message(user_name, user_phone)

# ask for a number and outputs the first 4 multiples

base = int(input("Please enter a number:  "))
def display_multiples(base):
    ctr = 1
    num = base
    while ctr <= 4:
        num += base
        ctr += 1
        print(num)


display_multiples(base)

# print the even numbers from a stored list

print("\n\nCounting even numbers from this list: ")
num_list = [3, 5, 6, 2, 13, 24, 42]
print(num_list)

def count_even_numbers(list):
    counter = 0
    for index, item in enumerate(list):
        if(isinstance(list[index], int)
        and (list[index] % 2) == 0):
            counter +=1
    print("\n The count of even numbers is: {0}"
          .format(counter))


count_even_numbers(num_list)


