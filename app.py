from flask import Flask
from flask_restx import Api
from apis.contact import api as contact


app = Flask(__name__)
app.config.from_pyfile("config.cfg")
api = Api(
    version=0.1,
    title="fkhonlineApi",
    contact="fkoh111",
    contact_url="fkoh111.org",
    description="Flask API for fkhonline.net",
    prefix="/api",
    doc=False,
)
api.init_app(app)

api.add_namespace(contact)

if __name__ == "__main__":
    app.run()
