import os

# exe erzeugen

# os.system("pyinstaller --onefile --noconsole PlotterWizard.py")

os.system("pyinstaller --onefile --icon=icons\\laser_YXc_icon.ico PlotterWizard.py")


# installer erstellen
os.system("iscc dist\\PlotterWizard.iss")