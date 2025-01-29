#Write functions that:
#Makes basic math calculations,
#Converts Celsius from faranheit.
#Calculate average speed in meters/sec .Distance is given in Km and time in hours.
#Test all the functions. Prints should be clear and precise.

#def my_function():

#    return 2 + 2


#my_val = my_function()

#print(my_val)


#def add_three_numbers(a, b, c):
#    num_sum = a + b + c
#    return num_sum * 52


#my_val = add_three_numbers(2, 2, 2)
#print(my_val)

#my_val_sec = add_three_numbers(89, 52, 567)
#print(my_val_sec)

def addition(value1, value2):
    calculate = value1 + value2
    return calculate
answer = addition(10, 10)
print(answer)

def substraction(value1, value2):
    calculate = value1 - value2
    return calculate
answer = substraction(20, 10)
print(answer)

def multiplication(value1, value2):
    calculate = value1 * value2
    return calculate
answer = multiplication(2, 5)
print(answer)

def division(value1, value2):
    calculate = value1 / value2
    return calculate
answer = division(20, 10)
print(answer)

def exponentiation(value1, value2):
    calculate = value1 ** value2
    return calculate
answer = exponentiation(5, 10)
print(answer)

def convert(farenheit, b, c):
    calculate_temperature = farenheit * b / c
    return calculate_temperature
temperature = convert(34, 5, 9)
print(temperature)

def speed(converted_kilometers, converted_hours):
    calculate_meters = converted_kilometers / converted_hours
    return calculate_meters
average_meters_per_sec = speed(10000, 7200)
print(average_meters_per_sec)