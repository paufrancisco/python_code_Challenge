def dis(amount, discount):
    
    percent = discount * 0.0100
    discountedPrice = amount*percent
    
    return discountedPrice

price = 4000
discPercent = 50

discountedPrice = dis(price, discPercent)

print(f"The discounted price of {price} with {discPercent} percent discount is {discountedPrice}")