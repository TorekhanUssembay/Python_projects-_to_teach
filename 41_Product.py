class Product:
    def __init__(self, name: str, price: float, tax_rate: float):
        if price < 0:
            raise ValueError("Price can not be negative")
        
        if tax_rate < 0:
            raise ValueError("Tax rate must be positive number")
        
        self.name = name
        self.price = price
        self.tax_rate = tax_rate

    def calculate_price_with_tax(self) -> float:
        return self.price * (1 + self.tax_rate)

    def apply_discount(self, percent: float):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount amount")

        dicount_amount = self.price * (percent / 100)
        self.price -= discount_amount

def main():

    product = Product("Laptop", 1000, 0.10)

    print("Product:", product.name)
    print("Base price: ", product.price)

    price_with_tax = product.calculate_price_with_tax()
    print("Price with tax: ", price_with_tax)

    product.apply_discount(20)
    print("Price with discount: ", product.price)
    print("Price after discount with:", calculate_price_with_tax)        


if __name__ == "__main__":
    main()