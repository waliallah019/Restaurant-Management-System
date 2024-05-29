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

    def delete_menu_item(self, item_id_to_delete):
        current = self.head
        previous = None

        while current:
            if current.item_id == item_id_to_delete:
                if previous is None:
                    self.head = current.next_node
                else:
                    previous.next_node = current.next_node
                print(f"Menu item with ID {item_id_to_delete} deleted.")
                break

            previous = current
            current = current.next_node

        else:
            print(f"Menu item with ID {item_id_to_delete} not found.")
            return

        # Write the updated linked list to the CSV file
        with open('resturant1.csv', mode='w', newline='') as csvfile:
            fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            current = self.head
            while current:
                writer.writerow({
                    'Item_ID': current.item_id,
                    'Name': current.name,
                    'Category': current.category,
                    'Ingredients': current.ingredients,
                    'Price': current.price,
                    'Rating': current.rating
                })
                current = current.next_node

# Read data from CSV and store in linked list
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

# Example usage
if __name__ == "__main__":
    food_list = FoodLinkedList()

    # Read data from CSV into the linked list
    read_csv_and_store('resturant1.csv', food_list)

  

    # Deleting a menu item
    item_id_to_delete = '23'
    food_list.delete_menu_item(item_id_to_delete)

   


    # Displaying the list after deletion
    print("After deletion:")
    # Assuming you have a 'display_foods' method in your FoodLinkedList class, uncomment the next line if you have it.
    food_list.display_foods()