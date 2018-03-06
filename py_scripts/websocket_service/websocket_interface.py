import json
import websockets

from py_scripts.websocket_service.my_logging import get_logger
from py_scripts.websocket_service.websocket_client import WebsocketClient

WS_HOST = 'localhost'
WS_PORT = 8282


class WebsocketInterface:
    clients = WebsocketClient()

    def __init__(self):
        self.logger = get_logger(__file__)

    async def start(self):
        await websockets.serve(self.connection_handler, WS_HOST, WS_PORT)
        self.logger.debug('test debug')
        self.logger.info('websocket service started')

    async def connection_handler(self, client, _):
        print('handle_connection')
        try:
            async for message in client:
                await self.client_handler(client, message)
        except websockets.exceptions.ConnectionClosed:
            self.clients.remove(client)

    async def client_handler(self, client: websockets, message: str):
        print('client connected with message: {}'.format(message))
        msg = json.loads(message)
        self.clients.add(msg['topic'], client)
        print(msg['topic'])

    @classmethod
    async def publish(cls, topic, msg):
        for client in cls.clients.get_subscribers(topic):
            print("msg to send {}".format(msg))
            await client.send(msg)

