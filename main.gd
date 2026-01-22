extends Control

var file_path: String = ""
@export var input_file_path : Button

var file_types = {
	'image': ["jpg", "jpeg", "png", "bmp", "gif", "webp"],
	'video': ["mp4", "avi", "mov", "mkv", "webm", "flv", "wmv"],
	'audio': ["mp3", "wav", "flac", "aac", "ogg", "m4a"]
}

func _ready() -> void:
	var args = OS.get_cmdline_args()
	if args.size() > 1:
		file_path = args[1].strip_edges()
		print("Args: ", file_path)
	else:
		push_error("Invalid file path")
	_update_inputfile(file_path)

func _convert_pressed() -> void:
	pass # Replace with function body.


func _compress_pressed() -> void:
	pass # Replace with function body.


func _editfps_pressed() -> void:
	pass # Replace with function body.


func _extractaudio_pressed() -> void:
	pass # Replace with function body.


func _select_file_pressed() -> void:
	$MarginContainer/VBoxContainer/Header/FilePath/FileDialog.show()
func _on_file_selected(path: String) -> void:
	_update_inputfile(path)

func _update_inputfile(path: String) -> void:
	file_path = path
	input_file_path.text = path
	print("File selected: ", path)


func _on_settings_pressed() -> void:
	$MarginContainer/VBoxContainer/Bottom/Settings/Window.show()
