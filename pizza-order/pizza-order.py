# welcome the user to the program
print("Welcome, what would you like to order today")
total_bill =  0
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# display the price of each pizza 
print(f"small pizza is: ${small_pizza}\nmedium pizza is: ${medium_pizza}\nlarge pizza is : ${large_pizza}")

# ask for the user order
user_order = input("What type of pizza will you like to order s for small,m for medium,l for large:\n").lower()
ask_pepperoni = input("Would you like pepperoni(y for yes/n for no)\n").lower()
ask_cheese = input("Would you like cheese (y for yes/n for no)\n").lower()

#check the user order
if user_order == "s":
    total_bill += small_pizza
    if ask_pepperoni == "y":
        total_bill += 2
else:
    if user_order == "m":
        total_bill += medium_pizza
    else:
        total_bill += large_pizza
        
    if ask_pepperoni == "y":
        total_bill += 3

if ask_cheese == "y":
    total_bill += 1

print(f"Your total bill is ${total_bill}")