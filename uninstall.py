```python
import os
from pathlib import Path

def remove_from_sendto():
    """Removes from SendTo folder"""
    try:
        sendto_path = Path(os.path.expanduser('~')) / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'SendTo'
        
        files_to_remove = [
            "Media Converter.bat",
            "Media Converter.lnk",
            "converter.bat"
        ]
        
        removed_count = 0
        for file in files_to_remove:
            file_path = sendto_path / file
            if file_path.exists():
                file_path.unlink()
                print(f"✅ Removed: {file}")
                removed_count += 1
        
        # Remove local BAT file
        local_bat = Path("converter.bat")
        if local_bat.exists():
            local_bat.unlink()
            print("✅ Removed local BAT file")
        
        return removed_count
        
    except Exception as e:
        print(f"❌ Removal error: {e}")
        return 0

def main():
    print("=== Media Converter Removal ===")
    
    removed = remove_from_sendto()
    
    if removed > 0:
        print(f"\n✅ Removed {removed} files")
    else:
        print("\nℹ️ Nothing to remove")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
```