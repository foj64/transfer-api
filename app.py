from flask import Flask
from controllers.event_controller import app as event_app

app = Flask(__name__)
app.register_blueprint(event_app)

if __name__ == '__main__':
    app.run(debug=True)
