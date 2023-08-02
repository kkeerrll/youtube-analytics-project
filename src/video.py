import json
import os

from googleapiclient.discovery import build

import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = "AIzaSyDzK-EuKi2DdmdlIl9Pl0Xs1HKEVoOk2HI"

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

url_main_video = 'https://youtu.be/'


class Video:
    """Класс для видео из ютуба"""

    def __init__(self, video_id: str):
        self.video_id: str = video_id
        try:
            """Экземпляр инициализируется id видео"""
            self.video_title: str = self.get_video_info()['items'][0]['snippet']['title']
            self.video_url: str = url_main_video + video_id
            self.view_count: int = self.to_int(self.get_video_info()['items'][0]['statistics']['viewCount'])
            self.like_count: int = self.to_int(self.get_video_info()['items'][0]['statistics']['likeCount'])
        except BaseException:
            self.title: str = None
            self.video_url: str = None
            self.view_count: int = None
            self.like_count: int = None




    def __str__(self):
        return f'{self.video_title}'


    def get_video_info(self):
        """Получает данные о видео по его id"""
        video_id = self.video_id
        video_info = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
        return video_info


    def to_int(self, numb):
        """Возвращает полученное значение в типе int"""
        if type(numb) == int:
            return numb
        else:
            num_int = int(float(numb))
            return num_int


class PLVideo(Video):
    """Класс, производный от класса Video"""

    def __init__(self, video_id, playlist_id):
        """Экземпляр инициализируется 'id видео' и 'id плейлиста'"""
        super().__init__(video_id)
        self.playlist_id = playlist_id


    def __str__(self):
        return f'{self.video_title}'