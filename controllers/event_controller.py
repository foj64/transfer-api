from flask import Flask, request, jsonify
from services.event_service import EventService

app = Flask(__name__)
event_service = EventService()

# In-memory storage for id and amount
data = {}

@app.route('/reset', methods=['POST'])
def reset_data():
    global data
    data = {}
    return 'OK', 200
