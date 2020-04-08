import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("opencv-python")
install("PyQt5")
install("pyqt5-tools")
install("scipy")
install("pyserial")
install("pyinstaller")