naryste = input("Ar jus esate musu bibliotekos narys? (taip/ne): ").lower()

if naryste == "taip":
    amzius = int(input("Irasykite savo amziu: "))
    if amzius >= 12:
        print("Jus galite skolintis visas knygas")
    else:
        palyda = input("Ar jus lydi suauges asmuo? (taip/ne)").lower()
        if palyda == "taip":
            print("Jus galite skolintis visas knygas")
        else:
            print("Jus galite skolintis tik vaiku knygas")
else:
    print("Jus neturite narystes ir negalite skolintis jokiu knygu")