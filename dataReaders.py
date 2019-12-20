import numpy as np
import cv2
import constants

class dataReader:

    Images = []
    def __init__(self):
        self.Images = []

    def readImages(self):
        end = constants.NUMBER_OF_IMAGES

        for i in range(end):
            Img = cv2.imread("Images/"+ str(i) +".jpg", cv2.IMREAD_GRAYSCALE)
            self.Images.append(Img)

    def splitImages(self, comm):
        Topleft_Images = []
        Topright_Images = []
        Bottomleft_Images = []
        Bottomright_Images = []

        for i in range(len(self.Images)):
            Topleft_Images.append(self.Images[i][:120, :160])
            Topright_Images.append(self.Images[i][:120, 160:])
            Bottomleft_Images.append(self.Images[i][120:, :160])
            Bottomright_Images.append(self.Images[i][120:, 160:])

        print("Split Complete.")
        comm.send(Topleft_Images, dest = constants.TOPLEFT_NODE)
        comm.send(Topright_Images, dest = constants.TOPRIGHT_NODE)
        comm.send(Bottomleft_Images, dest = constants.BOTTOMLEFT_NODE)
        comm.send(Bottomright_Images, dest = constants.BOTTOMRIGHT_NODE)
        print("Spliited Images Sent.")

    def waitForFinalImages(self, comm):
        TopLeft_Final = comm.recv(source = constants.TOPLEFT_NODE)
        TopRight_Final = comm.recv(source = constants.TOPRIGHT_NODE)
        BottomLeft_Final = comm.recv(source = constants.BOTTOMLEFT_NODE)
        BottomRight_Final = comm.recv(source = constants.BOTTOMRIGHT_NODE)
        
        BackgroundTop = np.append(TopLeft_Final, TopRight_Final, axis=1)
        BackgroundBottom = np.append(BottomLeft_Final, BottomRight_Final, axis=1)
        Background = np.append( BackgroundTop, BackgroundBottom, axis=0)

        cv2.imshow("Background", np.array(Background, dtype = np.uint8 ))
        cv2.waitKey(0)