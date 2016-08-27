import asyncio
import sys

import orm
from models import User


async def test(loop1):
    await orm.create_pool(loop=loop1, host='localhost', port=3306, user='root', password='369958', db='awesome')
    u = User(name='test77', email='test77@test.com', passwd='test', image='about:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
