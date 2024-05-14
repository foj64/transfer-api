from flask import Blueprint, request, jsonify
from services.balance_service import BalanceService

balance_controller = Blueprint('balance_controller', __name__)
balance_service = BalanceService()

@balance_controller.route('/balance', methods=['GET'])
def get_balance():
    account_id = request.args.get('account_id')
    if account_id is None:
        return jsonify({'error': 'account_id is required'}), 400

    balance = balance_service.get_balance(account_id)
    # Check if account_id exists in memory
    if balance is None:
        return '0', 404
    else:
        return str(balance), 200
