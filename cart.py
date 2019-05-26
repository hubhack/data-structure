class Cart(list):

    def __len__(self):
        return len(self)

    def __iter__(self):
        return iter(self)
    def __getitem__(self):
        return self[0]
    def __setitem__(self, key, value):
        pass
    def add(self, data):
        self.append(data)
# list()
cart = Cart()
cart.add(1)
cart.add(2)
print(cart[0])
# for x in cart:
#     print(x)