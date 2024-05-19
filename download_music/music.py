import re
import os
import datetime
from aiogram import types
from aiogram.types import FSInputFile
from aiogram import Router
from pytube import YouTube, Playlist


music_router = Router()


async def writes_logs(_ex):
    """Записывает логи в файл 'logs.log', в котором будут время и ошибка"""
    with open('logs.log', 'a') as file_log:
        file_log.write('\n' + str(datetime.datetime.now()) + ': ' + str(_ex))


async def create_audio(url):
    """Скачивает и открывает файл"""
    try:
        yt = YouTube(url).streams.filter(only_audio=True).first()
        path = yt.download("music")
        return path
    except Exception as _ex:
        await writes_logs(_ex)
        return None


async def delete_all_music_in_directory():
    """Удаляет все загруженные аудио из папки 'music'"""
    if not os.path.exists('music'):
        os.mkdir('music')
    for file in os.listdir('music'):
        try:
            if re.search('mp4', file):
                mp4_path = os.path.join('music', file)
                os.remove(mp4_path)
        except Exception as _ex:
            await writes_logs(_ex)


@music_router.message()
async def get_files(message: types.Message):
    """Ждёт от пользователя ссылку на ютуб плейлист или видео и начинает его скачивать, и отправляет пользователю"""
    if message.text.startswith('https://www.youtube.com/playlist?list='):
        # Для плейлиста
        playlist = Playlist(message.text)
        for url in playlist:
            try:
                path = await create_audio(url)
                if path:
                    audio = FSInputFile(path)
                    await message.answer_audio(audio)
            except Exception as _ex:
                await writes_logs(_ex)
        else:
            await message.answer("Плейлист закрыт")
    elif message.text.startswith('https://www.youtube.com/watch?v=') or message.text.startswith('https://youtu.be/'):
        # Для видео
        try:
            url = message.text
            path = await create_audio(url)
            if path:
                audio = FSInputFile(path)
                await message.answer_audio(audio)
        except Exception as _ex:
            await writes_logs(_ex)
