from models.data_manager import DataManager

class BalanceService:
    def __init__(self):
        self.data_manager = DataManager()

    def get_balance(self, id):
        return self.data_manager.get_balance(id)
