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
 
u_obj = User()
u_in = (u_obj.insert(username='a2'))
u_in.execute()
user_list = (u_obj.select(u_obj))
for u in user_list:
    print(u.username)
