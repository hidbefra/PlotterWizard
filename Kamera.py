import cv2 #opencv-python
import numpy as np
import os

class Kamera:

    cap = None
    ratio = None
    offset_x = None
    offset_y = None
    count = None

    def __init__(self,device_index=1):
        self.cap = cv2.VideoCapture(device_index, cv2.CAP_DSHOW)
        self.offset_x = 104.68-85
        self.offset_y = 300.33-200
        self.ratio = 145 / 3 #pix/mm
        self.count = 0

    def __del__(self):
        self.cap.release()

    def save_image(self):
        ret, img = self.cap.read()
        ret, img = self.cap.read()
        ret, img = self.cap.read()
        status = cv2.imwrite('./Testbilder/loch_{}.png'.format(self.count), img)
        self.count=self.count+1

    def get_image(self):
        ret, frame = self.cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('test', image)
        cv2.waitKey(0)
        return image

    def HoughCircles(self):

        for file in os.listdir('./Testbilder/'):
            src = cv2.imread('./Testbilder/'+file, cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 500,
                                       param1=100, param2=3, minRadius=0, maxRadius=0)

            if circles is not None:
                circles = np.uint16(np.around(circles))
                (x, y, r) = circles[0][0]
                center = (x, y)
                # circle center
                cv2.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = r
                cv2.circle(src, center, radius, (255, 0, 255), 3)

            cv2.imshow("detected circles", src)
            cv2.waitKey(0)


    def get_loch(self):

        ret, img = self.cap.read()
        ret, img = self.cap.read()
        ret, img = self.cap.read() # das erste bild ist irgendwie immer das latzte

        height, width, channels = img.shape
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 500,
                                   param1=100, param2=30, minRadius=0, maxRadius=0)

        circles = np.uint16(np.around(circles))

        xm = int(width / 2)
        ym = int(height / 2)

        #for i in circles[0, :]:
        (x, y, r) = circles[0][0]
        # draw the outer circle
        cv2.circle(cimg, (x, y), r, (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (x, y), 2, (0, 0, 255), 3)
        rel_x = (x-xm)/self.ratio  # -1 wenn Kordinatensystem des Bildes anders liegt als das vom Tisch und xy tauschen
        rel_y = (y-ym) / self.ratio * (-1)

        cv2.putText(cimg, "rel_x = {:.3f} rel_y = {:.3f}".format(rel_x,rel_y), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

        cv2.destroyAllWindows()
        cv2.imshow('detected circles', cimg)
        cv2.waitKey(0)
        #cv2.destroyAllWindows()

        return rel_x, rel_y

    def manuel_einrichten(self):
        durchmesser = 3

        #cap = cv2.VideoCapture(1)

        while (True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame

            height, width, channels = frame.shape
            lineThickness = 1
            x1 = int(width / 2)
            y1 = 0
            x2 = x1
            y2 = height
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), lineThickness)
            x1 = 0
            y1 = int(height / 2)
            x2 = width
            y2 = y1
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), lineThickness)

            cv2.circle(frame, (int(width / 2), int(height / 2)), int(durchmesser * self.ratio), (0, 0, 255), lineThickness)

            frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cv2.destroyAllWindows()

def Manual_Kamera_einrichten():
    cam=Kamera(1)
    cam.manuel_einrichten()

def test_get_loch():
    cam = Kamera(1)
    cam.get_loch()
    cv2.waitKey(0)

def circel_test():
    cam = Kamera(1)
    cam.HoughCircles()

if __name__ == '__main__':
    test_get_loch()