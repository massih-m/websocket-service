import json
import websockets
from .my_logging import get_logger
from .websocket_client import WebsocketClient

# msg: {'action': 'subscribe/unsubscribe', 'topic': 'topic_name'}


class WebsocketInterface:
    clients = WebsocketClient()
    WS_HOST = '0.0.0.0'
    WS_PORT = 8888

    def __init__(self):
        self.logger = get_logger(__file__)

    async def start(self):
        await websockets.serve(self.connection_handler, self.WS_HOST, self.WS_PORT)
        self.logger.info('test debug')
        self.logger.info('websocket service started')

    async def connection_handler(self, client, _):
        print('handle_connection')
        try:
            async for message in client:
                await self.client_handler(client, message)
        except websockets.exceptions.ConnectionClosed:
            self.clients.remove(client)

    async def client_handler(self, client: websockets, message: str):
        self.logger.info('client connected with message: {}'.format(message))
        msg = json.loads(message)
        if self.is_msg_valid(msg):
            self.clients.add(msg['topic'], client)
        else:
            self.logger.debug('invalid message received => {}'.format(msg))
        # self.logger.info(msg['topic'])

    @classmethod
    async def publish(cls, topic, msg):
        for client in cls.clients.get_subscribers(topic):
            print("msg to send {}".format(msg))
            await client.send(msg)

    @staticmethod
    def is_msg_valid(message):
        return message.get('action') and message.get('topic')