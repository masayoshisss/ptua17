question1 = int(input("Iveskite savo pirmaji skaiciu: "))
question2 = int(input("Iveskite antra norima skaiciu: "))
suma = question1 + question2
print("Suma yra", suma)


name = "Hello"
print(name[::-1])

num1 = input("Iveskite savo varda: ")
num2 = input("Iveskite savo pavarde: ")
suma = f"{num2}, {num1}"
print(("Jusu vardas yra: "), suma)

num1 = (input("Iveskite savo pirmojo katino varda: "))
num = (input("Parasykite kada jis numire rest in peace: "))
suma = num1 + num
print("Sveikiname jusu katino vardas yra",num1,"ir jis mire",num)


full_name = input("Įveskite savo pilną vardą: ")


space_index = full_name.find(" ")
first_name = full_name[:space_index]


first_name_upper = first_name.upper()


greeting = f"Labas, {first_name.upper()}, sveiki atvykę!"


print(greeting)
