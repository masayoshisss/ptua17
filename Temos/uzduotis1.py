pirmasnumeris = float(input("Iveskite pirmaji skaiciu: "))
antrasnumeris = float(input("Iveskite antraji skaiciu: "))

if pirmasnumeris > antrasnumeris:
    print(f"Didesnis skaicius yra {pirmasnumeris}")
elif pirmasnumeris == antrasnumeris:
    print("Numeriai yra lygus")
else:
    print("Jusu numeris deja buvo mazesnis")