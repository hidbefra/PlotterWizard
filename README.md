# PlotterWizard
customized zünd communicator

Dieses Tool erlaubt es Zünd HPGL programme in unterschiedlichen Nullpunkten auszuführen.

- Ein Arbeitsschrit besteht aus einem Beliebigen HPGL programm. Schnitparameter können über ein GUI angepast werden
- Mehrere Arbeitsschritte werden zu einem Prozess zussammengefast
- Mehrere Prozesse zu einer Schablone

Jedes "level" kann über eine Nulpunktverschiebung angepast werden.

Die Programme werden über RS232 an den Ploter gesendet


Instalation:

Für Windows:
  den Installer  PlotterWizard/dist/setup PlotterWizard.exe benutzen

Für Linux:
Für Entwickerl welche den Cood weiter verwenden möchten:
- Das Projekt ist mitPyCharm erstelt worden
- Verwendet wurde Python 3.7 als Virtualenv Enviroment
- zu Beginn _externe_inhalte_installieren.py ausführen. Dieses instaliert alle nötigen packages
- Das Programm startet mit PlotterWizard.py
- _main.py übersetzt alle QT*.ui Datein und startet dan das Programm.
- _exe_bauen.py übersetzt das Program in eine exe und erstelt den Installer ( in der Datei "
PlotterWizard/dist/PlotterWizard.iss " muss die Zeile:" Source: "C:\Users\franz.hidber\Desktop\KonturGenerator\dist\PlotterWizard.exe";" angepast werden)

