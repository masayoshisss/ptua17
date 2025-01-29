import random

numeris = (random.randint(0,10))
while True:
    spejimas = int(input("Atspėkite skaičių (1–10): "))
    if spejimas == numeris:
        print(f"Teisingai! Skaičius yra {numeris}.")
        break
    elif spejimas < numeris:
        print("Per mažas! Bandykite dar kartą.")
    else:
        print("Per didelis! Bandykite dar kartą.")