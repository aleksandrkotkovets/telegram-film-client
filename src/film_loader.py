import glob
import os

from telethon import TelegramClient

from src.mongo_service import MongoService
from src.utils import *
from src.variables import api_id, api_hash, channel_id


def load_film_into_file():
    purge_sessions()
    print('starting up, buckle up bois')
    client = TelegramClient("channel_name", api_id, api_hash)
    with client:
        client.loop.run_until_complete(load_film_from_telegram_and_close(client))
    print('purging sessions')
    purge_sessions()


async def load_film_from_telegram_and_close(client: TelegramClient):
    me = await client.get_me()
    print(me.stringify())

    film_collection = MongoService().film_collection
    film_collection.drop()

    async for message in client.iter_messages(channel_id):
        if message.text is not None:
            film_info = get_film_info_from_message(message)

            if film_info is not None:
                print(f'I sensed new film! {film_info}')
                film_collection.insert(film_info)

            print(message)
    await client.disconnect()


def purge_sessions():
    for f in glob.glob('*.session*'):
        os.remove(f)
