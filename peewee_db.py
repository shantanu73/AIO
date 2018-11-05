import asyncio
import peewee
import logging
from peewee_async import Manager, PostgresqlDatabase

loop = asyncio.new_event_loop() # Note: custom loop!
database = PostgresqlDatabase('test')
objects = Manager(database, loop=loop)
