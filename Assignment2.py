def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if 20% or higher."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

if __name__ == "__main__":
    try:
        print("Welcome to the Discount Calculator!")
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        if discount_percent >= 20:
            print(f"Discount of {discount_percent:.2f}% applied. Final price: {final_price:.2f}")
        else:
            print(f"No discount applied. Final price: {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
