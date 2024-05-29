import csv
from queue import Queue

# ... (previous code remains unchanged)

class FoodNode:
    def __init__(self, item_id, name, Category, Ingrediants, Price, rating):
        self.item_id = item_id
        self.name = name
        self.Category = Category
        self.Ingrediants = Ingrediants
        self.Price = Price
        self.rating = rating
        self.next_node = None

class FoodLinkedList:
    def __init__(self):
        self.head = None

    def add_food(self, item_id, name, Category, Ingrediants, Price, rating):
        new_food = FoodNode(item_id, name, Category, Ingrediants, Price, rating)
        new_food.next_node = self.head
        self.head = new_food

def read_csv_and_store(filename, linked_list):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            linked_list.add_food(
                row['Item_ID'],
                row['Name'],
                row['Category'],
                row['Ingredients'],
                row['Price'],
                row['Rating']
            )

class ManageQueue:
    def __init__(self):
        self.bill_queue = Queue()
        self.order_number = 1

    def calculate_total_bill(self, order_data):
        price = float(order_data['Price'])
        quantity = int(order_data['Quantity'])
        total_bill = price * quantity
        order_data['Total_Bill'] = total_bill
        self.bill_queue.put(order_data)

    def store_bills_in_csv(self, filename):
        with open(filename, 'w', newline='') as bill_file:  # Use 'w' mode for write (overwrites existing file)
            fieldnames = ['Item_ID', 'Customer_Name', 'Price', 'Quantity', 'Total_Bill']
            bill_writer = csv.DictWriter(bill_file, fieldnames=fieldnames)

            bill_writer.writeheader()

            while not self.bill_queue.empty():
                bill_data = self.bill_queue.get()
                bill_writer.writerow({
                    'Item_ID': bill_data['Item_ID'],
                    'Customer_Name': bill_data['Customer_Name'],
                    'Price': bill_data['Price'],
                    'Quantity': bill_data['Quantity'],
                    'Total_Bill': bill_data['Total_Bill']
                })
                print(f"Bill stored in the file:\n{bill_data}")
    def remove_bill(self, item_id):
        # Remove bill from the queue
        temp_queue = Queue()
        while not self.bill_queue.empty():
            bill_data = self.bill_queue.get()
            if bill_data['Item_ID'] != item_id:
                temp_queue.put(bill_data)
        self.bill_queue = temp_queue

        # Remove bill from the file
        file_path = 'bills.csv'
        with open(file_path, 'r', newline='') as bill_file:
            reader = csv.DictReader(bill_file)
            rows = [row for row in reader if row['Item_ID'] != item_id]

        with open(file_path, 'w', newline='') as bill_file:
            fieldnames = ['Item_ID', 'Customer_Name', 'Price', 'Quantity', 'Total_Bill']
            bill_writer = csv.DictWriter(bill_file, fieldnames=fieldnames)
            bill_writer.writeheader()
            bill_writer.writerows(rows)        

        file_path = 'restaurant_orders.csv'
        with open(file_path, 'r', newline='') as order_file:
            reader = csv.DictReader(order_file)
            rows = [row for row in reader if row['Item_ID'] != item_id]

        with open(file_path, 'w', newline='') as order_file:
            fieldnames = ['Customer_Name', 'Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Quantity', 'Rating']
            order_writer = csv.DictWriter(order_file, fieldnames=fieldnames)
            order_writer.writeheader()
            order_writer.writerows(rows)      
    def writefile(self):
        file_path = 'restaurant_orders.csv'
        with open(file_path, 'r', newline='') as order_file:
            reader = csv.DictReader(order_file)
            for row in reader:
                self.calculate_total_bill({
                    'Item_ID': row['Item_ID'],
                    'Customer_Name': row['Customer_Name'],
                    'Price': row['Price'],
                    'Quantity': row['Quantity'],
                })

        # Store the calculated bills in the CSV file (overwrite existing file)
        self.store_bills_in_csv('bills.csv')

           

if __name__ == "__main__":
    food_list = FoodLinkedList()
    read_csv_and_store('resturant1.csv', food_list)

    order_queue = ManageQueue()

    order_queue.writefile()
 
