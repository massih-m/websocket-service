
class WebsocketClient:

    def __init__(self):
        self.topics = {}
        self.clients = {}

    def add(self, topic: str, client):
        self.topics.setdefault(topic, []).append(client)
        self.clients.setdefault(client, []).append(topic)

    def remove_topic(self, topic: str):
        if topic in self.topics:
            for client in self.topics[topic]:
                self.clients[client].remove(topic)

            self.topics.pop(topic)

    def remove(self, client):
        if client in self.clients:
            for topic in self.clients[client]:
                self.topics[topic].remove(client)

            self.clients.pop(client)

    def get_subscribers(self, topic: str):
        return self.topics.get(topic, [])