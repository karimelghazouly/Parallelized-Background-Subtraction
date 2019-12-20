import numpy as np
import cv2
import constants



class imageProcessor:

    def readAndProcessImages(self, comm, rank):
        Final_Pixels = np.zeros((constants.BLOCK_HEIGHT_SIZE,constants.BLOCK_WIDTH_SIZE))
        Splitted_Images = comm.recv(source = constants.DATAREADER_NODE)
        for i in range(constants.BLOCK_HEIGHT_SIZE):
            for j in range(constants.BLOCK_WIDTH_SIZE):
                Sorted_Pixels = []
                for Img in Splitted_Images:
                    Sorted_Pixels.append(Img[i,j])

                Sorted_Pixels.sort()
                Final_Pixels[i,j] = (int(Sorted_Pixels[constants.MEDIAN_IDX_1]) + int(Sorted_Pixels[constants.MEDIAN_IDX_2])) / 2

        comm.isend(Final_Pixels, dest = constants.DATAREADER_NODE)
        print("Node with rank = ", rank, "done with it's part.")

