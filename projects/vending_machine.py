"""
You are tasked with creating a Python program that simulates a vending machine. The vending machine should have the
following functionality:

1. The vending machine should have a list of available items, with their prices and quantities.
2. The user should be able to insert money into the vending machine and see their current balance.
3. The user should be able to select an item from the list of available items, and the vending machine should check if
they have enough money to purchase the item. If they do, the vending machine should subtract the cost of the item from
the user's balance and give them the item. If not, the vending machine should display a message saying they do not have
enough money.
4. The user should be able to request a refund of their remaining balance at any time.
5. The vending machine should keep track of the total amount of money earned and the total number of items sold.
"""


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class VendingMachine:
    def __init__(self):
        self.items = []
        self.total_earnings = 0
        self.total_items_sold = 0

    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)

    @staticmethod
    def check_balance(self, customer):
        return customer.balance

    def purchase(self, customer, item_name):
        item = next((i for i in self.items if i.name == item_name), None)
        if item and item.quantity > 0 and customer.balance >= item.price:
            customer.balance -= item.price
            item.quantity -= 1
            self.total_earnings += item.price
            self.total_items_sold += 1
            return f"Successfully purchased {item.name} for {item.price}."
        elif not item:
            return "Invalid item."
        elif item.quantity <= 0:
            return "Item out of stock."
        else:
            return "You have no money."


    def refund(self, customer):
        refund = customer.balance
        customer.balance = 0
        return (
            refund,
            f"We are sorry for the inconvenience."
        )


class Customer:
    def __init__(self):
        self.balance = 0
        self.purchase_history = []

    def insert_money(self, amount):
        self.balance += amount

    def add_to_history(self, item_name, cost):
        self.purchase_history.append((item_name, cost))


def main():
    vending_machine = VendingMachine()
    vending_machine.add_item("Soda", 2.00, 10)
    vending_machine.add_item("Chips", 1.50, 5)
    vending_machine.add_item("Chocolate bar", 1.00, 7)

    customer = Customer()

    while True:
        print("1. Insert money")
        print("2. Check balance")
        print("3. Purchase item")
        print("4. Request refund")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = float(input("Enter amount to insert: "))
            customer.insert_money(amount)
            print(f"Current balance: {customer.balance}")
        elif choice == 2:
            print(f"Current balance: {customer.balance}")
        elif choice == 3:
            item_name = input("Enter item name: ")
            result = vending_machine.purchase(customer, item_name)
            if "Successfully" in result:
                customer.add_to_history(item_name, vending_machine.items[vending_machine.items.index(next((i for i in \
                                        vending_machine.items if i.name == item_name), None))].price)
            print(result)
        elif choice == 4:
            refund = vending_machine.refund(customer)
            print(f"Refunded {refund}.")
        elif choice == 5:
            print("Total Earnings: ", vending_machine.total_earnings)
            print("Total items sold: ", vending_machine.total_items_sold)
            print("Purchase history: ", customer.purchase_history)
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
