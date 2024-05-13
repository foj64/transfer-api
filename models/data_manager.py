class DataManager:
    def __init__(self):
        self.data = {}

    def add_amount(self, id, amount):
        if id in self.data:
            self.data[id] += amount
        else:
            self.data[id] = amount
        return self.data[id]
        