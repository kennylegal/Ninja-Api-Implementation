from ninja import NinjaAPI, Schema


api = NinjaAPI()
class UserSchema(Schema):
    username: str
    is_authenticated:bool
    pass

@api.get('/hello')
def hello(request, name: str): 
    return f"Hello {name}"

@api.get('/me', response=UserSchema)
def me(request): 
    return request.user 

