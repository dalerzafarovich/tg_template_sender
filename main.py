import asyncio

from pyrogram import Client
from pyrogram.filters import user
from pyrogram.types import Message

import config

app = Client('account', config.API_ID, config.API_HASH)


async def send_templates(receiver) -> None:
    message = await app.send_message(config.ADMIN, f'Идет отправка сообщений пользователю {receiver}')
    for text in config.TEXT_LIST:
        await app.send_message(receiver, text)
        await asyncio.sleep(config.DELAY)
    await app.send_message(config.ADMIN, f'Отправка сообщений пользователю {receiver} закончена успешно',
                           reply_to_message_id=message.id)


@app.on_message(user([config.ADMIN]))
async def send_message(client: Client, message: Message):
    try:
        task = asyncio.create_task(send_templates(message.text))
        await task
    except Exception:
        await client.send_message(message.from_user.id, 'Произошла ошибка')


app.run()
