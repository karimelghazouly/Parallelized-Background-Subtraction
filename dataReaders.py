import numpy as np
import cv2
import constants
import math

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
        Splitted_Images = [[] for i in range(comm.size - 1)]
        Chunk_Size = math.ceil(constants.IMAGE_HEIGHT / (comm.size - 1))

        for i in range(len(self.Images)):
            BeginRow = 0
            for splitNumber in range(0, comm.size - 1):
                EndRow = min(BeginRow + Chunk_Size , constants.IMAGE_HEIGHT)
                Splitted_Images[splitNumber].append(self.Images[i][BeginRow: EndRow, :])
                BeginRow = EndRow
                
        for i in range(len(Splitted_Images)):
            comm.send(Splitted_Images[i], dest = i+1)

        print("Spliited Images Sent.")

    def waitForFinalImages(self, comm):

        Background = np.zeros((240, 320))
        BeginRow = 0
        for i in range(1, comm.size):
            Recived_Part = comm.recv(source = i)
            EndRow = BeginRow + len(Recived_Part)
            Background[BeginRow:EndRow, :] = Recived_Part
            BeginRow = EndRow


        Background = np.array(Background,  dtype = np.uint8)
        print(Background.shape)
        print(Background)
        cv2.imshow("Background", Background)
        cv2.waitKey(0)