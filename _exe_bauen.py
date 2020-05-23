import os

# exe erzeugen

os.system("pyinstaller --onefile --noconsole gui_main.py")#

os.system("pyinstaller --onefile --windowed --icon=icons\\laser_YXc_icon.ico gui_main.py")