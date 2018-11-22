from aiohttp import web
import json
from datetime import datetime
import random, string
import time
import datetime
    
def new_register(request):
    try:
        print("hi")
        agent_id = request.query['agent_id']
        print(agent_id)
        response_obj = { 'agent_id' : agent_id }
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }        
        return web.Response(text=json.dumps(response_obj), status=500)

app = web.Application()
app.router.add_get('/register', new_register)

web.run_app(app)
