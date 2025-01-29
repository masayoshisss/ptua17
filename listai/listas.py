# Įgyvendinkite paprastą žodyną, kuris saugo žodžius ir jų reikšmes. Leiskite vartotojui įvesti žodį ir atspausdinkite jo reikšmę.

# Užduoties instrukcijos:

# Iš anksto užpildykite žodyną keliais žodžiais ir jų reikšmėmis.

# Prašykite vartotojo įvesti žodį, kol ji nuspręs sustoti.

# Atspausdinkite žodžio reikšmę arba klaidą, jei žodyne nėra tokio žodžio.

# Pavyzdinis žodynas galėtų būti toks:


# dictionary = {
#     "obuolys": "vaisius, augantis ant medžių",
#     "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
#     "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
# }
# Pavyzdinė įvestis / išvestis:


# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): obuolys
# Žodžio obuolys reikšmė: vaisius, augantis ant medžių.
# Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): automobilis
# # Šio žodžio mūsų žodyne nėra.
# # Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): pabaiga

#value = print(my_dict["name"])

definitions = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

while True:
      user_imput = input("Write your word to get its meaning (Write end if you want to end the program) ")      
      if user_imput.lower() == "end":
         print("Program ended")
         break
      if user_imput in definitions:
           print(f"Žodžio {user_imput} reikšmė: {definitions[user_imput]}")
           break  
      else:
           print("We dont have this word in our library")

    

# while True:
#     input_username = input("Įveskite vartojo vardą: ")
#     input_password = input("Įveskite slaptažodį: ")
#     if input_username == username and input_password == password:
#         print(f"Prisijungimas sėkmingas! Sveiki, {username}


