import os
import sys
import shutil
from pathlib import Path

def create_bat_launcher():
    """Creates BAT file for launch"""
    script_dir = Path(__file__).parent
    python_exe = sys.executable
    main_script = script_dir / "media_converter.py"
    
    bat_content = f'''@echo off
chcp 65001 >nul
echo Media Converter...
"{python_exe}" "{main_script}" "%1"
pause
'''
    
    bat_file = script_dir / "converter.bat"
    with open(bat_file, 'w', encoding='utf-8') as f:
        f.write(bat_content)
    
    return bat_file

def install_to_sendto():
    """Installs to 'Send to' folder"""
    try:
        # Get SendTo folder
        sendto_path = Path(os.path.expanduser('~')) / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'SendTo'
        
        if not sendto_path.exists():
            print("❌ 'SendTo' folder not found!")
            return False
        
        # Create BAT file
        bat_file = create_bat_launcher()
        
        # Create shortcut in SendTo
        from win32com.client import Dispatch
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(str(sendto_path / "Media Converter.lnk"))
        shortcut.Targetpath = str(bat_file)
        shortcut.WorkingDirectory = str(bat_file.parent)
        shortcut.save()
        
        print("✅ Successfully added to 'Send to' menu!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Trying alternative method...")
        return install_to_sendto_simple()

def install_to_sendto_simple():
    """Alternative method - copy BAT file directly"""
    try:
        sendto_path = Path(os.path.expanduser('~')) / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'SendTo'
        
        if not sendto_path.exists():
            print("❌ 'SendTo' folder not found!")
            return False
        
        # Create BAT file
        bat_file = create_bat_launcher()
        
        # Copy BAT file to SendTo with different name
        sendto_bat = sendto_path / "Media Converter.bat"
        shutil.copy2(bat_file, sendto_bat)
        
        print("✅ Successfully added to 'Send to' menu!")
        return True
        
    except Exception as e:
        print(f"❌ Alternative method error: {e}")
        return False

def check_ffmpeg():
    """Checks if FFmpeg is installed"""
    if shutil.which("ffmpeg") is None:
        print("❌ FFmpeg not found in PATH!")
        print("Download FFmpeg from https://ffmpeg.org/download.html")
        print("Extract and add bin folder to PATH")
        return False
    print("✅ FFmpeg found")
    return True

def main():
    print("=== Media Converter - Installation ===")
    print("Installing to 'Send to' menu...")
    
    # Check FFmpeg
    if not check_ffmpeg():
        input("Press Enter to exit...")
        return
    
    # Install to SendTo
    if install_to_sendto():
        print("\n🎉 INSTALLATION COMPLETED!")
        print("\n📋 HOW TO USE:")
        print("1. RIGHT-click on a file")
        print("2. Select 'Send to'")
        print("3. Click 'Media Converter'")
        print("4. A window with action choices will open")
    else:
        print("\n❌ Installation failed!")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main
