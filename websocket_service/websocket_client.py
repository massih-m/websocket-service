
class WebsocketClient:

    def __init__(self):
        self.topics = {}
        self.clients = {}

    def add(self, topic: str, client):
        self.topics.setdefault(topic, []).append(client)
        self.clients.setdefault(client, []).append(topic)

    def delete_topic(self, topic: str):
        for client in self.topics[topic]:
            self.clients[client].remove(topic)

        self.topics.pop(topic)

    def delete_client(self, client):
        for topic in self.clients[client]:
            self.topics[topic].remove(client)

        self.clients.pop(client)
