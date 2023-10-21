from mongoengine import *

class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(max_length=100) 
    amount = IntField(max_value=10000000000)
    
    
    
class transfer(Document):
    to_email = EmailField(required=True)
    from_email = EmailField(required=True)
    amount = IntField(max_value=10000000000)
    
    
    
    
    
    
    
    def to_dict(self):
        return {name : self.name, email : self.email, balance : self.balance ,user_id : self.user_id}