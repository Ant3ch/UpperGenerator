import random

with open("result.txt", "w") as f:
    f.write(" ")


def upper_generator(text: str) -> list:
    """:return all possibility of uppercase and lower in a text(using random)"""
    list_ = []
    number_of_possibilites = 2 ** len(text) - len(text) - 1
    stop = True
    iterator =0
    while stop:
        iterator +=1
        roll = random.randint(0, len(text))
        list_text = list(text)
        for b in range(roll):
            rdm_letter = random.choice(list_text)
            list_text[list_text.index(rdm_letter)] = list_text[list_text.index(rdm_letter)].upper()
            if len(list_) >= number_of_possibilites or iterator > 10000:

                stop = False

            if "".join(list_text) not in list_:
                list_.append("".join(list_text))
            else:
                continue
    return list_

validate = False
while not validate :
    try:
        user_input = str(input("Entrez pseudo(en minuscule): "))
        validate = True
    except TypeError:
        user_input = str(input("Entrez pseudo(en minuscule): "))
        print("Entrez invalid")
        continue

with open("result.txt", "w") as f:
    for val in upper_generator(user_input):
        f.write(val + "\n")

