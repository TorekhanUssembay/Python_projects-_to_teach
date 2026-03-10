class Product:
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
    
        def __str__(self):
            return f"{self.name} ${self.price.2f}"

class Cart:
    def __niit__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
    
    def remove_product(self, product_name: str):
        self.product = [
            product for product in self.products
            if product.name != product_name
        ]

    def calculate_total(self) -> float:
        return sum(product.price for product in self.products)

    def print_summary(self):
        if not self.products:
            print("Cart is empty")
            return
        
        print("Cart summary")

        for product in self.products:
            print(product)

        print(f"Total: ${self.calculate_total():.2f}")

class Order:
    def __init__(self, cart: Cart):
        if not cart.products:
            raise ValueError("Cannot create order from empty cart")

        self.products = cart.products.copy()
        self.total = cart.calculate_total 

    def print_order(self):
        print("Order summary")

        for product in self.products:
            print(product)
        
        print(f"Total Paid: ${self.total:.2f}")

p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 50)
p3 = Product("Keyboard", 100)

cart = Cart()

cart.add_pdroduct(p1)
cart.add_pdroduct(p2)
cart.add_pdroduct(p3)

cart.print_summary()

cart.remove_product("Mouse")

print()

cart.print_summary()

order = Order(cart)

print()
order.print_order()