class Cosmetic:
    products = ['lipstick','foundation','maskara','eye liner']

shrushti = Cosmetic()

print(shrushti.products)
shrushti.products.pop()
print(shrushti.products)
shrushti.products.append('highlighter')
print(shrushti.products)

cust2 = Cosmetic()
print(cust2.products)
