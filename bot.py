import logging
from time import sleep, asctime

from aiogram import Bot, Dispatcher, executor, types

from credentials import bot_token

logging.basicConfig(level=logging.INFO, format="%(message)s")

TOKEN = bot_token

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# TODO: send audio on command (audio.py)
# TODO: notify of an unrecognized command/msg


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
	user_id = message.from_user.id
	user_full_name = message.from_user.full_name
	user_first_name = message.from_user.first_name

	logging.info(f"{user_id=} {user_full_name=} {asctime()}")

	await bot.send_chat_action(message.chat.id, "typing")
	sleep(2)

	await bot.send_message(message.chat.id, f"Hello, {user_first_name}!\nMy name is Strawberette.")


@dp.message_handler(commands=["oink"])
async def oink_function(message: types.Message):
	await bot.send_chat_action(message.chat.id, "typing")
	sleep(1)

	await bot.send_message(message.chat.id, "Oink-oink!")


@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
	await bot.send_chat_action(message.chat.id, "typing")
	sleep(2)

	await bot.send_message(message.chat.id, "Basically, you can send me some commands and I will do something for you. Because we are friends!\nI love helping my friends!")
	sleep(2)

	await bot.send_chat_action(message.chat.id, "typing")
	sleep(1.25)

	await bot.send_message(message.chat.id, "And I love you \U00002764")


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
