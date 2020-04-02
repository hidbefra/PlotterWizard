# install opencv-python
# install PyQt5
# install PyQt5-tool
# install scipy
# install pyserial
# install pyinstaller

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("opencv-python")
install("PyQt5")
install("PyQt5-tools")
install("scipy")
install("pyserial")
install("pyinstaller")