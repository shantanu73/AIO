from aiohttp import web
import json
import random, string
import time
import datetime
from peewee import *

db = SqliteDatabase('Handler_db.db')

class BaseModel(Model):
    class Meta:
        database = db

class Handler(BaseModel):
    handler_uuid = CharField(primary_key=True)
    agent_id = CharField(max_length=40)
    system_id = CharField(max_length=40)
    vesion = CharField(max_length=40)
    registered_time = CharField(max_length=40)

Handler.create_table(True)
    
async def new_register(request):
    try:
        agent_id = request.query['agent_id']
        system_id = request.query['system_id']
        vesion = request.query['vesion']
        handler_uuid = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(16))
        registered_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        handler_data = (Handler.insert(handler_uuid=handler_uuid,agent_id=agent_id,system_id=system_id,vesion=vesion,registered_time=registered_time))
        handler_data.execute()
        handler_list = (Handler.select(Handler))
        for row in handler_list:
            print(row.handler_uuid)
            print(row.agent_id)
            print(row.system_id)
            print(row.vesion)
            print(row.registered_time)
            
        response_obj = { 'handler_uuid' : handler_uuid , 'registered_time' : registered_time }
        return web.Response(text=json.dumps(response_obj))
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }        
        return web.Response(text=json.dumps(response_obj))

app = web.Application()
app.router.add_get('/register', new_register)

web.run_app(app)
