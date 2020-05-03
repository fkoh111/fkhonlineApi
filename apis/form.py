from flask_restx import Resource, Namespace, fields
from commons.helpers import MailConfig, set_subject
import yagmail

api = Namespace("form", description="File namespace")

schema = api.model(
    "Resource",
    {
        "name": fields.String(required=True),
        "email": fields.String(required=True),
        "message": fields.String(required=True),
    },
)


@api.route("/contact")
class Contact(Resource):
    @api.expect(schema)
    @api.response(code=201, description="Success")
    @api.response(
        code=400,
        description="If payload does not correspond with expected schema, a 400 will be returned",
    )
    @api.response(code=500, description="A catch all for errors")
    def post(self):
        """Takes a payload expected by schema and sends it to mail"""
        try:
            subject = set_subject(name=api.payload["name"], mail=api.payload["email"])
            yag = yagmail.SMTP(MailConfig.SENDER, MailConfig.PSWD)
            yag.send(MailConfig.RECEIVER, subject, api.payload["message"])
            return {"status": "success"}, 201
        except:
            return {"status": "error"}, 500
