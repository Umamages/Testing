purchase_amount = float(input("Enter the Amount:$"))

state_tax = purchase_amount * 0.08875

total_Amount = purchase_amount + state_tax

print("The sales_tax is:${}" .format(state_tax.__round__(2)))
print("The Total_price is:${}" .format(total_Amount.__round__(2)))