from models.data_manager import DataManager

class EventService:
    def __init__(self):
        self.data_manager = DataManager()

    def add_amount(self, request_data):
        if 'id' not in request_data or 'amount' not in request_data:
            return {'error': 'id and amount fields are required'}, 400
        id = request_data['id']
        amount = request_data['amount']
        updated_amount = self.data_manager.add_amount(id, amount)
        return {'id': id, 'balance': updated_amount}, 201
