from flask import Flask
from controllers.event_controller import event_controller
from controllers.balance_controller import balance_controller

app = Flask(__name__)
app.register_blueprint(event_controller)
app.register_blueprint(balance_controller)

if __name__ == '__main__':
    app.run(debug=True)
