from models.data_manager import DataManager

class EventService:
    def __init__(self):
        self.data_manager = DataManager()

    def add_amount(self, request_data):
        if 'destination' not in request_data or 'amount' not in request_data:
            return {'error': 'destination and amount fields are required'}, 400

        destination = request_data['destination']
        amount = request_data['amount']
        updated_amount = self.data_manager.add_amount(destination, amount)
        return {"destination": {'id': destination, 'balance': updated_amount}}, 201

    def transfer_amount(self, request_data):
        if 'origin' not in request_data or 'destination' not in request_data or 'amount' not in request_data:
            return {'error': 'origin, destination, and amount fields are required'}, 400

        origin = request_data['origin']
        destination = request_data['destination']
        amount = request_data['amount']
        success, origin_amount, destination_amount = self.data_manager.transfer_amount(origin, destination, amount)
        if success:
            return {'origin': {'id': origin, 'balance': origin_amount}, 'destination': {'id': destination, 'balance': destination_amount}}, 201
        else:
            return '0', 404

    def withdraw_amount(self, request_data):
        if 'origin' not in request_data or 'amount' not in request_data:
            return {'error': 'origin and amount fields are required'}, 400

        origin = request_data['origin']
        amount = request_data['amount']
        success, updated_amount = self.data_manager.withdraw_amount(origin, amount)
        if success:
            return {'origin': {'id': origin, 'balance': updated_amount}}, 201
        else:
            return '0', 404

    def reset_data(self):
        self.data_manager.reset_data()
