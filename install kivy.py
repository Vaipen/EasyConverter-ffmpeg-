import os
try:
    os.system("pip install kivy")
    print("\nInstalled successfully")
    input("Press Enter to exit... ")
except Exception as e:
    print(f'Install error -> {e}')