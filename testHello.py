'''
Filename : handler_app.py

Author : Shantanu Dhiman

Desciption : 
    Handle '/register' request.
    Set values for agent_id, system_id, version, handler_uuid & registered_time, 
    then put it into Handler table. If operation successful, then, return handler_uuid
    as response, otherwise return failure message.
    Prints all rows of the table 'Handler'.
'''

from aiohttp import web
import json
import random, string
import datetime
from peewee import *

db = SqliteDatabase('Handler_db.db')

class BaseModel(Model):
    class Meta:
        database = db

class Handler(BaseModel):
    '''
    This is a class for table 'Handler'. 
      
    Attributes: 
        handler_uuid (string) 
        agent_id (string)
        system_id (string)
        version (string)
        registered_time (string) 
    '''
    handler_uuid = CharField(primary_key=True)
    agent_id = CharField(max_length=40)
    system_id = CharField(max_length=40)
    version = CharField(max_length=40)
    registered_time = CharField(max_length=40)

Handler.create_table(True)


async def number(request):
    
    try:
        num = request.query['']
        print(num)
        response_obj = { 'number' : num }
        return web.Response(text=json.dumps(response_obj))
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }        
        return web.Response(text=json.dumps(response_obj))
    
async def new_register(request):
    '''
    Handle '/register' request.
    Set values for agent_id, system_id, version, handler_uuid & registered_time, 
    then put it into Handler table. If operation successful, then, return handler_uuid
    as response, otherwise return failure message.
    Prints all rows of the table 'Handler'.
  
    Parameters: 
    request (): request url which contains agent_id, system_id & version.
  
    Returns: 
    response_obj (json): handler_uuid if success otherwise failure status. 
    '''
    try:
        # set values for agent_id, system_id, vesion, handler_uuid and registered_time
        print(type(request))
        agent_id = request.query['agent_id']
        system_id = request.query['system_id']
        version = request.query['vesion']
        handler_uuid = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(32))
        registered_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        # query to insert values into database
        handler_data = (Handler.insert(handler_uuid=handler_uuid,agent_id=agent_id,system_id=system_id,version=version,registered_time=registered_time))
        handler_data.execute()
        
        # query to fetch all rows from database  
        handler_list = (Handler.select(Handler))
        '''
        for row in handler_list:
            print(row.handler_uuid)
            print(row.agent_id)
            print(row.system_id)
            print(row.version)
            print(row.registered_time)
        '''
        response_obj = { 'handler_uuid' : handler_uuid }
        return web.Response(text=json.dumps(response_obj))
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }        
        return web.Response(text=json.dumps(response_obj))

app = web.Application()
app.router.add_get('/register', new_register)
app.router.add_get('/number', number)

web.run_app(app)
