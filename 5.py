# Define a tuple
my_tuple = (1, 1, 1, 1)

# Use set() to get the unique items in the tuple
unique_items = set(my_tuple)

# If there is only one unique item in the set, all items in the tuple are the same
if len(unique_items) == 1:
    print("All items in the tuple are the same.")
else:
    print("Not all items in the tuple are the same.")
