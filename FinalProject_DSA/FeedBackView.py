# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:52:25 2023

@author: Alishba Mazhar
"""
import csv

def view_feedbacks_from_stack(feedback_stack):
    print("Viewing feedbacks from the stack:")
    feedbacks_to_write = []  # Create a list to store feedbacks temporarily
    while feedback_stack:
        feedback = feedback_stack.pop()
        feedbacks_to_write.append(feedback)  # Append feedback to the list

    # Write all feedbacks to the file once
    write_to_csv('output.csv', feedbacks_to_write)


def read_output_csv(filename):
    
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Customer Name: {row['Customer_Name']}")
            print(f"Food_ID: {row['Food_ID']}")
            print(f"Feedback Message: {row['Feedback_Message']}")
            print(f"Review: {row['Review']}")

def read_feedback_csv(filename, feedback_stack):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in (list(reader)):
            feedback_stack.append(row)

            print(f"Customer Name: {row['Customer_Name']}")
            print(f"Food_ID: {row['Food_ID']}")
            print(f"Feedback Message: {row['Feedback_Message']}")
            print(f"Review: {row['Review']}")               

def write_to_csv(filename, feedbacks):
    fieldnames = ['Customer_Name', 'Food_ID', 'Feedback_Message', 'Review']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerows(feedbacks)

# Example usage
if __name__ == "__main__":
    feedback_stack = []

    # Read data from CSV into the stack
    read_feedback_csv('feedbacks.csv', feedback_stack)

    # Viewing feedbacks from the stack
    view_feedbacks_from_stack(feedback_stack)
