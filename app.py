from flask import Flask
from apis import api

app = Flask(__name__)
app.config.from_pyfile("config.prod.cfg")
api.init_app(app)

if __name__ == "__main__":
    app.run()
