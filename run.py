from telethon import TelegramClient
from telethon.tl.types import MessageMediaDice

api_id = '8600879'
api_hash = 'e94e3ea1f78e7a12768e60b7a0e00564'

client = TelegramClient('dom4k', api_id, api_hash)

emotion = "🎰🎲🏀🎳🎯"
wins = [64,6,5,6,6]

j = int(input("Enter emotion ("+emotion+"): "))
chat = int(input("Enter chat id: "))

async def main():
	await client.start()
	dice = MessageMediaDice(emoticon=emotion[j], value=wins[j])
	i = 0
	while True:
		a = await client.send_file(chat, dice)
		print(f"Выпало: {a.media.value} | Попытка: {i}")
		if a.media.value == wins[j]: break
		i += 1
		await client.delete_messages(chat, [a.id])
with client: client.loop.run_until_complete(main())

