'''Students: Meera ALshara & Syed Wasti
    Repository Links: 
    Meera: https://github.com/meeralshara/gcis123/edit/main/group3-activity4.py
    Syed: '''

import csv

INVENTORY = {}

def read_data(file_path): 
    '''Function that reads the products data from a csv file'''
    try:
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                name, price, quantity = row
                INVENTORY[name] = {'price': float(price), 'quantity': int(quantity)}
                
    except FileNotFoundError: 
        print("File not found.")

class Article: 
    '''This class represents an article that contains its name, price and quantity'''
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def _str_(self):
        return "Article: " + str(self.name) + " Quantity: " + str(self.quantity) + " Price: " + str(self.price)

class Cart:
    '''This class represents a shopping cart where the user can add, remove, display and finally checkout products'''
    def _init_(self):
        self.list_of_purchased = []
    
    def addProduct(self, name, quantity):
        if name in INVENTORY:
            available_quantity = min(quantity, INVENTORY[name]['quantity'])
            
            if any(article.get_name() == name for article in self.list_of_purchased):
                for article in self.list_of_purchased:
                    if article.get_name() == name:
                        current_quantity = article.get_quantity()
                        
                        new_quantity = min(INVENTORY[name]['quantity'], current_quantity + quantity)
                        
                        article.set_quantity(new_quantity)
                        
                        INVENTORY[name]['quantity'] -= new_quantity - current_quantity
                        
                        print("Added", quantity, "units of", name, "to the existing cart item.")
                        
                        break
            else:
                INVENTORY[name]['quantity'] -= available_quantity
                article = Article(name, INVENTORY[name]['price'], available_quantity)
                self.list_of_purchased.append(article)
                print(available_quantity, name, "added to cart.")
        else:
            print("Product not found in inventory.")


    def removeProduct(self, name, quantity):
        for article in self.list_of_purchased:
            if article.get_name() == name:
                removed_quantity = min(quantity, article.get_quantity())
                article.set_quantity(article.get_quantity() - removed_quantity)
                INVENTORY[name]['quantity'] += removed_quantity
                if article.get_quantity() == 0:
                    self.list_of_purchased.remove(article)
                print(removed_quantity, name, "removed from cart.")
                return
        print("Product not found in cart.")

    def displayCart(self):
        if not self.list_of_purchased:
            print("Cart is empty.")
            return
        print("Cart:")
        for article in self.list_of_purchased:
            print(article)

    def checkout(self):
        total = 0
        for article in self.list_of_purchased:
            price = article.get_price() * article.get_quantity()
            if article.get_quantity() >= 3:
                price *= 0.9
            total += price
        total *= 1.07
        print("Total: $", total)

def menu():
    print("Commands:")
    print("1. List - List available products")
    print("2. Cart - Display cart")
    print("3. Add - Add product to cart")
    print("4. Remove - Remove product from cart")
    print("5. Checkout - Finalize purchase")
    print("6. Exit - Quit program")

def main():
    read_data('products.csv')
    cart = Cart()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Available Products:")
            for name, details in INVENTORY.items():
                print(name, ": $", details['price'], "Quantity:", details['quantity'])
        elif choice == 2:
            cart.displayCart()
        elif choice == 3:
            name = input("Enter product name: ").strip()
            quantity = int(input("Enter quantity: "))
            cart.addProduct(name, quantity)
        elif choice == 4:
            name = input("Enter product name: ").strip()
            quantity = int(input("Enter quantity: "))
            cart.removeProduct(name, quantity)
        elif choice == 5:
            cart.checkout()
            break
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
