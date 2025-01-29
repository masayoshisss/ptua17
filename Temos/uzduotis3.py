pirmasskaicius = float(input("Iveskite savo pirma norima skaiciu: "))
simbolis = (input("Iveskite simboli su kuriuo noretumet atlikti matematini veiksma: "))
antrasskaicius = float(input("Iveskite savo antra norima skaiciu: "))
result = None

if  simbolis == "+":
    result = {pirmasskaicius + antrasskaicius}
elif simbolis == "-":
    result = {pirmasskaicius - antrasskaicius}
elif simbolis == "/":
    result = {pirmasskaicius / antrasskaicius}
elif simbolis == "*":
    result = {pirmasskaicius * antrasskaicius}
print(f"{pirmasskaicius}{simbolis}{antrasskaicius} rezultatas yra {result}")
