extends Node
@onready var main: Control = $".."
var exe_path := OS.get_executable_path()
var exe_dir := exe_path.get_base_dir()
var ffmpeg_path := str(exe_dir+r"ffmpeg\bin\ffmpeg.exe")
var ffprobe_path := str(exe_dir+r"ffmpeg\bin\ffprobe.exe")

##region Video functions
func change_audio_bitrate_in_video(bitrate: int):
	var command = [ffmpeg_path+" -i "+main.file_path+" -b:a "+str(bitrate)+"k "+main.file_path.get_file().get_basename()+"_audio_compressed"+str(bitrate)+"k "+main.file_path.get_extension()]
	print(command)
	OS.execute("cd",["/D", exe_dir])
	OS.execute(ffmpeg_path,command)
#
#func change_fps(fps):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -r {self.parameters[fps].text} {abs_file.stem}_editfps{abs_file.suffix}"
	#os.system(command)
#
#func extract_audio():
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vn {abs_file.stem}_extracted.mp3"
	#os.system(command)
#
#func change_bitrate(bitrate):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -b:v {self.parameters[bitrate].text}k {abs_file.stem}_changed_bitrate{abs_file.suffix}"
	#os.system(command)
#
#func convert_video(format):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c copy {abs_file.stem}_converted.{self.parameters[format].text}"
	#os.system(command)
#
#func compress_video_by_size(size):
	#result = subprocess.run([f"{ffprobe_path}", "-v", "error", "-show_entries",
							#"format=duration", "-of",
							#"funcault=noprint_wrappers=1:nokey=1", file],
		#stdout=subprocess.PIPE,
		#stderr=subprocess.STDOUT)
	#duration = float(result.stdout)
#
	#filesize = os.path.getsize(file)/1024**2
#
	#new_bitrate = ((size * 8192) / duration)-128
	#print(duration)
	#print(filesize)
	#print(new_bitrate)
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -b:v {new_bitrate}k {abs_file.stem}_compressed{abs_file.suffix}"
	#os.system(command)
#
#func resize_video(size):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -vf scale={self.parameters[size].text} {abs_file.stem}_resized{abs_file.suffix}"
	#os.system(command)
##endregion
##region Image functions
#func convert_image(format):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} {abs_file.stem}.{self.parameters[format].text}"
	#os.system(command)
#func resize_image(size):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -s {self.parameters[size].text} {abs_file.stem}_resized{abs_file.suffix}"
	#os.system(command)
	#print(command)
#func compress_image(jpeg_parameter):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -q:v {self.parameters[jpeg_parameter].text} {abs_file.stem}_compressed.jpg"
	#os.system(command)
##endregion
##region Audio functions
#
#func convert_audio(format):
	#command = "echo empty"
	#if format == "wav":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a pcm_s16le {abs_file.name}.{format}" #Несжатый, высокое
	#if format == "mp3":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libmp3lame {abs_file.name}.{format}" #Универсальный
	#if format == "flac":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a flac -compression_level 8 {abs_file.name}.{format}"# Lossless
	#if format == "ogg":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libvorbis {abs_file.name}.{format}"
	#if format == "aac":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a aac {abs_file.name}.{format}"
	#if format == "opus":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libopus {abs_file.name}.{format}"
	#if format == "wma":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a wmav2 {abs_file.name}.{format}"
	#if format == "aiff":
		#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a pcm_s16be {abs_file.name}.{format}"
#
	#os.system(command)
#func change_audio_bitrate(bitrate):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -c:a libmp3lame -b:a {self.parameters[bitrate].text}k {abs_file.stem}_compressed.mp3"
	#os.system(command)
#func change_audio_samplerate(sample_rate):
	#command = f"cd /D {os.path.dirname(file)} && {ffmpeg_path} -i {abs_file.name} -ar {self.parameters[sample_rate].text} {abs_file.stem}_{self.parameters[sample_rate].text}.wav"
	#os.system(command)
##endregion
