customer_id = [77,33,66,22,99]
new_customer_id = [11,22,44,55,66,88,99]

for id in new_customer_id:
    if id not in customer_id:
        customer_id.append(id)

customer_id.sort()
print(customer_id)