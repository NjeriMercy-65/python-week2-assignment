def calculate_discount(price, discount_percent):
  """Calculates the final price after discount (if 20% or more)."""
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount
  else:
    return price

# Get user input
try:
  price = float(input("Enter the original price: "))
  discount = float(input("Enter the discount percentage: "))

  final_price = calculate_discount(price, discount)

  if final_price == price:
    print(f"No discount. Final price: {final_price:.2f} Kenyan Shillings")
  else:
    print(f"Discounted price: {final_price:.2f} Kenyan Shillings")

except ValueError:
  print("Invalid input. Please enter numbers.")