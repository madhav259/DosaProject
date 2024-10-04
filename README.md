# DosaProject
## Project Overview

This project reads JSON data from a file (e.g., a file containing orders), processes the data to extract customer information and item details, and then writes the results to two separate JSON files:

customers.json: Contains a mapping of customer phone numbers to their names.

items.json: Contains a list of items ordered, their price, and the total number of times each item has been ordered.

This program is designed to be efficient, using Python's built-in libraries and data structures to manage and process the data effectively.

## Design

### Input:
A JSON file containing an array of orders. Each order includes customer information (name and phone number) and the list of items they purchased. Each item has a name, price, and other potential attributes.

### Output:
1.customers.json: This file contains a dictionary where the keys are customer phone numbers and the values are the corresponding customer names.

2.items.json: This file contains a dictionary where the keys are item names and the values are dictionaries with the price of the item and the number of orders that included that item.


## Prerequisites:
Python 3.x installed on your machine.
### Instructions:
1.Place the JSON input file in the project directory: Ensure you have a valid JSON file (e.g., example_orders.json) in the project directory. This file should contain the orders in the correct format.

2.Run the Python Script: You can run the script using the following command:

        "python3 midproject.py example_orders.json"

3.Check the Output: After running the script, you will find two output files in the project directory:

customers.json: Contains the customer information.

items.json: Contains the item information, including item price and the number of orders for each item.

