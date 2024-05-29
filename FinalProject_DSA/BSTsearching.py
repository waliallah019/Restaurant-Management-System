import csv
import pandas as pd

class TreeNode:
    def __init__(self, item_id, name, Category, Ingrediants, Price, rating):
        self.item_id = item_id
        self.name = name
        self.Category = Category
        self.Ingrediants = Ingrediants
        self.Price = Price
        self.rating = rating
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item_id, name, Category, Ingrediants, Price, rating):
        self.root = self._insert(self.root, item_id, name, Category, Ingrediants, Price, rating)

    def _insert(self, root, item_id, name, Category, Ingrediants, Price, rating):
        if not root:
            return TreeNode(item_id, name, Category, Ingrediants, Price, rating)

        if item_id < root.item_id:
            root.left = self._insert(root.left, item_id, name, Category, Ingrediants, Price, rating)
        elif item_id > root.item_id:
            root.right = self._insert(root.right, item_id, name, Category, Ingrediants, Price, rating)

        return root

    def display_inorder(self):
        self._display_inorder(self.root)

    def _display_inorder(self, root):
        if root:
            self._display_inorder(root.left)
            print(f"Food ID: {root.item_id}, Name: {root.name}, Category: {root.Category}, Ingrediants: {root.Ingrediants}, Price: {root.Price}, Rating: {root.rating}")
            self._display_inorder(root.right)

    def search_and_store_all_to_csv(self, value, filename):
        matching_results = self._search_all(self.root, value)

        if matching_results:
            with open(filename, 'w', newline='') as csvfile:  # Use 'w' for write mode
                fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                # Write all matching rows
                for result in matching_results:
                    writer.writerow({
                        'Item_ID': result.item_id,
                        'Name': result.name,
                        'Category': result.Category,
                        'Ingredients': result.Ingrediants,
                        'Price': result.Price,
                        'Rating': result.rating
                    })

        return matching_results


    def _search_all(self, root, value):
        matching_results = []

        if root:
            if (
                str(value) == str(root.item_id)
                or value == root.name
                or value == root.Category
                or value == root.Ingrediants
                or value == root.Price
                or value == root.rating
            ):
                matching_results.append(root)

            matching_results += self._search_all(root.left, value)
            matching_results += self._search_all(root.right, value)

        return matching_results



    def to_csv(self, filename):
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['Item_ID', 'Name', 'Category', 'Ingredients', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            self._write_to_csv(writer, self.root)

    def _write_to_csv(self, writer, root):
        if root:
            self._write_to_csv(writer, root.left)
            writer.writerow({
                'Item_ID': root.item_id,
                'Name': root.name,
                'Category': root.Category,
                'Ingredients': root.Ingrediants,
                'Price': root.Price,
                'Rating': root.rating
            })
            self._write_to_csv(writer, root.right)

# Function to read data from CSV and store in BST
def read_csv_and_store_bst(filename, bst):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bst.insert(
                row['Item_ID'],
                row['Name'],
                row['Category'],
                row['Ingredients'],
                row['Price'],
                row['Rating']
            )

# Example usage
# if __name__ == "__main__":
#     bst = BinarySearchTree()
#     read_csv_and_store_bst('C:\\Users\\Track Computers\\Desktop\\DSA\\finalproject\\New folder\\resturant1.csv', bst)
#     # bst.display_inorder()
#     text='French'
#     search_result = bst.search_and_store_to_csv(text,'BSTsearchData_output.csv' )
#     if search_result:
#         print(f"Found: Food ID: {search_result.item_id}, Name: {search_result.name}, Category: {search_result.Category}, "
#               f"Ingredients: {search_result.Ingrediants}, Price: {search_result.Price}, Rating: {search_result.rating}")
#     else:
#         print("Not found.")

    # Store the BST back into a CSV file
    # bst.to_csv('BSTsearchData_output.csv')
