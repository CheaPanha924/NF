price=float(input('Enter price='))
qty=int(input('Enter quantity='))
total=price*qty
if total >= 0 and total <10:
    discount = 0
elif total >= 10 and total <25:
    discount = 10
pay = total - (total * discount / 100)

print(f"total = {total}$")
print(f"after discount {discount}%")
print(f"payment ={pay}$")