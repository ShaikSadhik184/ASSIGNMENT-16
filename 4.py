# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Print the original tuples
print("Original Tuple 1:", tuple1)
print("Original Tuple 2:", tuple2)

# Swap the tuples by unpacking and re-packing their values
tuple1, tuple2 = tuple2, tuple1

# Print the swapped tuples
print("Swapped Tuple 1:", tuple1)
print("Swapped Tuple 2:", tuple2)
