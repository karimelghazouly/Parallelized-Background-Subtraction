import numpy as np
import cv2
from mpi4py import MPI

import dataReaders
import imageProcessor
import constants

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if (rank == constants.DATAREADER_NODE):
    # Data reader node which reads and splits data across image processor nodes
    DataReader = dataReaders.dataReader()
    DataReader.readImages()
    DataReader.splitImages(comm)
    DataReader.waitForFinalImages(comm)


    
else:
    # Image processor nodes repsonsible for median filtering
    ImageProcessor = imageProcessor.imageProcessor()
    ImageProcessor.readAndProcessImages(comm, rank)