# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 01:01:57 2023

@author: Alishba Mazhar
"""

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
class OrderQueue:
    def __init__(self):
        self.queue = Queue()
        self.order_number = 1  # Initialize order number counter

    def enqueOrder(self, customer_name, item_data, quantity):
        order_data = {
            
            'Customer_Name': customer_name,
            'Item_ID': item_data['Item_ID'],
            'Name': item_data['Name'],
            'Category': item_data['Category'],
            'Ingredients': item_data['Ingredients'],
            'Price': item_data['Price'],
            'Quantity': quantity,
            'Rating': item_data['Rating']
        }
        self.queue.put(order_data)
        print(f"Order added to the queue:\n{order_data}")
        # Increment order number

    # ... (rest of the class remains unchanged)

    def remove_order(self, item_id):
        # Remove order from the queue
        temp_queue = Queue()
        while not self.queue.empty():
            order_data = self.queue.get()
            if order_data['Item_ID'] != item_id:
                temp_queue.put(order_data)
        self.queue = temp_queue

        # Remove order from the file
        file_path = 'restaurant_orders.csv'
        with open(file_path, 'r', newline='') as order_file:
            reader = csv.DictReader(order_file)
            rows = [row for row in reader if row['Item_ID'] != item_id]

        with open(file_path, 'w', newline='') as order_file:
            fieldnames = ['Customer_Name', 'Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Quantity', 'Rating']
            order_writer = csv.DictWriter(order_file, fieldnames=fieldnames)
            order_writer.writeheader()
            order_writer.writerows(rows)


    def process_orders(self):
        # Process orders from the queue and update the restaurant file
        while not self.queue.empty():
            order_data = self.queue.get()
            file_path = 'restaurant_orders.csv'
            
            with open(file_path, 'a', newline='') as order_file:
                fieldnames = [ 'Customer_Name', 'Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Quantity', 'Rating']
                order_writer = csv.DictWriter(order_file, fieldnames=fieldnames)
                
                # Check if the file is empty, write headers if needed
                if order_file.tell() == 0:
                    order_writer.writeheader()
    
                order_writer.writerow(order_data)

if __name__ == "__main__":
    food_list = FoodLinkedList()
    read_csv_and_store('resturant1.csv', food_list)

    order_queue = OrderQueue()

    # Get user input for item ID
    item_id = input("Enter the item ID you want to order: ")
    quantity = input("Enter quantity: ")

    # Search for the item ID in the restaurant file
    current = food_list.head
    while current:
        if current.item_id == item_id:
            # Found the item, add its data to the order queue
            order_queue.enqueOrder('John Doe', {
                'Item_ID': current.item_id,
                'Name': current.name,
                'Category': current.Category,
                'Ingredients': current.Ingrediants,
                'Price': current.Price,
                'Rating': current.rating
            }, quantity)
            break
        current = current.next_node
    else:
        print("Item with ID not found in the restaurant file.")

    # Move the process_orders outside the loop
    order_queue.process_orders()
