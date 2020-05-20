import model_Plotter as pt
import Abstandhalter as ah

def main():

    plotter = pt.Plotter()
    plotter.init_rs232("COM3")

    plotter.kamera_init(1)

    #plotter.move(0, 0)

    punkte = [[-411.8,-257.6],
              [-256.1,-412.42],
              [-35.47,-420.29],
              [194.56,-419.58],
              [414.33,-413.51],
              [421.57,-193.87],
              [421.95,36.55],
              [411.63,257.85],
              [256.06,412.65],
              [35.45,421.34],
              [-194.32,421.05],
              [-414.11,413.71],
              [-420.9,194.23],
              [-421.23,-36.35]]

    punkte = [[-411.800,-256.731],
[-256.555,-412.089],
[-35.553,-420.911],
[194.229,-420.780],
[413.958,-413.800],
[421.446,-194.284],
[421.619,36.012],
[412.540,256.733],
[257.219,411.740],
[36.402,420.885],
[-193.534,421.091],
[-413.241,413.462],
[-420.610,193.940],
[-420.899,-36.060]]


    pezugspunkt_x = 477.89 - (104.15 - 85)
    pezugspunkt_y = 732.64 - (302.39 - 200)
    abstandhalter = ah.Abstandhalter(punkte,pezugspunkt_x,pezugspunkt_y)

    abstandhalter.loecher_einlesen(plotter)

    data=abstandhalter.loecher

    with open('loecher.txt', 'w') as out_file:
        for pont in data:
            out_file.write("[{:.3f},{:.3f}],\n".format(pont[0], pont[1]))


if __name__ == "__main__":
    main()
