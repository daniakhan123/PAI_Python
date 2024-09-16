class Restaurant:
    def __init__(self):
        self.menu_items = {}  
        self.booked_tables = []  
        self.customer_orders = []  

    def add_item_to_menu(self):
        item_name = input("Enter the name of the menu item: ")
        item_price = float(input(f"Enter the price for {item_name}: "))
        self.menu_items[item_name] = item_price
        print(f"Added {item_name} to the menu with price {item_price}")

    def book_table(self):
        table_num = input("Enter table number to book: ")
        if table_num in self.booked_tables:
            print(f"Table {table_num} is already booked.")
        else:
            self.booked_tables.append(table_num)
            print(f"Table {table_num} has been booked.")

    def customer_order(self):
        table_num = input("Enter table number for the order: ")
        if table_num not in self.booked_tables:
            print(f"Table {table_num} is not booked.")
            return
        
        item_name = input("Enter the name of the menu item to order: ")
        if item_name not in self.menu_items:
            print(f"{item_name} is not on the menu.")
            return

        self.customer_orders.append((table_num, item_name))
        print(f"Order added: Table {table_num} - {item_name}")

    def print_menu(self):
        if not self.menu_items:
            print("The menu is currently empty.")
        else:
            print("Menu:")
            for item_name, price in self.menu_items.items():
                print(f"{item_name}: ${price:.2f}")

    def print_booked_tables(self):
        if not self.booked_tables:
            print("No tables are currently booked.")
        else:
            print("Booked Tables:")
            for table in self.booked_tables:
                print(f"Table {table}")

    def print_customer_orders(self):
        if not self.customer_orders:
            print("No customer orders yet.")
        else:
            print("Customer Orders:")
            for table_num, item_name in self.customer_orders:
                print(f"Table {table_num}: {item_name}")


rest = Restaurant()


rest.add_item_to_menu()
rest.add_item_to_menu()

rest.book_table()
rest.book_table()

rest.customer_order()
rest.customer_order()

rest.print_menu()
rest.print_booked_tables()
rest.print_customer_orders()
