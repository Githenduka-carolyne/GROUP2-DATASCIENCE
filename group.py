print ("Hello,  this is Clive!")

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