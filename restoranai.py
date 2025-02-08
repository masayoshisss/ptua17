while True:
    try:
        number_of_restaurants = int(input("Enter the number of restaurants: "))
        if number_of_restaurants > 0:
            print("Thank you, you can proceed!")
            break
        elif number_of_restaurants == 0:
            print("Please put a positive number!")
    except ValueError:
        print("Please put a number!")

restaurants = []

for _ in range(number_of_restaurants):
    restaurant_name = input("Enter the name of the restaurant: ")
    while True:
        try:
            rating = float(input("Enter the rating of the restaurant: "))
            if rating < 1.0 or rating > 5.0:
                print("Please enter a number from 1.0 to 5.0")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the rating.")
    restaurants.append({f"restaurant_name": restaurant_name, "rating": rating})

while True:
    try:
        minimum_rating = input("Enter the minimum rating (Or leave the blank it will be set to 4.0): ")
        if minimum_rating == "":
            minimum_rating = 4.0
        else:
            minimum_rating = float(minimum_rating)
            if minimum_rating < 1.0 or minimum_rating > 5.0:
                print("Please enter a number from 1.0 to 5.0")
                continue
        break
    except ValueError:
        print("Please enter a valid number for the minimum rating.")

restaurants = sorted(restaurants, key=lambda x: x["restaurant_name"])

print("These are the restaurants that meet your rating criteria:")

found = False
for restaurant in restaurants:
    if restaurant["rating"] >= minimum_rating:
        print(f"{restaurant['restaurant_name']} - {restaurant['rating']}")
        found = True

if not found:
    print("No restaurants meet your rating criteria.")

    



