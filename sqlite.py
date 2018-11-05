import datetime
from peewee import *

db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)


print('\n\nHI\n\n')
User.create_table(True)
    
u_in = (User.insert(username='a1'))
u_in.execute()
user_list = (User.select(User))
for u in user_list:
    print(u.username)
