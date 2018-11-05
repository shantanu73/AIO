import asyncio
import peewee
import logging
from peewee_async import Manager, PostgresqlDatabase

loop = asyncio.new_event_loop() # Note: custom loop!
database = PostgresqlDatabase('Handler_db')

objects = Manager(database, loop=loop)

class Handler(peewee.Model):
    handler_uuid = peewee.CharField(max_length=40, unique=True)
    agent_id = peewee.CharField(max_length=40)
    system_id = peewee.CharField(max_length=40)
    vesion = peewee.CharField(max_length=40)
    registered_time = peewee.CharField(max_length=40)

    class Meta:
        database = database
        
# creating table for above block
Handler.create_table(True)
query = Handler.insert_from(
           Handler.handler_uuid, Handler.agent_id, Handler.system_id, Handler.vesion, Handler.registered_time ),fields=['a', 'b', 'c', 'd', 'e'])
query.execute()
query1 = Handler.select(
           Handler.handler_uuid, Handler.agent_id, Handler.system_id, Handler.vesion, Handler.registered_time ))
query1.execute()
