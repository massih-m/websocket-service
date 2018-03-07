import asyncio
import aioredis
import json

from .my_logging import get_logger
from .websocket_interface import WebsocketInterface

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


class RedisClient:
    def __init__(self):
        self.logger = get_logger(__file__)

    async def redis_start(self):
        _redis = await aioredis.create_redis((REDIS_HOST, REDIS_PORT))
        self.logger.info('Redis listener started')
        subscribe = await _redis.subscribe('websocket_interface')
        return subscribe[0]

    async def redis_listener(self, channel):
        while await channel.wait_message():
            msg = await channel.get_json(encoding="utf-8")
            print("received message => {}".format(msg))
            asyncio.ensure_future(WebsocketInterface.publish(msg.get('topic'), msg.get('data')))


async def redis_stuff():
    redis = await aioredis.create_redis(('127.0.0.1', 6379))
    await redis.publish('websocket_interface', json.dumps({'topic': 'test', 'data': 'hellooooo'}))

    #await redis.set('key', 'hello world')
    #val = await redis.get(key='key', encoding='UTF-8')
    #print(val)
    redis.close()
    await redis.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(redis_stuff())
