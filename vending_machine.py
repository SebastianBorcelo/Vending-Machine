#Vending machine choices

class VendingMachine:
    def __init__(self):
        self.items = {
            'A1': {'name': 'Doritos', 'price': 7.50, 'stock': 1},
            'A2': {'name': 'Lays', 'price': 7.25, 'stock': 5},
            'A3': {'name': 'Takis', 'price': 7.00, 'stock': 2},
            'B1': {'name': 'Hersheys', 'price': 5.00, 'stock': 20},
            'B2': {'name': 'Tobleron', 'price': 8.00, 'stock': 2},
            'B3': {'name': 'Kinder', 'price': 4.00, 'stock': 12},
            'C1': {'name': 'Pepsi', 'price': 2.50, 'stock': 4},
            'C2': {'name': 'Sprite', 'price': 2.50, 'stock': 5},
            'C3': {'name': 'Water', 'price': 1.00, 'stock': 8},
        }
        self.selected_items = {}

    def display_items(self):
        print("\nAvailable items:")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']} (Stock: {item['stock']})")

    def select_item(self, code, quantity):
        if code in self.items:
            item = self.items[code]
            if item['stock'] >= quantity:
                self.selected_items[code] = {'name': item['name'], 'price': item['price'], 'quantity': quantity}
                item['stock'] -= quantity  # Reduce stock
                print(f"You have selected {quantity} x {item['name']} - ${item['price']:.2f} each.")
            else:
                print("Sorry, insufficient stock for that item.")
        else:
            print("Invalid item code.")

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.selected_items.values())
        return total

    def process_payment(self, amount, payment_method):
        total = self.calculate_total()
        if payment_method == 'cash':
            if amount >= total:
                change = amount - total
                receipt = "Receipt:\n"
                for item in self.selected_items.values():
                    receipt += f"{item['quantity']} x {item['name']} - ${item['price']:.2f} each\n"
                receipt += f"Total: ${total:.2f}"
                if change > 0:
                    receipt += f" | Change: ${change:.2f}"
                print(f"\nYou purchased:\n{receipt}")
                self.selected_items.clear()  # Clear selected items after purchase
                print("Thank you for using the vending machine! Have a great day!")
            else:
                print(f"Insufficient funds. Please insert the correct amount. Returning your cash of ${amount:.2f}.")
                return False  # Indicate insufficient funds
        elif payment_method == 'card':
            if amount >= total:
                change = amount - total
                receipt = "Receipt:\n"
                for item in self.selected_items.values():
                    receipt += f"{item['quantity']} x {item['name']} - ${item['price']:.2f} each\n"
                receipt += f"Total: ${total:.2f}"
                if change > 0:
                    receipt += f" | Change: ${change:.2f}"
                print(f"\nYou purchased:\n{receipt}")
                self.selected_items.clear()  # Clear selected items after purchase
                print("Thank you for using the vending machine! Have a great day!")
            else:
                print("Sorry, but you have an insufficient balance.")
                return False  # Indicate insufficient funds
        return True  # Indicate successful payment

def main():
    print("Welcome to the Snack Vending Machine!")
    input("Press 'Enter' to start...")  # Prompt to start the ordering process
    
    machine = VendingMachine()
    
    while True:
        machine.display_items()
        while True:
            code = input("Enter item code to purchase: ").strip().upper()
            if code in machine.items:
                break
            else:
                print("Invalid item code. Please enter a valid code.")

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                else:
                    print("Please enter a positive integer for quantity.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        machine.select_item(code, quantity)

        while True:
            more_items = input("Would you like to order something else? (yes/no): ").strip().lower()
            if more_items in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if more_items == 'no':
            break  # Exit the loop to proceed to payment

    while True:
        payment_method = input("Do you want to pay with 'cash' or 'card'? ").strip().lower()
        if payment_method in ['cash', 'card']:
            break
        else:
            print("Invalid payment method. Please enter 'cash' or 'card'.")

    while True:
        try:
            amount = float(input("Enter amount to pay: "))
            if amount >= 0:
                break
            else:
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if not machine.process_payment(amount, payment_method):
        print("Transaction failed. Please start over.")
        return  # End the prompt if the transaction fails

    # Ask if the user wants to order more after the transaction
    while True:
        more_order = input("Would you like to order more items? (yes/no): ").strip().lower()
        if more_order in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if more_order == 'yes':
        main()  # Restart the ordering process
    else:
        print("Thank you for your order! Have a great day!")

if __name__ == "__main__":
    main()
