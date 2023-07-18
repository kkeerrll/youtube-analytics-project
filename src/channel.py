import json
import os

from googleapiclient.discovery import build

import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = "AIzaSyDzK-EuKi2DdmdlIl9Pl0Xs1HKEVoOk2HI"

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title: str = self.get_channel_id()['items'][0]['snippet']['title']
        self.videoCount: int = self.get_channel_id()['items'][0]['statistics']['videoCount']
        self.description: str = self.get_channel_id()['items'][0]['snippet']['description']
        self.url: str = 'https://www.youtube.com/channel/' + self.channel_id
        self.viewCount: int = self.get_channel_id()['items'][0]['statistics']['viewCount']

    def print_json(self, dict_print: dict) -> None:
        """Выводит словарь в json-подобном формате с отступами"""
        print(json.dumps(dict_print, indent=2, ensure_ascii=False))

    def get_channel_id(self):
        """Получить данные о канале по его id"""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self, dict_to_print=None) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_channel_id()
        self.print_json(channel)