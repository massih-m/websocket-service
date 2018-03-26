import json


class RedisApi:
    __modules = read_json_file()

    @classmethod
    async def register_module(cls, data):
        if cls.is_valid(data):
            cls.__modules[data.name] = data

    @classmethod
    async def deregister_module(name):
        pass

    @staticmethod
    async def is_registered(cls, name):
        return name in cls.__modules

    @staticmethod
    def is_valid(data):
        return data.get('name') and data.get('inputs')

    @staticmethod
    def read_json_file():
        with open('./modules.json', 'r') as handler:
            return json.load(handler)

    @staticmethod
    def update_json_file(data):
        with open('./modules.json', 'w') as handler:
            json.dump(data, handler)

