from flask import Flask
from apis import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile("config.prod.cfg")
api.init_app(app)

if __name__ == "__main__":
    app.run()
