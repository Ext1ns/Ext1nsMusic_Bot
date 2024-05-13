from aiogram.filters import Filter
from aiogram import types
from typing import List


class MyFilter(Filter):
    def __init__(self, types_of_chats: List[str]) -> None:
        self.types_of_chats = types_of_chats

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.types_of_chats