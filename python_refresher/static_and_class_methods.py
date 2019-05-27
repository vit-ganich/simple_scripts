class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls("{} - franchise".format(store.name))

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, store.stock_price())


store1 = Store("Hamster")
store1_fran = Store.franchise(store1)
store1.add_item('Garment', 500)
store1_fran.add_item('Trash', 10)
print(store1_fran.name)
print(Store.store_details(store1))
print(Store.store_details(store1_fran))
