from flask import Blueprint, request, jsonify
from services.event_service import EventService

event_controller = Blueprint('event_controller', __name__)
event_service = EventService()

@event_controller.route('/event', methods=['POST'])
def handle_event():
    request_data = request.get_json()
    if 'type' not in request_data:
        return jsonify({'error': 'type field is required'}), 400

    event_type = request_data['type']
    if event_type == 'deposit':
        return add_amount(request_data)
    elif event_type == 'transfer':
        return transfer_amount(request_data)
    elif event_type == 'withdraw':
        return withdraw_amount(request_data)
    else:
        return jsonify({'error': 'Invalid event type'}), 400

def add_amount(request_data):
    return event_service.add_amount(request_data)

def transfer_amount(request_data):
    return event_service.transfer_amount(request_data)

def withdraw_amount(request_data):
    return event_service.withdraw_amount(request_data)

@event_controller.route('/reset', methods=['POST'])
def reset_data():
    event_service.reset_data()
    return 'OK', 200
