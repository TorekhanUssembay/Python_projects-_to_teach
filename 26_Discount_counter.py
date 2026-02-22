def apply_discount(cart_total):
    if cart_total < 0:
        return None 
    elif cart_total < 50:
        discount = 0
    elif cart_total < 100:
        discount = 5
    elif cart_total < 200:
        discount = 10
    else:
        discount = 15

    final_price = cart_total * (1 - discount / 100)
    return final_price, discount


def main():
    try:
        cart_total = float(input("Enter cart total: "))
        result = apply_discount(cart_total)

        if result is None:
            print("Invalid cart total.")
        else:
            final_price, discount = result
            print(f"Discount applied: {discount}%")
            print(f"Final price: ${final_price:.2f}")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
