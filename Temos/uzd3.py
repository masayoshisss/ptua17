stored_pin = "1234"

for i in range(10000):
    pin = str(i)
    while len(pin) < 4:
        pin = "0" + pin

    if pin == stored_pin:
        print(f"Surastas PIN: {pin}")
        break