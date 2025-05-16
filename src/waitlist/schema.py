from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistCreateSchema(Schema):
    email: EmailStr



class WaitlistDetails(Schema):
    email: EmailStr
    timestamp: datetime


class ListWaitlist(Schema):
    id: int
    email: EmailStr
    timestamp: datetime