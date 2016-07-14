class Item(object):
    def __init__(self, v, w):
        self.value = v # Item's value. You want to maximize that!
        self.weight = w # Item's weight. The sum of all items should be <= CAPACITY
