import random
number = str(random.randint(0, 11))

while True:
    devin = input("choisi un nombre entre 1 et 10 : ")

    if devin < number:
        print("c'est plus grand")

    if devin > number:
        print("c'est plus petit")

    if devin == number:
        print("bravo !")

