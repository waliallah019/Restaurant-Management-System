
import csv

class FoodNode:
    def __init__(self, item_id, name, Category, Ingrediants, Price, rating):
        self.item_id = item_id
        self.name = name
        self.Category = Category
        self.Ingrediants =Ingrediants
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

    def display_foods(self):
       current = self.head
       while current:
         print(f"Food ID: {current.item_id}, Name: {current.name}, Category: {current.Category}, Ingrediants: {current.Ingrediants}, Price: {current.Price}, Rating: {current.rating}")
         print('\n')
         current = current.next_node
    def item_id_exists(self, item_id):
        current = self.head
        while current:
            if current.item_id == item_id:
                return True
            current = current.next_node
        return False



    def add_menu_item(self, item_id, name, Category, Ingrediants, Price, rating):
        new_menu_item = FoodNode( item_id, name, Category, Ingrediants, Price, rating)

        if not self.head:
          
            self.head = new_menu_item
        else:
       
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_menu_item
            
        with open('C:\\Users\\Track Computers\\Desktop\\DSA\\finalproject\\New folder\\resturant1.csv', 'a', newline='') as csvfile:
            fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'Item_ID': new_menu_item.item_id,
                'Name': new_menu_item.name,
                'Category': new_menu_item.Category,
                'Ingredients': new_menu_item.Ingrediants,
                'Price': new_menu_item.Price,
                'Rating': new_menu_item.rating
            })
# Read data from CSV and store in linked list
def read_csv_and_store(filename, linked_list):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Reading row: {row}")
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
    read_csv_and_store('C:\\Users\\Track Computers\\Desktop\\DSA\\finalproject\\New folder\\resturant1.csv', food_list)
    # food_list.display_foods()
    food_list.add_menu_item('490', 'burger', 'fastfood', 'shimla mirxh ,sauces', '299', '4')

    food_list.display_foods()