import os

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import Bold, as_marked_section
from sqlalchemy.ext.asyncio import AsyncSession
from my_filters.filter_user import MyFilter

private_router = Router()
private_router.message.filter(MyFilter(['private']))


@private_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer('Добро пожаловать в музыкального бота ! '
                         'Для помощи в использовании введите /help')


@private_router.message(or_f(Command('help'), (F.text.lower() == 'помощь')))
@private_router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer('Чтобы скачать музыку пришлите ссылку на видео с YouTube')


@private_router.message(or_f(Command('about'), (F.text.lower() == 'О создателе')))
@private_router.message(Command('about'))
async def about_command(message: types.Message):
    about = as_marked_section(
        Bold('О создателе:\n'),
        'Создатель: Ext1ns\n'
        'GitHub: https://github.com/Ext1ns\n')
    await message.answer(about.as_html())

# Добавить ссылку на донат
@private_router.message(or_f(Command('donate'), (F.text.lower() == 'Поддержать автора')))
async def donate_command(message: types.Message):
    pass
