import csv
from queue import Queue


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

class BillQueue:
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
        with open(filename, 'w', newline='') as bill_file:
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
                print(f"Bill stored in the file")

    def search_customer_bills(self, customer_name):
        searched_bills = [] 
        file_path = 'bills.csv'

        with open(file_path, 'r', newline='') as bill_file:
            reader = csv.DictReader(bill_file)
            for row in reader:
                if row['Customer_Name'] == customer_name:
                    searched_bills.append(row)
        if searched_bills:
            searched_file_path = 'searched_bills.csv'
            with open(searched_file_path, 'w', newline='') as searched_file:
                fieldnames = ['Item_ID', 'Customer_Name', 'Price', 'Quantity', 'Total_Bill']
                searched_writer = csv.DictWriter(searched_file, fieldnames=fieldnames)
                searched_writer.writeheader()
                searched_writer.writerows(searched_bills)
                print(f"Searched bills stored in the file")
        else:
            raise ValueError(f"you have paid your bill")

if __name__ == "__main__":
    food_list = FoodLinkedList()
    read_csv_and_store('resturant1.csv', food_list)

    order_queue = BillQueue()
    print("Bills processed")
    customer_name_input = input("Enter the customer name to search for bills: ")

    order_queue.search_customer_bills(customer_name_input)
