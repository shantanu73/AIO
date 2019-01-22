from aiohttp import web
import json
from datetime import datetime
import random, string
import time
import datetime
    
def new_register(request):
    try:
        index_path = "/root/AIO/index.html"
        index_file = open(index_path)
        log.info("Serving %s", index_path)
        resp = web.Response(body=index_file.read().encode('utf-8'))
        resp.headers['content-type'] = 'text/html'
        return resp
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }        
        return web.Response(text=json.dumps(response_obj), status=500)

app = web.Application()
app.router.add_get('/register', new_register)

web.run_app(app)
