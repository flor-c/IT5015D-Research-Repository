# short quiz

score = 0

print("\n Two item quiz")


def get_score(question, answer, score):
    print("/n" + question)
    user_response = input("Answer: ")
    if user_response == answer:
        score += 1
        print("Well done")
    else:
        print("Sorry, you got it wrong")
    return score


score = get_score("What i the color of the sky?", "blue", score)
score = get_score("Official language of Spain", "spanish", score)

print(\n your score: {0}.format(score))
