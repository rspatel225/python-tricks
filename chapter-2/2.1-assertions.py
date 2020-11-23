car = {
    'brand': 'Honda',
    'model': 'civic',
    # price in cents
    'price': 2105000,
}

def apply_discount(product, discount): 
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], "Invaild final price"
    return price

# legal discount
print(apply_discount(car, 0.20))

# invaild discount
print(apply_discount(car, 2.0))