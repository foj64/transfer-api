from flask import Flask, request, jsonify
from services.event_service import EventService

app = Flask(__name__)
event_service = EventService()

@app.route('/reset', methods=['POST'])
def reset_data():
    global data
    data = {}
    return 'OK', 200
