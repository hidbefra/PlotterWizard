import os

def ui_translate():
    pfad = "venv\\Scripts\\pyuic5.exe"

    os.system(pfad + " -x -o QT_MainWindow_schnittomat.py QT_MainWindow_schnittomat.ui") # gui übersetzten

    os.system(pfad + " -x -o QT_Arbeitsschritt.py QT_Arbeitsschritt.ui") # gui übersetzten

    os.system(pfad + " -x -o QT_Prozess.py QT_Prozess.ui") # gui übersetzten

    os.system(pfad + " -x -o QT_Schablone.py QT_Schablone.ui") # gui übersetzten


if __name__ == "__main__":
    print("translate ui to py")
    print("Current Working Directory ", os.getcwd())
    ui_translate()