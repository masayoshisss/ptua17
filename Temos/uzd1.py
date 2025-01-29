username = "user123"
password = "securepass"

while True:
    input_username = input("Įveskite vartojo vardą: ")
    input_password = input("Įveskite slaptažodį: ")
    if input_username == username and input_password == password:
        print(f"Prisijungimas sėkmingas! Sveiki, {username}.")
        break