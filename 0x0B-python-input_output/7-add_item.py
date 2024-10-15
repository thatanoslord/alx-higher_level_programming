#!/usr/bin/python3
import sys
import os

# Import the required functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename for the JSON file
filename = "add_item.json"

# Try to load the existing data from the file, if it exists
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all the command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
