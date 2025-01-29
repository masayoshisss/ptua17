#Create 3 separate list . One list contains shopt items, another list - prices, and last list 
#amount.
#Ask user to enter the number of item baskets she/he wants to create (min 5 buckets).
#Basket is created randomly picking one value from each list (items,price,amount)
#Example bucket = {"item":toy, "price": 35, "amount": 56}
#Created buckets are put in a final list.
#Print the buckets index on the final list witch contains most expensive items.
#Which item is with lowest price? Which item has most monetary value in store?
#There can be only different items on the final list (can't be same item in different buckets)
#my_list = [{"a" : 1}, 2, "a", [1, 2, 3, ["a", "b", "c"]]]
import random

items_list = ["apple", "cabbage", "pineapple", "bread", "beer", "banana", "meat", "beef", "chicken", "juice"]
prices_list = [3, 4, 5, 7, 2, 1, 10, 34, 12, 9, 12]
quantity = [50, 40, 15, 20, 100, 30, 10, 1, 2, 3, 4]


while True:
        baskets_quantity = int(input("How many baskets would you like me to generate? 5-10 "))
        final_list = []
        if baskets_quantity <5 or baskets_quantity >10:
            print("Netinkamas skaicius, turi but nuo 5 iki 10")



        else:   
            for i in range(baskets_quantity):
                randomized_item = random.choice(items_list)
                price_index = int(items_list.index(randomized_item))
                basket = {"item":randomized_item, "Price":prices_list[price_index], "Quantity":random.choice(quantity)}
                items_list.remove(randomized_item)
                final_list.append(basket)
        print(final_list)
        break


highest_value = max(d["Price"] for d in final_list)
final_price_list = [d['Price'] for d in final_list]
index_of_highest = final_price_list.index(highest_value)
print(f"Index of the final list that contains the must expensive item is {index_of_highest}")

lowest_value = min(d["Price"] for d in final_list)
cheapest_progress = final_price_list.index(lowest_value)
cheapest_indeed = final_list[cheapest_progress]
print(f"The cheapest is {cheapest_indeed["item"]}")

min_price = None
min_item = None
print(final_list)
for basket in final_list:
    price = basket["Price"]
    item = basket["item"]
    if min_price ==None:
         min_price = price
    elif price <min_price:
        min_price = price
        min_item = item

print(f"Lowest price is {min_price}, and the cheapest item is {min_item}")

max_price = 0
index_of_max_price = None
items_name = None
for index, basket in enumerate(final_list):
    price = basket["Price"]
    item = basket["item"]
    if price >max_price:
        max_price = price
        items_name = item
        index_of_max_price = index

        
print(f"Index of the basket that has the most expensive item is {index_of_max_price}, it's price is {max_price}, and that item is {items_name}")
