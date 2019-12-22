import numpy as np
import cv2
import constants



class imageProcessor:

    def readAndProcessImages(self, comm, rank):
        
        Splitted_Images = comm.recv(source = constants.DATAREADER_NODE)
        Number_Of_Rows = len(Splitted_Images[0])

        Final_Pixels = np.zeros((Number_Of_Rows,constants.IMAGE_WIDTH))

        for i in range(Number_Of_Rows):
            for j in range(constants.IMAGE_WIDTH):
                Sorted_Pixels = []
                for Img in Splitted_Images:
                    Sorted_Pixels.append(Img[i,j])

                Sorted_Pixels.sort()
                Final_Pixels[i,j] = (int(Sorted_Pixels[constants.MEDIAN_IDX_1]) + int(Sorted_Pixels[constants.MEDIAN_IDX_2])) / 2

        comm.isend(Final_Pixels, dest = constants.DATAREADER_NODE)
        print("Node with rank = ", rank, "done with it's part.")

