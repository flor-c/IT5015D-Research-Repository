from datetime import datetime

score = 0
start_time = datetime.today()

answer_one = (input("What is the capital of NZ?\n\n"))

if answer_one.lower() == "wellington":
    score = score + 1
    print("That is correct. Your score is ", score, "\n\n")
else:
    print("Incorrect. Your score is still ", score, "\n\n")

answer_two = (input("What is the Maori name for NZ?\n\n"))

if answer_two.lower() == "aotearoa":
    score = score + 1
    print("That is correct. Your score is ", score, "\n\n")
else:
    print("Incorrect. Your score is still ", score, "\n\n")

answer_three = (input("What is the name of the New Zealand Rugby team?\n\n"))

if answer_three.lower() == "all blacks":
    score = score + 1
    print("That is correct. Your score is ", score, "\n\n")
else:
    print("Incorrect. Your score is still ", score, "\n\n")

answer_four = (input("What are the official languages of NZ?\n\n"))

if answer_four.lower() == "english, maori and NZ Sing Language":
    score = score + 1
    print("That is correct. Your score is ", score, "\n\n")
else:
    print("Incorrect. Your score is still ", score, "\n\n")

print("Your final score is ", score, "\n")
print("Total time: ", datetime.today() - start_time)

