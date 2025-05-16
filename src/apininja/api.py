from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI
from waitlist.api import router as waitlist_router

api = NinjaExtraAPI()
api.add_router('waitlist/', waitlist_router)

api.register_controllers(NinjaJWTDefaultController)

class UserSchema(Schema):
    username: str
    is_authenticated:bool


@api.get('/hello')
def hello(request, name: str): 
    return f"Hello {name}"

@api.get('/me', response=UserSchema, auth=JWTAuth())
def me(request): 
    return request.user 

