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

    def find_food_by_id(self, item_id):
        current = self.head
        while current:
            if current.item_id == item_id:
                return current
            current = current.next_node
        return None

class FeedbackStack:
    def __init__(self):
        self.feedback_stacks = {}

    def push(self, customer_name, feedback_data):
        if customer_name not in self.feedback_stacks:
            self.feedback_stacks[customer_name] = []

        self.feedback_stacks[customer_name].append(feedback_data)
        print("Added to stack!")

    def add_feedback(self, customer_name, feedback_id, feedback_message, review):
        feedback_data = {
            'Food_ID': feedback_id,
            'Feedback_Message': feedback_message,
            'Review': review
        }
        self.push(customer_name, feedback_data)

    def get_customer_feedback(self, customer_name):
        if customer_name in self.feedback_stacks:
            return self.feedback_stacks[customer_name]
        else:
            return f"No feedback found for customer {customer_name}"

    def write_feedback_to_csv(self, filename):
        with open(filename, 'a', newline='') as csvfile:  # Use 'w' mode to overwrite existing file
            fieldnames = ['Customer_Name', 'Food_ID', 'Feedback_Message', 'Review']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                  writer.writeheader()
            

            # Write feedback data for each customer's stack
            for customer_name, feedback_stack in self.feedback_stacks.items():
                for feedback_data in feedback_stack:  # Reverse to maintain stack order
                    feedback_data['Customer_Name'] = customer_name
                    writer.writerow(feedback_data)
    def search_and_display(self, search_key):
        matches = []

        for customer_name, feedback_stack in self.feedback_stacks.items():
            for feedback_data in feedback_stack:
            
                if any(search_key.lower() in value.lower() for value in feedback_data.values()):
                    matches.append((customer_name, feedback_data))

        if matches:
           
            for customer_name, feedback_data in matches:
                print(f"Customer Name: {customer_name}")
                print(f"Food_ID: {feedback_data['Food_ID']}")
                print(f"Feedback_Message: {feedback_data['Feedback_Message']}")
                print(f"Review: {feedback_data['Review']}")
                print()

         
            self.write_searched_data_to_csv(matches, 'searched_data.csv')
        else:
            raise ValueError(f"No matching rows found for search key '{search_key}'.")
    def pop_feedback_and_write_to_csv(self, filename):
        popped_feedback = []
        for customer_name, feedback_stack in self.feedback_stacks.items():
            while feedback_stack:
                feedback_data = feedback_stack.pop()
                feedback_data['Customer_Name'] = customer_name
                popped_feedback.append(feedback_data)

        if popped_feedback:
            with open(filename, 'a', newline='') as csvfile:
                fieldnames = ['Customer_Name', 'Food_ID', 'Feedback_Message', 'Review']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if csvfile.tell() == 0:
                    writer.writeheader()
                for feedback_data in popped_feedback:
                    writer.writerow(feedback_data)
        else:
            print("No feedback to pop and write to CSV.")
    def write_searched_data_to_csv(self, matches, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Customer_Name', 'Food_ID', 'Feedback_Message', 'Review']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for customer_name, feedback_data in matches:
                feedback_data['Customer_Name'] = customer_name
                writer.writerow(feedback_data)
    def read_csv_and_store1(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_feedback(
                    row['Customer_Name'],
                    row['Food_ID'],
                    row['Feedback_Message'],
                    row['Review']
                )          
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

if __name__ == "__main__":
    food_list = FoodLinkedList()
    feedback_stack = FeedbackStack()
    read_csv_and_store('resturant1.csv', food_list)

    # Get user input for item ID
    item_id = input("Enter the item ID: ")

    # Check if the item ID exists in the restaurant file
    food_item = food_list.find_food_by_id(item_id)
    if not food_item:
        print("Item with ID found in the restaurant file.")
    else:
    # Continue with the rest of your code (feedback) as before
          customer_name = 'fasi'  # Variable to store customer name

    # Get user input for feedback
    
          feedback_message = input("Enter your feedback message: ")
          review = input("Enter your review (out of 5): ")

    # Add feedback to the stack with the customer's name using the push method
          feedback_stack.add_feedback(customer_name, item_id, feedback_message, review)
          feedback_stack.write_feedback_to_csv('feedbacks.csv')
         
