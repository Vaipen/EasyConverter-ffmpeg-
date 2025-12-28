import os
import sys

from kivy.app import App  # чтобы все писать не с нуля
from kivy.uix.boxlayout import BoxLayout  # единственный который я помню как работает
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
import subprocess
import json
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

#Color palette (0.0 - 1.0)


pallete_dark = {"Background": (18/255,17/255,19/255,1),
            "Back": (34/255,29/255,37/255,1),
            "Main": (137/255,152/255,120/255,1),
            "Highlight": (228/255,230/255,195/255,1),
            "Contrast": (247/255,247/255,242/255,1)}

pallete_darkblue = {"Background": (18/255,17/255,19/255,1),
            "Back": (34/255,29/255,37/255,1),
            "Main": (137/255,152/255,120/255,1),
            "Highlight": (228/255,230/255,195/255,1),
            "Contrast": (247/255,247/255,242/255,1)}

pallete_white = {"Background": (18/255,17/255,19/255,1),
            "Back": (34/255,29/255,37/255,1),
            "Main": (255/255,255/255,255/255,1),
            "Highlight": (228/255,230/255,195/255,1),
            "Contrast": (247/255,247/255,242/255,1)}

pallete_whiteblue = {"Background": (18/255,17/255,19/255,1),
            "Back": (34/255,29/255,37/255,1),
            "Main": (137/255,152/255,120/255,1),
            "Highlight": (228/255,230/255,195/255,1),
            "Contrast": (247/255,247/255,242/255,1)}

pallete_green = {"Background": (18/255,17/255,19/255,1),
            "Back": (34/255,29/255,37/255,1),
            "Main": (137/255,152/255,120/255,1),
            "Highlight": (228/255,230/255,195/255,1),
            "Contrast": (247/255,247/255,242/255,1)}

pallete_pink = {"Background": (96/255,36/255,55/255,1),
            "Back": (138/255,40/255,70/255,1),
            "Main": (224/255,122/255,162/255,1),
            "Highlight": (225/255,194/255,212/255,1),
            "Contrast": (225/255,224/255,233/255,1)}

mainpallete = pallete_green

script_path = os.path.abspath(__file__)
ffmpeg_folder = r"ffmpeg\bin\ffmpeg.exe"
ffprobe_folder = r"ffmpeg\bin\ffprobe.exe"
ffmpeg_path= script_path.replace("converter.py","")+ffmpeg_folder
ffprobe_path= script_path.replace("converter.py","")+ffprobe_folder

dev_mode=0
if dev_mode == 1:
    file = "D:\Клипы\clip.mp4"
else:
    file = str(sys.argv[1])
abs_file = Path(file)
file_types = {
    'image': ("jpg", "jpeg", "png", "bmp", "gif", "webp"),
    'video': ("mp4", "avi", "mov", "mkv", "webm", "flv", "wmv"),
    'audio': ("mp3", "wav", "flac", "aac", "ogg", "m4a")
}

buttons_design = {
    'background_color': mainpallete["Main"],
    # 'background_normal': '',
    'color': mainpallete["Highlight"],
    # 'border_width': 2,
    # 'outline_color': (1,1,1,1)
} #НАААЙС РАБОТАЕТ <<< а хули оно работаект то как новые добавить? ало ало хуем по лбу не дало??????????????????? ????<<<?????? я сделал
label_design = {
    'color': mainpallete["Contrast"],
    'font_name': "misc\InterTight-SemiBold.ttf",
    'font_size':13
    # 'border_width': 2,
    # 'outline_color': (1,1,1,1)
}
edit_box_design = {
    'multiline': False,
    'background_color': mainpallete["Back"], 
    'foreground_color': mainpallete["Contrast"],
    'font_name': "misc/InterTight-Medium.ttf"
    # 'outline_width': 2,
    # 'outline_color': (1,1,1,1)
}

Window.clearcolor = mainpallete["Background"]





class WRecode(App):
    def build(self):
        self.map = []
         # я щас прийду
        file_layout = BoxLayout(orientation='horizontal')
        input_layout = BoxLayout(orientation='vertical')
        input_label = Label(text=f'Input file:', font_name="misc\InterTight-MediumItalic.ttf", font_size=22, color=mainpallete["Contrast"])
        # with input_label.canvas:
        #     Color(0, 1, 0, 0.25)
        #     Rectangle(pos=input_label.pos, size=input_label.size)

        # def change_file_path(self, instance):
        #     abs_file = Path(self.input.text)

        input_layout.add_widget(input_label)
        self.input = TextInput(text=file, on_text_validate=self.change_file_path, **edit_box_design, font_size=18) # пиши в лс я без звука щаSyntaxError: positional argument follows keyword argument где ну я выделяю блят, ты
        input_layout.add_widget(self.input)
        file_layout.add_widget(input_layout)
        self.map.append([file_layout])

        choices = []

        # if " " in file:
        #     self.parameters = []
        #     choices = [Label(text='Try renaming the file so that the name\ndoes not contain spaces or special symbols', font_name="misc\InterTight-SemiBold.ttf", font_size=17)]
        #     labels = [Label(text='')]
            
        if file.split('.')[-1] in file_types['image']:
            self.parameters = [TextInput(**edit_box_design) for _ in range(3)]
            choices = [
                Button(text='Convert', on_press=lambda *args: self.convert_image(self, 0), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Resize', on_press=lambda *args: self.resize_image(self, 1), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Compress', on_press=lambda *args: self.compress_image(self, 2), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design)
                # Button(text='Compress with size', on_press=self.compress, size_hint = (2,1))
            ]
            labels = [
                Label(text=f'Write this formats(without .):\n {" ".join(file_types["image"])}', **label_design),
                Label(text='Write size e.g."1000:1000"', **label_design),
                Label(text='JPEG Compression (1-100)', **label_design)
            ]
        elif file.split('.')[-1] in file_types['video']:
            self.parameters = [TextInput(**edit_box_design) for _ in range(6)]
            choices = [
                Button(text='Convert', on_press=lambda *args: self.convert_video(self, 0), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design), # FFFF 424242 4242424242244242424242424242424242424242424242424242 оставляем похуй
                Button(text='Compress', on_press=lambda *args: self.compress_video_by_size(self, 1), size_hint=(2, 1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Change FPS', on_press=lambda *args: self.change_fps(self, 2), size_hint=(2, 1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Resize', on_press=lambda *args: self.resize_video(self, 3), size_hint=(2, 1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Change bitrate', on_press=lambda *args: self.change_bitrate(self, 4), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Change audiotrack bitrate', on_press=lambda *args: self.change_audio_bitrate_in_video(self, 5), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=30, **buttons_design),
                Button(text='Extract audio', on_press=self.extract_audio, size_hint=(3,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design)
            ]
            labels = [
                Label(text=f'Write this formats(without .):\n {" ".join(file_types["video"])}', **label_design),
                Label(text='Just write size in MB', **label_design),
                Label(text='Write FPS', **label_design),
                Label(text='Write size\n e.g."1000:1000"', **label_design),
                Label(text='Write bitrate\n in kb/s (only value)', **label_design),
                Label(text='Write bitrate\n in kb/s (only value)', **label_design),
                Label(text='Extract audiotrack\n from video', **label_design)
            ]
        elif file.split('.')[-1] in file_types['audio']:
            self.parameters = [TextInput(**edit_box_design) for _ in range(3)]
            choices = [
                Button(text='Convert', on_press=lambda *args: self.convert_audio(self, 0), size_hint = (2, 1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Change bitrate', on_press=lambda *args: self.change_audio_bitrate(self, 1), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=42, **buttons_design),
                Button(text='Change sampling frequency', on_press=lambda *args: self.change_audio_samplerate(self, 2), size_hint = (2,1), font_name="misc\InterTight-Black.ttf", font_size=30, **buttons_design) 
                # Button(text='Compress with size', on_press=self.com, size_hint = (2,1))
            ]
            labels = [
                Label(text=f'Write this formats(without .):\n {" ".join(file_types["audio"])}', **label_design),
                Label(text='Write bitrate in kb/s (only value)', **label_design),
                Label(text='Write sample rate', **label_design)
            ]
        else:
            self.parameters = []
            choices = [Label(text='File not supported', font_name="misc\InterTight-SemiBold.ttf", font_size=17)]
            labels = [Label(text='')]

        # for i in labels:
        #     with i.canvas:
        #         Color(0, 1, 0, 0.25)
        #         Rectangle(pos=i.pos, size=i.size)

        dropdown = DropDown()


        for i in range(len(self.parameters)):
            g = BoxLayout(orientation='horizontal')
            g.add_widget(choices[i])
            g.add_widget(self.parameters[i])
            g.add_widget(labels[i])
            self.map.append([g])
        for i in range(len(choices) - len(self.parameters)):
            g = BoxLayout(orientation='horizontal')
            g.add_widget(choices[i + len(self.parameters)])
            g.add_widget(labels[i + len(self.parameters)])
            self.map.append([g])
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
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -b:a {self.parameters[bitrate].text}k {abs_file.stem}_audio_compressed{abs_file.suffix}"
        os.system(command)

    def change_fps(self, instance, fps):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f'cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vf "fps={self.parameters[fps].text}" {abs_file.stem}_editfps{abs_file.suffix}'
        os.system(command)

    def extract_audio(self, instance):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vn {abs_file.stem}_extracted.mp3"
        os.system(command)

    def change_bitrate(self, instance, bitrate):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -b:v {self.parameters[bitrate].text}k {abs_file.stem}_changed_bitrate{abs_file.suffix}"
        os.system(command)

    def convert_video(self, instance, format):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c copy {abs_file.stem}_converted.{self.parameters[format].text}"
        os.system(command)

    def compress_video_by_size(self, instance, target_size_mb):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        
        try:
            target_size_mb = float(self.parameters[target_size_mb].text)
            if target_size_mb <= 0:
                raise ValueError
        except:
            print("Invalid target size")
            return
        
        # ffprobe
        cmd = [
            ffprobe_path, "-v","error",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            file
        ]

        probe = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if probe.returncode != 0:
            raise ValueError(f"ffprobe error: {probe.stderr}")

        data = json.loads(probe.stdout)

        duration = float(data["format"]["duration"])
        if duration <= 0:
            raise ValueError("Duration must be more than 0")

        audio_bitrate = 128000
        width = height = None

        for stream in data["streams"]:
            if stream.get("codec_type") == "audio" and "bit_rate" in stream:
                audio_bitrate = int(stream["bit_rate"])
                break

        for stream in data["streams"]:
            if stream.get("codec_type") == "video":
                width = int(stream.get("width", 0))
                height = int(stream.get("height", 0))
                break

        target_bits = target_size_mb *8*1024*1024
        total_bitrate = target_bits / duration
        audio_steps = [160000, 128000, 96000, 64000, 48000]
        audio_steps = [a for a in audio_steps if a <= audio_bitrate]

        video_bitrate = total_bitrate - audio_bitrate

        for a in audio_steps:
            vb = total_bitrate - a
            if vb >= 300_000:
                audio_bitrate = a
                video_bitrate = vb
                break


        if video_bitrate <= 0:
            raise ValueError("Size too small")

        video_kbps = int(video_bitrate/1000)
        audio_kbps = int(audio_bitrate/1000)

        dir_name = abs_file.parent
        base_name = abs_file.stem
        ext = abs_file.suffix
        # output_file = str(dir_name / f"{base_name}_compressed{ext}")
        passlog = dir_name / base_name

        if os.path.exists("ffmpeg2pass-0.log"):
            os.remove("ffmpeg2pass-0.log")

        null_out = "NUL" if os.name == "nt" else "/dev/null"

        pass1 = (f'{ffmpeg_path} -fflags +genpts+igndts -avoid_negative_ts make_zero -loglevel warning  -i "{file}" -fps_mode passthrough -c:v libx264 -b:v {video_kbps}k -pass 1 -passlogfile "{passlog}" -an -f null {null_out}')
        pass2 = (f'{ffmpeg_path} -fflags +genpts+igndts -avoid_negative_ts make_zero -loglevel warning  -i "{file}" -fps_mode passthrough -c:v libx264 -b:v {video_kbps}k -pass 2 -passlogfile "{passlog}" -c:a aac -b:a {audio_kbps}k {abs_file.stem}_compessed{abs_file.suffix}')
        os.system(pass1)
        os.system(pass2)

        for ext in (".log", ".log.mbtree"):
            log_file = Path(str(passlog) + "-0" + ext)
            if log_file.exists():
                log_file.unlink()

    def resize_video(self, instance, size):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vf scale={self.parameters[size].text} {abs_file.stem}_resized{abs_file.suffix}"
        os.system(command)

    #Image funcs
    def convert_image(self, instance, format):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} {abs_file.stem}.{self.parameters[format].text}"
        os.system(command)
    def resize_image(self, instance, size):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -s {self.parameters[size].text} {abs_file.stem}_resized{abs_file.suffix}"
        os.system(command)
        print(command)
    def compress_image(self, instance, jpeg_parameter):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -q:v {self.parameters[jpeg_parameter].text} {abs_file.stem}_compressed.jpg"
        os.system(command)
    #Audio funcs
    def convert_audio(self, instance, format):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        if format == "wav":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a pcm_s16le {abs_file.name}.{format}" #Несжатый, высокое
        if format == "mp3":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libmp3lame {abs_file.name}.{format}" #Универсальный
        if format == "flac":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a flac -compression_level 8 {abs_file.name}.{format}"# Lossless
        if format == "ogg":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libvorbis {abs_file.name}.{format}"
        if format == "aac":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a aac {abs_file.name}.{format}"
        if format == "opus":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libopus {abs_file.name}.{format}"
        if format == "wma":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a wmav2 {abs_file.name}.{format}"
        if format == "aiff":
            command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a pcm_s16be {abs_file.name}.{format}"
        print("selected format ", format)
        os.system(command)
    def change_audio_bitrate(self, instance, bitrate):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libmp3lame -b:a {self.parameters[bitrate].text}k {abs_file.stem}_compressed.mp3"
        os.system(command)
    def change_audio_samplerate(self, instance, sample_rate):
        if " " in str(abs_file.name):
            print("The file name contains spaces, please remove them.")
            return
        command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -ar {self.parameters[sample_rate].text} {abs_file.stem}_{self.parameters[sample_rate].text}.wav"
        os.system(command)

    def change_file_path(self, instance):
        abs_file = Path(self.input.text)

WRecode().run()


# Имя с расширением: {p.name}   clip.mp4
# Имя без расширения: {p.stem}  clip
# Расширение файла: {p.suffix}  .mp4
# Родительская папка: {p.parent} D:\Клипы