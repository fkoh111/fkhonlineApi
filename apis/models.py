from flask_restx import Namespace, fields

api = Namespace("contact")

schema = api.model(
    "contact",
    {
        "name": fields.String(required=True),
        "email": fields.String(required=True),
        "message": fields.String(required=True),
    },
)
