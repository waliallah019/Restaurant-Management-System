# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:43:57 2023

@author: Alishba Mazhar
"""

import csv
from queue import Queue

class FoodNode:
    def __init__(self, item_id, name, Category, Ingrediants, Price, rating, quantity):
        self.item_id = item_id
        self.name = name
        self.Category = Category
        self.Ingrediants = Ingrediants
        self.Price = Price
        self.rating = rating
        self.quantity = quantity
        self.next_node = None

class FoodLinkedList:
    def __init__(self):
        self.head = None

    def add_food(self, item_id, name, Category, Ingrediants, Price, rating, quantity):
        new_food = FoodNode(item_id, name, Category, Ingrediants, Price, rating, quantity)
        new_food.next_node = self.head
        self.head = new_food

def read_csv_and_store(filename):
    linked_list = FoodLinkedList()
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            linked_list.add_food(
                row['Item_ID'],
                row['Name'],
                row['Category'],
                row['Ingredients'],
                row['Price'],
                row['Rating'],
                row['Quantity']
            )
    return linked_list

class OrderQueue:
    def __init__(self):
        self.queue = Queue()
        self.bill = None

       

    def enqueOrder(self, customer_name, item_data):
        order_data = {
            'Customer_Name': customer_name,
            'Item_ID': item_data['Item_ID'],
            'Name': item_data['Name'],
            'Category': item_data['Category'],
            'Ingredients': item_data['Ingredients'],
            'Price': float(item_data['Price']),  # Convert price to float for calculations
            'Quantity': int(item_data['quantity']),  # Convert quantity to int for calculations
            'Rating': item_data['Rating']
        }
        self.queue.put(order_data)
        print(f"Order added to the queue:\n{order_data}")

    def process_orders(self):
        total_bill = 0
        while not self.queue.empty():
            order_data = self.queue.get()
            total_amount = order_data['Quantity'] * order_data['Price']
            total_bill += total_amount

        # Store the order details in the "bill.csv" file
        bill_file_path = 'bill.csv'
        with open(bill_file_path, 'a', newline='') as bill_file:
            fieldnames = ['Customer_Name', 'Item_ID', 'Total_Amount']
            bill_writer = csv.DictWriter(bill_file, fieldnames=fieldnames)

            # Check if the file is empty, write headers if needed
            if bill_file.tell() == 0:
                bill_writer.writeheader()

            # Write the order details to the bill file
            bill_writer.writerow({
                'Customer_Name': order_data['Customer_Name'],
                'Item_ID': order_data['Item_ID'],
                'Total_Amount': total_bill
            })

        print(f"Total Bill for {order_data['Customer_Name']}: ${total_bill}")

if __name__ == "__main__":
    restaurant_file = 'restaurant.csv'
    food_list = read_csv_and_store(restaurant_file)

    order_queue = OrderQueue()

    customer_name = input("Enter customer name: ")

    # Find customer and order
    current = food_list.head
    customer_found = False
    while current:
        if current.name.lower() == customer_name.lower():
            order_queue.enqueOrder(customer_name, {
                'Item_ID': current.item_id,
                'Name': current.name,
                'Category': current.Category,
                'Ingredients': current.Ingrediants,
                'Price': current.Price,
                'Rating': current.rating,
                'quantity': current.quantity  # Taking quantity from the restaurant file
            })
            customer_found = True
            break
        current = current.next_node

    if not customer_found:
        print(f"Customer '{customer_name}' not found in the restaurant file.")

    # Process orders
    order_queue.process_orders()
