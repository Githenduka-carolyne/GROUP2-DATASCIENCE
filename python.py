sales = [
    {"branch": "Nairobi", "item": "Laptop", "category": "Electronics",
     "price": 780, "quantity": 4, "discount": 0.05, "date": "2025-01-03"},

    {"branch": "Nairobi", "item": "Phone", "category": "Electronics",
     "price": 520, "quantity": 6, "discount": 0.10, "date": "2025-01-03"},

    {"branch": "Mombasa", "item": "Headphones", "category": "Accessories",
     "price": 150, "quantity": 10, "discount": 0.00, "date": "2025-01-04"},

    {"branch": "Nakuru", "item": "Laptop", "category": "Electronics",
     "price": 780, "quantity": 2, "discount": 0.00, "date": "2025-01-04"},

    {"branch": "Nairobi", "item": "Tablet", "category": "Electronics",
     "price": 310, "quantity": 3, "discount": 0.10, "date": "2025-01-05"},

    {"branch": "Mombasa", "item": "Phone", "category": "Electronics",
     "price": 520, "quantity": 4, "discount": 0.00, "date": "2025-01-05"},

    {"branch": "Nakuru", "item": "Keyboard", "category": "Accessories",
     "price": 80, "quantity": 12, "discount": 0.15, "date": "2025-01-05"},

    {"branch": "Nairobi", "item": "Monitor", "category": "Electronics",
     "price": 260, "quantity": 5, "discount": 0.05, "date": "2025-01-06"},

    {"branch": "Mombasa", "item": "Tablet", "category": "Electronics",
     "price": 310, "quantity": 2, "discount": 0.00, "date": "2025-01-06"},
]
unique_items = list(set([sale['item'] for sale in sales]))
print("Unique Items:", unique_items) 



# Using unique_items from Part 1, create a dictionary mapping each item to its total net revenue across all records.
item_net_revenue = {item: sum((sale["price"] * sale["quantity"]) * (1 - sale["discount"])
        for sale in sales
        if sale["item"] == item
    )
    for item in unique_items
}
item_net_revenue


# Using item_net_revenue from Part 2, create a list of items whose total net revenue exceeds 2000. Name the result: top_items.
top_items = [item for item, net_revenue in item_net_revenue.items() if net_revenue > 2000]
top_items

# Using top_items from Part 3, create a new list containing only the sales records for these items.
filtered_sales = [sale for sale in sales if sale['item'] in top_items]
filtered_sales

#Part 5 — Compute Total Quantity Sold per Branch using filtered sales in part 4
branch_quantities = {}
for sale in filtered_sales:
    branch = sale['branch']
    quantity = sale['quantity']
    branch_quantities[branch] = branch_quantities.get(branch, 0) + quantity
print(branch_quantities)

#part 6 Determine the Most Successful Branch
most_successful_branch = max(branch_quantities, key=branch_quantities.get)
print(most_successful_branch)