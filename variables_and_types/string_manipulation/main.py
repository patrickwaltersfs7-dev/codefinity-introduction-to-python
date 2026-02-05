grocery_items = "milk cheese bread apples oranges chicken"

# 1. Extract dairy and bakery items via slicing
dairy1 = grocery_items[0:4]    # 'milk'
dairy2 = grocery_items[5:11]   # 'cheese'
bakery1 = grocery_items[12:17] # 'bread'

# 2. Concatenate into the required message
message = (
    "We have dairy and bakery items: "
    + dairy1 + ", "
    + dairy2 + ", and "
    + bakery1
    + " in aisle 5"
)

# 3. Print the message
print(message)