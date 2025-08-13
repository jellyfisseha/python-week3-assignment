def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        return price * 0.8  # Apply a 20% discount
    else:
        return price  # No discount applied

# Example usage
print(calculate_discount(2500, 10))  # 2500.0 (no discount)
print(calculate_discount(2500, 20))  # 2000.0 (20% discount)

