#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price."""
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount_percent)
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")