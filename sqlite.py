import datetime
from peewee import *

db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
    
    
tweets = (Tweet
          .select(Tweet, User)
          .join(User)
          .order_by(Tweet.created_date.desc()))
for tweet in tweets:
    print(tweet.user.username, tweet.message)
