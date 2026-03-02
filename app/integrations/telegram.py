import aiohttp

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    async def send(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        async with aiohttp.ClientSession() as session:
            await session.post(url, data={
                "chat_id": self.chat_id,
                "text": message
            })
