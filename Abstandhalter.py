import stuetzpunkt as sp
import csv
import time

class Abstandhalter:

    ausgangsPunkte = []
    stuetzpunkt = []
    bezugspunt_x = None
    bezugspunk_y = None

    type = None
    version = None


    def __init__(self, ausgangsPunkte,bezugspunt_x,bezugspunk_y):
        self.ausgangsPunkte = ausgangsPunkte
        self.bezugspunt_x = bezugspunt_x
        self.bezugspunk_y = bezugspunk_y

    def loecher_einlesen (self, Plotter):

        for Pkt in self.ausgangsPunkte:
            x = Pkt[0]+self.bezugspunt_x
            y = Pkt[1]+self.bezugspunk_y
            Plotter.move_kamera(x,y)
            #bild = Plotter.bild_erstellen()
            #self.loecher.append(id.Loch(x,y))

            rel_x, rel_y = Plotter.kamera.get_loch()
            self.loecher.append([x+rel_x-self.bezugspunt_x, y+rel_y-self.bezugspunk_y])
            Plotter.kamera.save_image()

    def csv_einlesen(self,pfad):
        with open(pfad, newline='') as csvfile:

            reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)

            for row in reader:
                if reader.line_num == 1:
                    self.type = row[0]
                    self.version = row[1]
                    continue
                elif reader.line_num == 2:
                    # Header infos
                    continue
                else:
                    self.stuetzpunkt.append(sp.stuetzpunkt(float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5])))

                print(', '.join(row))

    def csv_speichern(self,pfad):
        with open(pfad, 'w', newline='') as csvfile:

            fieldnames = ['nr', 'x', 'y', 'd1', 'd2', 'd3']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE)

            writer.writerow({'nr': self.type, 'x': self.version})
            writer.writeheader()
            nr = 1
            for punkt in self.stuetzpunkt:
                writer.writerow({'nr': nr, 'x': punkt.x, 'y': punkt.y, 'd1': punkt.d1, 'd2': punkt.d2, 'd3': punkt.d3})
                nr += 1


    def versionieren(self):
        self.version ="blub"



def main():
    ab = Abstandhalter(0,0,0)
    ab.csv_einlesen('CV95_stuetzkontur.csv')
    ab.versionieren()
    ab.csv_speichern('CV95_stuetzkontur.csv')


if __name__ == "__main__":
    main()

