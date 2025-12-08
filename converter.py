# importо-замещение
import os
from kivy.app import App  # чтобы все писать не с нуля
from kivy.uix.boxlayout import BoxLayout  # единственный который я помню как работает
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from pathlib import Path

# class Main(App):  # все функции от App(встроенный плейсхолдер), будут в Main(наше приложение)
#     def build(self):
#         self.val = 0  # переменная, которая принадлежит классу, работает лучше, нужен self.
#         self.map = []  # это будет матрица, просто вспомогательная
#         self.label = Label(text='')
#         self.map.append([self.label])
#         self.butt = Button(text='Print', on_press=self.print)  # print() и self.print() - разное

#         # мне лень каждую кнопку вручную писать, но думаю суть ясна
#         for i in range(4):
#             self.map.append(
#                 [Button(text=f'+{j + i * 4}', on_press=self.func) for j in range(4)]
#             )
#         self.map[1][0].text = 'Clear'

#         self.map.append([self.butt])
#         self.layout = BoxLayout(orientation='vertical')
#         for row in self.map:
#             l = BoxLayout(orientation='horizontal')
#             for obj in row:
#                 l.add_widget(obj)
#             self.layout.add_widget(l)
#         return self.layout

#     def print(self, instance):  # instance - объект, который вызвал функцию, без него будет ошибка
#         self.label.text = str(self.val)

#     def func(self, instance: Button):
#         if instance.text == 'Clear':
#             self.val = 0
#             return
#         self.val += int(instance.text[1:])

script_path = os.path.abspath(__file__)
ffmpeg_folder = r"ffmpeg\bin\ffmpeg.exe"
ffmpeg_path= script_path.replace("converter.py","")+ffmpeg_folder
file = "D:\Клипы\clip.mp4"
abs_file = Path("D:\Клипы\clip.mp4")
file_types = {
    'image': ("jpg", "jpeg", "png", "bmp", "gif", "webp"),
    'video': ("mp4", "avi", "mov", "mkv", "webm", "flv", "wmv"),
    'audio': ("mp3", "wav", "flac", "aac", "ogg", "m4a")
}


class Main(App):
    def build(self):
        self.map = [[Label(text=f'File selected: {file}')]]

        choices = []
        if file.split('.')[-1] in file_types['image']:
            choices = [
                Button(text='Convert', on_press=self.convert),
                Button(text='Resize', on_press=self.resize),
                Button(text='Compress', on_press=self.compress),
                Button(text='Compress with size', on_press=self.compress)
            ]
        elif file.split('.')[-1] in file_types['video']:
            choices = [
                Button(text='Convert', on_press=self.convert),
                Button(text='Change bitrate', on_press=self.compress),
                Button(text='Compress with size', on_press=self.compress),
                Button(text='Change FPS', on_press=self.compress),
                Button(text='Extract audio', on_press=self.compress)
            ]
        elif file.split('.')[-1] in file_types['audio']:
            choices = [
                Button(text='Convert', on_press=self.convert),
                Button(text='Change bitrate', on_press=self.compress),
                Button(text='Change sampling frequency', on_press=self.compress),
                Button(text='Compress with size', on_press=self.compress)
            ]
        else:
            choices = [Label(text='File type not supported')]
        
        self.input = TextInput()
        self.map.append([self.input])
        
        for i in choices:
            self.map.append([i])
        self.layout = BoxLayout(orientation='vertical')
        
        for row in self.map:
            l = BoxLayout(orientation='horizontal')
            for obj in row:
                l.add_widget(obj)
            self.layout.add_widget(l)
        
        return self.layout

    def _print(self, instance):
        print(self.input.text)

    def convert(self, instance):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c copy out.mkv"
        os.system(command)
        
    def resize(self, instance):
        pass
    def compress(self, instance):
        pass
    def edit_fps(self, instance):
        pass
    def extract_audio(self, instance):
        pass

Main().run()