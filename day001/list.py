# Day 2: List Practice Exercises
# Author: Anisha Rifa Thahir

# 1️⃣ Create a list of grocery items
groceries = ["milk", "eggs", "bread", "butter", "rice"]
print("Grocery List:", groceries)

# 2️⃣ Access individual elements
print("First item:", groceries[0])
print("Last item:", groceries[-1])

# 3️⃣ Add and remove items
groceries.append("sugar")  # add new item at end
groceries.remove("bread")  # remove an item
print("Updated List:", groceries)

# 4️⃣ Loop through the list
print("Items one by one:")
for item in groceries:
    print("-", item)

# 5️⃣ Check if an item exists
if "milk" in groceries:
    print("Milk is in the list!")

# 6️⃣ Find the length of the list
print("Total items:", len(groceries))