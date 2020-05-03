from flask_restx import Api
from .form import api as form

api = Api(
    version=0.1,
    title="fkhonlineApi",
    contact="fkoh111",
    contact_url="fkoh111.org",
    description="Flask API for fkhonline.net",
    prefix="/api",
)

api.add_namespace(form)
