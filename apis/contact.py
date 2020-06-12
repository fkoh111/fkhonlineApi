from flask_restx import Resource
from commons.helpers import MailConfig, set_subject
from .models import api, schema
import yagmail


@api.route("/form")
class Contact(Resource):
    @api.expect(schema)
    @api.response(code=201, description="Success")
    @api.response(
        code=400, description="If payload does not correspond with schema",
    )
    @api.response(code=500, description="Error")
    def post(self):
        """Takes a payload expected by schema and sends it to mail"""
        try:
            subject = set_subject(name=api.payload["name"], mail=api.payload["email"])
            yag = yagmail.SMTP(MailConfig.SENDER, MailConfig.PSWD)
            yag.send(MailConfig.RECEIVER, subject, api.payload["message"])
            return {"status": "success"}, 201
        except:
            return {"status": "error"}, 500
