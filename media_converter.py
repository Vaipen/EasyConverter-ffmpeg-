import os
import sys
import subprocess
import json
from pathlib import Path

class MediaConverter:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_type = self.detect_file_type()
        
    def detect_file_type(self):
        extension = self.file_path.suffix.lower()
        
        audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma']
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.mpeg', '.mpg', '.webm']
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
        
        if extension in audio_extensions:
            return 'audio'
        elif extension in video_extensions:
            return 'video'
        elif extension in image_extensions:
            return 'image'
        else:
            return 'unknown'
    
    def run_ffmpeg(self, command):
        try:
            print(f"🔄 Processing: {command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
            if result.returncode == 0:
                print("✅ Operation completed successfully!")
                return True
            else:
                print(f"❌ FFmpeg error: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Runtime error: {e}")
            return False
    
    def show_menu(self):
        if self.file_type == 'audio':
            self.show_audio_menu()
        elif self.file_type == 'video':
            self.show_video_menu()
        elif self.file_type == 'image':
            self.show_image_menu()
        else:
            print("❌ Unsupported file type!")
    
    def show_audio_menu(self):
        while True:
            print(f"\n🎵 AUDIO CONVERTER: {self.file_path.name}")
            print("1. Convert to another format")
            print("2. Change bitrate")
            print("3. Change sample rate")
            print("4. Trim audio")
            print("5. Compress audio (reduce bitrate)")
            print("0. Back/Exit")
            
            choice = input("Select an action: ").strip()
            
            if choice == '1':
                self.convert_audio_format()
            elif choice == '2':
                self.change_audio_bitrate()
            elif choice == '3':
                self.change_sample_rate()
            elif choice == '4':
                self.trim_audio()
            elif choice == '5':
                self.compress_audio()
            elif choice in ['0', '']:
                break
            else:
                print("❌ Invalid choice!")
    
    def show_video_menu(self):
        while True:
            print(f"\n🎬 VIDEO CONVERTER: {self.file_path.name}")
            print("1. Convert to another format")
            print("2. Change video bitrate")
            print("3. Change resolution")
            print("4. Change frame rate")
            print("5. Extract audio")
            print("6. Trim video")
            print("7. Compress video (reduce bitrate)")
            print("8. Compress audio track in video")
            print("0. Back/Exit")
            
            choice = input("Select an action: ").strip()
            
            if choice == '1':
                self.convert_video_format()
            elif choice == '2':
                self.change_video_bitrate()
            elif choice == '3':
                self.change_resolution()
            elif choice == '4':
                self.change_framerate()
            elif choice == '5':
                self.extract_audio_from_video()
            elif choice == '6':
                self.trim_video()
            elif choice == '7':
                self.compress_video()
            elif choice == '8':
                self.compress_video_audio()
            elif choice in ['0', '']:
                break
            else:
                print("❌ Invalid choice!")
    
    def show_image_menu(self):
        while True:
            print(f"\n🖼️ IMAGE CONVERTER: {self.file_path.name}")
            print("1. Convert to another format")
            print("2. Resize")
            print("3. Compress image")
            print("4. Change quality")
            print("0. Back/Exit")

            choice = input("Select an action: ").strip()
            
            if choice == '1':
                self.convert_image_format()
            elif choice == '2':
                self.resize_image()
            elif choice == '3':
                self.compress_image()
            elif choice == '4':
                self.change_image_quality()
            elif choice in ['0', '']:
                break
            else:
                print("❌ Invalid choice!")
    
    # Audio functions
    def convert_audio_format(self):
        formats = {
            '1': ('mp3', 'libmp3lame'),
            '2': ('wav', 'pcm_s16le'),
            '3': ('flac', 'flac'),
            '4': ('aac', 'aac'),
            '5': ('ogg', 'libvorbis')
        }
        print("\n🎯 Select format:")
        print("1. MP3")
        print("2. WAV")
        print("3. FLAC")
        print("4. AAC")
        print("5. OGG")
        
        format_choice = input("Your choice: ").strip()
        
        if format_choice in formats:
            output_format, codec = formats[format_choice]
            output_file = self.file_path.with_suffix(f'.{output_format}')
            command = f'ffmpeg -i "{self.file_path}" -c:a {codec} "{output_file}"'
            self.run_ffmpeg(command)
        else:
            print("❌ Invalid choice!")
    
    def change_audio_bitrate(self):
        bitrate = input("Enter bitrate (e.g. 128k, 192k, 320k): ").strip()
        if not bitrate.endswith('k'):
            bitrate += 'k'
        
        output_file = self.file_path.with_suffix(f'.{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -b:a {bitrate} "{output_file}"'
        self.run_ffmpeg(command)
    
    def compress_audio(self):
        print("\n🎯 Audio compression (bitrate reduction):")
        print("1. Low quality (96k)")
        print("2. Medium quality (128k)")
        print("3. Good quality (192k)")
        print("4. Specify a custom bitrate")
        
        choice = input("Your choice: ").strip()
        
        bitrates = {'1': '96k', '2': '128k', '3': '192k'}
        
        if choice in bitrates:
            bitrate = bitrates[choice]
        elif choice == '4':
            bitrate = input("Enter bitrate (e.g. 64k, 128k): ").strip()
            if not bitrate.endswith('k'):
                bitrate += 'k'
        else:
            print("❌ Invalid choice!")
            return
        
        output_file = self.file_path.with_suffix(f'.compressed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -b:a {bitrate} "{output_file}"'
        self.run_ffmpeg(command)
    
    def change_sample_rate(self):
        samplerate = input("Enter sample rate (e.g. 44100, 48000): ").strip()
        output_file = self.file_path.with_suffix(f'.{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -ar {samplerate} "{output_file}"'
        self.run_ffmpeg(command)
    
    def trim_audio(self):
        start = input("Trim start (format: HH:MM:SS or seconds): ").strip()
        end = input("Trim end (format: HH:MM:SS or seconds): ").strip()
        output_file = self.file_path.with_suffix(f'.trimmed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -ss {start} -to {end} "{output_file}"'
        self.run_ffmpeg(command)
    
    # Video functions
    def convert_video_format(self):
        formats = {
            '1': 'mp4',
            '2': 'avi',
            '3': 'mov',
            '4': 'mkv',
            '5': 'webm'
        }
        print("\n🎯 Select format:")
        print("1. MP4")
        print("2. AVI")
        print("3. MOV")
        print("4. MKV")
        print("5. WebM")
        
        format_choice = input("Your choice: ").strip()
        
        if format_choice in formats:
            output_format = formats[format_choice]
            output_file = self.file_path.with_suffix(f'.{output_format}')
            command = f'ffmpeg -i "{self.file_path}" "{output_file}"'
            self.run_ffmpeg(command)
        else:
            print("❌ Invalid choice!")
    
    def change_video_bitrate(self):
        bitrate = input("Enter video bitrate (e.g. 1M, 2M, 500k): ").strip()
        output_file = self.file_path.with_suffix(f'.compressed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -b:v {bitrate} "{output_file}"'
        self.run_ffmpeg(command)
    
    def compress_video(self):
        print("\n🎯 Video Compression:")
        print("1. Heavy compression (smaller size)")
        print("2. Medium compression")
        print("3. Light compression (better quality)")
        print("4. Specify CRF manually (18-28)")
        
        choice = input("Your choice: ").strip()
        
        crf_values = {'1': '28', '2': '23', '3': '18'}
        
        if choice in crf_values:
            crf = crf_values[choice]
        elif choice == '4':
            crf = input("Enter CRF value (18-28, lower=better quality): ").strip()
        else:
            print("❌ Invalid choice!")
            return
        
        output_file = self.file_path.with_suffix(f'.compressed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -vcodec libx264 -crf {crf} "{output_file}"'
        self.run_ffmpeg(command)
    
    def compress_video_audio(self):
        print("\n🎯 Compress audio track in video:")
        bitrate = input("Enter audio bitrate (e.g. 128k, 64k): ").strip()
        if not bitrate.endswith('k'):
            bitrate += 'k'
        
        output_file = self.file_path.with_suffix(f'.audio_compressed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -c:v copy -b:a {bitrate} "{output_file}"'
        self.run_ffmpeg(command)
    
    def change_resolution(self):
        resolution = input("Enter resolution (e.g. 1280x720, 1920x1080, 50%): ").strip()
        output_file = self.file_path.with_suffix(f'.resized{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -vf "scale={resolution}" "{output_file}"'
        self.run_ffmpeg(command)
    
    def change_framerate(self):
        fps = input("Enter frame rate (e.g. 24, 30, 60): ").strip()
        output_file = self.file_path.with_suffix(f'.{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -r {fps} "{output_file}"'
        self.run_ffmpeg(command)
    
    def extract_audio_from_video(self):
        format_choice = input("Audio format (mp3/wav): ").lower().strip()
        output_file = self.file_path.with_suffix(f'.{format_choice}')
        command = f'ffmpeg -i "{self.file_path}" -q:a 0 -map a "{output_file}"'
        self.run_ffmpeg(command)
    
    def trim_video(self):
        start = input("Trim start (format: HH:MM:SS): ").strip()
        end = input("Trim end (format: HH:MM:SS): ").strip()
        output_file = self.file_path.with_suffix(f'.trimmed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -ss {start} -to {end} "{output_file}"'
        self.run_ffmpeg(command)
    
    # Image functions
    def convert_image_format(self):
        formats = {
            '1': 'jpg',
            '2': 'png',
            '3': 'webp',
            '4': 'bmp'
        }
        print("\n🎯 Select format:")
        print("1. JPG")
        print("2. PNG")
        print("3. WebP")
        print("4. BMP")
        
        format_choice = input("Your choice: ").strip()
        
        if format_choice in formats:
            output_format = formats[format_choice]
            output_file = self.file_path.with_suffix(f'.{output_format}')
            command = f'ffmpeg -i "{self.file_path}" "{output_file}"'
            self.run_ffmpeg(command)
        else:
            print("❌ Invalid choice!")
    
    def resize_image(self):
        size = input("Enter size (e.g. 50% or 800x600): ").strip()
        output_file = self.file_path.with_suffix(f'.resized{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -vf "scale={size}" "{output_file}"'
        self.run_ffmpeg(command)
    
    def compress_image(self):
        quality = input("Enter quality (1-100, lower=more compression): ").strip()
        output_file = self.file_path.with_suffix(f'.compressed{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -q:v {quality} "{output_file}"'
        self.run_ffmpeg(command)
    
    def change_image_quality(self):
        quality = input("Enter JPG quality (1-100): ").strip()
        output_file = self.file_path.with_suffix(f'.quality{self.file_path.suffix}')
        command = f'ffmpeg -i "{self.file_path}" -qscale:v {quality} "{output_file}"'
        self.run_ffmpeg(command)

def main():
    if len(sys.argv) < 2:
        print("❌ Drag and drop a file onto this script or specify a file path!")
        input("Press Enter to exit...")
        return
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print("❌ File not found!")
        input("Press Enter to exit...")
        return
    
    converter = MediaConverter(file_path)
    converter.show_menu()

if __name__ == "__main__":
    main()