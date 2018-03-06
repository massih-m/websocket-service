import asyncio

from py_scripts.websocket_service import WebsocketInterface
from py_scripts.websocket_service.redis_client import RedisClient


async def service_starter():
    ws = WebsocketInterface()
    asyncio.ensure_future(ws.start())
    redis = RedisClient()
    redis_channel = await redis.redis_start()
    asyncio.ensure_future(redis.redis_listener(redis_channel))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(service_starter())
    loop.run_forever()
