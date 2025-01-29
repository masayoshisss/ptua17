vardas = input("Iveskite savo varda: ")
pavarde = input("Iveskite savo pavarde: ")
amzius = int(input("Iveskite savo amziu: "))
if amzius > 21:
    print(f"Sveikiname{vardas}{pavarde}, jums leidziama gamblinti is savo buto")
else:
    print("Jus esate nepilnametis ir zaisti negalite")