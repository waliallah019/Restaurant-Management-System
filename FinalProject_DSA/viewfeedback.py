class FeedNode:
    def __init__(self,feedback):
        self.feedback = feedback
        self.next_node = None

class FeedLinkedList:
    def __init__(self):
        self.head = None
        self.feedback_stack = []  # Stack for storing feedbacks

    def add_feed(self,  feedback):
        new_feed = FeedNode(feedback)
        new_feed.next_node = self.head
        self.head = new_feed

    def view_feedbacks(self):
        for feedback in reversed(self.feedback_stack):
            print(f"Customer Feedback: {feedback}")
            print('\n')


# Example usage
if __name__ == "__main__":
    feed_list = FeedLinkedList()

    # Read data from CSV into the linked list
    read_csv_and_store('C:\\Users\\Alishba Mazhar\\Downloads\\resturant2.csv', food_list)

    # Adding feedback to the stack
    item_id_to_add_feedback = '473'
    feedback_to_add = "Great food! Excellent service!"
    food_list.add_feedback_to_stack(item_id_to_add_feedback, feedback_to_add)

    # Viewing feedbacks from the stack
    print("Customer Feedbacks:")
    food_list.view_feedbacks()
