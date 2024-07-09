# Gordon Andric
# Programming
# 23 Oct 10
# I'm Amazing Bonus
# Create a tipper program 

print("Thank you for dining at Larry's Restaurant")

meal_price = float(input("Please enter the total bill for your meal (In $): "))

tip_percentage = float(input("Would you like to leave a 15%, 20%, or custom tip (in %): "))

tip = meal_price * (tip_percentage / 100)

total_price = meal_price + tip

print(f"The price for your meal, including a {tip_percentage}% tip, will be ${total_price:.2f}")

input("\n\nPress the enter key to exit")