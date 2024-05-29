import csv

class FoodNode:
    def __init__(self, item_id, name, category, ingredients, price, rating):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.price = price
        self.rating = rating
        self.next_node = None

class FoodLinkedList:
    def __init__(self):
        self.head = None

    def add_food(self, item_id, name, category, ingredients, price, rating):
        new_food = FoodNode(item_id, name, category, ingredients, price, rating)
        new_food.next_node = self.head
        self.head = new_food
        
    
    def display_foods(self):
        current = self.head
        while current:
            print(f"Food ID: {current.item_id}, Name: {current.name}, Category: {current.category}, "
                  f"Ingredients: {current.ingredients}, Price: {current.price}, Rating: {current.rating}")
            print('\n')
            current = current.next_node

 
    def update_menu_item(self, item_id_to_update, new_data):
        current = self.head
        found = False

        while current:
            if current.item_id == item_id_to_update:
                current.name = new_data.get('Name', current.name)
                current.category = new_data.get('Category', current.category)
                current.ingredients = new_data.get('Ingredients', current.ingredients)
                current.price = new_data.get('Price', current.price)
                current.rating = new_data.get('Rating', current.rating)

                print(f"Menu item with ID {item_id_to_update} updated.")
                found = True
                break  

            current = current.next_node

        if found:
            menu_items = []
            with open('C:\\Users\\Track Computers\\Desktop\\DSA\\finalproject\\New folder\\ResTest.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                menu_items = list(reader)

            for item in menu_items:
                if item['Item_ID'] == item_id_to_update:
                    item.update({
                        'Name': new_data.get('Name', item['Name']),
                        'Category': new_data.get('Category', item['Category']),
                        'Ingredients': new_data.get('Ingredients', item['Ingredients']),
                        'Price': new_data.get('Price', item['Price']),
                        'Rating': new_data.get('Rating', item['Rating'])
                    })

          
            with open('C:\\Users\\Track Computers\\Desktop\\DSA\\finalproject\\New folder\\ResTest.csv', 'w', newline='') as csvfile:
                fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                # Write the updated list
                writer.writerows(menu_items)

            return

        # If the loop completes without finding the item
        print(f"Menu item with ID {item_id_to_update} not found.")
        return


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



            
# # Example usage
# if __name__ == "__main__":
#     food_list = FoodLinkedList()

#     # Read data from CSV into the linked list
#     read_csv_and_store('C:\\Users\\Track Computers\\Desktop\\DSA\\finalproject\\New folder\\ResTest.csv', food_list)

#     # Updating a menu item
#     item_id_to_update = '101'           
#     new_data = { 'Name': 'shuwarma', 'Price': '15.99', 'Rating': '4.5','Ingredients': 'My own'}
#     food_list.update_menu_item(item_id_to_update, new_data)

#     # Displaying the list after update
#     print("After update:")
#     food_list.display_foods()





