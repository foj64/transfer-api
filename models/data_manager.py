class DataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.data = {}
        return cls._instance

    def add_amount(self, id, amount):
        if id in self.data:
            self.data[id] += amount
        else:
            self.data[id] = amount
        return self.data[id]

    def transfer_amount(self, origin, destination, amount):
        if origin not in self.data or self.data[origin] < amount:
            return False, 0, 0

        self.data[origin] -= amount
        self.data[destination] = self.data.get(destination, 0) + amount
        return True, self.data[origin], self.data[destination]

    def withdraw_amount(self, id, amount):
        if id not in self.data or self.data[id] < amount:
            return False, 0
        self.data[id] -= amount
        return True, self.data[id]

    def reset_data(self):
        self.data = {}

    def get_balance(self, id):
        return self.data.get(id)
        