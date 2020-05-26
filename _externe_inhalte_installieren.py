import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("opencv-python")
install("PyQt5")
install("pyqt5-tools")
install("scipy")
install("pyserial")
# install("pyinstaller")
install("https://github.com/pyinstaller/pyinstaller/archive/develop.zip")
# https://stackoverflow.com/questions/37815371/pyinstaller-failed-to-execute-script-pyi-rth-pkgres-and-missing-packages

#manuel https://jrsoftware.org/isdl.php instalieren und programm order in den Systemvariablne eintragen unter PATH