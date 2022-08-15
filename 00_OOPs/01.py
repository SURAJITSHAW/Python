class Item:
    # class attributes -> ypu can acess it from the class and all the instances of it.
    pay_rate = 0.8 # after giving 20% discount
    def __init__(self, name: str, price: float, quantity = 0): # quantity is a default parameter

        # validating args, 'assert' is a key word which helps to validate your expectation with code's reality. It takes 2 args first the expression and second the error message you wanna show ( optional )
        assert price >= 0, f'Price {price} is not equals or greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not equals or greater than zero!'

        # assign attributes to self obj
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calc_total(self):
        return self.price * self.quantity


item1 = Item('smartphone', 10000, 1)
item2 = Item('airpods', 1000, 10)

print(Item.pay_rate) 
print(Item.__dict__) 
print(item1.pay_rate)
