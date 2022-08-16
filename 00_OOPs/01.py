import csv


class Item:
    # It would be nice to keep track of all the instances of this class in a list. That's why we declare this class attribute, and then append the self obj each time a new instance got created.
    all = []
    # class attributes -> you can acess it from the class and all the instances of it.
    pay_rate = 0.8 # after giving 20% discount
    def __init__(self, name: str, price: float, quantity = 0): # quantity is a default parameter

        # validating args, 'assert' is a key word which helps to validate your expectation with code's reality. It takes 2 args first the expression and second the error message you wanna show ( optional )
        assert price >= 0, f'Price {price} is not equals or greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not equals or greater than zero!'

        # assign attributes to self obj
        self.name = name
        self.price = price
        self.quantity = quantity

        # Executing task
        Item.all.append(self)
        
    def calc_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    # this magic function is representing all the objs
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})" # we return the objs exactly in this format to distiguish them easily.

    @classmethod
    def instatiate_from_csv(cls):
        with open('items.csv', 'r') as f: # when using 'with' keyword don't had to worry about closing the file.
            # csv.DictReader() helps to directly read csv file and later convert it into python dictionaries
            reader = csv.DictReader(f)
            items = list(reader) # convert it into list of dict

        for item in items:
            # creating instances of Item class
            Item(
                name=item.get('name'),
                price=float(item.get('price')), # the value will be return in str. that's why convert it according to your need
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            # count out the floats which are point zero, ex: 6.0, 11.0
            return num.is_integer() 
        else:
            return False

Item.instatiate_from_csv()
print(Item.all)
