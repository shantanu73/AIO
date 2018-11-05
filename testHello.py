from aiohttp import web
import json
from datetime import datetime
import random, string
import time


async def new_register(request):
    try:
        agent_id = request.query['agent_id']
        system_id = request.query['system_id']
        version = request.query['version']
        handler_uuid = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(16))
        registered_time = time.strftime("%H:%M:%S", time.now())#datetime.datetime.now().strftime('%H:%M:%S')
        
        
        response_obj = { 'handler_uuid' : handler_uuid }
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }        
        return web.Response(text=json.dumps(response_obj), status=500)

app = web.Application()
app.router.add_get('/register', new_register)

web.run_app(app)
