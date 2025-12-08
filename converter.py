# importо-замещение
import os

from kivy.app import App  # чтобы все писать не с нуля
from kivy.uix.boxlayout import BoxLayout  # единственный который я помню как работает
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
import subprocess
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
file = r"E:\Леса.png"
abs_file = Path(file)
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
            self.parameters = [TextInput() for _ in range(3)]
            choices = [
                Button(text='Convert', on_press=lambda *args: self.convert_image(self, 0), size_hint = (2,1)),
                Button(text='Resize', on_press=lambda *args: self.resize_image(self, 1), size_hint = (2,1)),
                Button(text='Compress', on_press=lambda *args: self.compress_image(self, 2), size_hint = (2,1))
                # Button(text='Compress with size', on_press=self.compress, size_hint = (2,1))
            ]
        elif file.split('.')[-1] in file_types['video']:
            self.parameters = [TextInput() for _ in range(3)]
            choices = [
                Button(text='Convert', on_press=lambda *args: self.convert_video(self, 0), size_hint = (2,1)),
                Button(text='Change bitrate', on_press=lambda *args: self.change_bitrate(self, 1), size_hint = (2,1)),
                # Button(text='Compress with size', on_press=self.compress_video_by_size, size_hint = (2,1)),
                Button(text='Change FPS', on_press=lambda *args: self.change_fps(self, 2), size_hint = (2,1)),
                Button(text='Extract audio', on_press=self.extract_audio)
            ]
        elif file.split('.')[-1] in file_types['audio']:
            self.parameters = [TextInput() for _ in range(2)]
            choices = [
                # Button(text='Convert', on_press=self.c, size_hint = (2,1)),
                Button(text='Change bitrate', on_press=lambda *args: self.change_audio_bitrate(self, 0), size_hint = (2,1)),
                Button(text='Change sampling frequency', on_press=lambda *args: self.change_audio_samplerate(self, 1), size_hint = (2,1))
                # Button(text='Compress with size', on_press=self.com, size_hint = (2,1))
            ]
        else:
            self.parameters = []
            choices = [Label(text='File type not supported')]
        
        for i in range(len(self.parameters)):
            g = BoxLayout(orientation='horizontal')
            g.add_widget(choices[i])
            g.add_widget(self.parameters[i])
            self.map.append([g])
        for i in range(len(choices) - len(self.parameters)):
            self.map.append([choices[i + len(self.parameters)]])
        self.layout = BoxLayout(orientation='vertical')
        
        for row in self.map:
            l = BoxLayout(orientation='horizontal')
            for obj in row:
                l.add_widget(obj)
            self.layout.add_widget(l)
        
        return self.layout

    def _print(self, instance):
        print(self.input.text)


    #Video funcs
    def change_audio_bitrate_in_video(self, instance, bitrate):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -b:a {self.parameters[bitrate].text}k {abs_file.stem}_audio_compressed.{abs_file.suffix}"
        os.system(command)
    def change_fps(self, instance, fps):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -r {self.parameters[fps].text} {abs_file.stem}_editfps.{abs_file.suffix}"
        os.system(command)
    def extract_audio(self, instance):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vn {abs_file.stem}_extracted.mp3"
        os.system(command)
    def change_bitrate(self, instance, bitrate):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -b:v {self.parameters[bitrate].text}k {abs_file.stem}_changed_bitrate.{abs_file.suffix}"
        os.system(command)
    def convert_video(self, instance, format):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c copy {abs_file.stem}_converted.{self.parameters[format].text}"
        os.system(command)
    def compress_video_by_size(self, instance, size):
        pass
    def resize_video(self, instance, size):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vf 'scale={self.parameters[size].text}' {abs_file.stem}_resized.{abs_file.suffix}"
        os.system(command)

    #Image funcs
    def convert_image(self, instance, format):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} {abs_file.stem}.{self.parameters[format].text}"
        os.system(command)
    def resize_image(self, instance, size):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -s {self.parameters[size].text} {abs_file.stem}_resized.{abs_file.suffix}"
        os.system(command)
    def compress_image(self, instance, jpeg_parameter):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -q:v {self.parameters[jpeg_parameter].text} {abs_file.stem}_compressed.jpg"
        os.system(command)
    #Audio funcs
    # def convert_audio(self, instance, format):
    #     command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -s {size_x}x{size_y} {abs_file.name}_resized.{format}"
    #     os.system(command)
    def change_audio_bitrate(self, instance, bitrate):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libmp3lame -b:a {self.parameters[bitrate].text}k {abs_file.stem}_compressed.mp3"
        os.system(command)
    def change_audio_samplerate(self, instance, sample_rate):
        command = f"echo UMC && cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a copy -ar {self.parameters[sample_rate].text} {abs_file.stem}_{self.parameters[sample_rate].text}.wav"
        os.system(command)
    


Main().run()


# Имя с расширением: {p.name}   clip.mp4
# Имя без расширения: {p.stem}  clip
# Расширение файла: {p.suffix}  .mp4
# Родительская папка: {p.parent} D:\Клипы