import pymongo


class MongoService:
    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://xxx:password@xxx.8mamm.mongodb.net/db_name?retryWrites=true&w=majority")

        self.film_collection = client.get_database('film_from_telegram_channel').get_collection('films')
