# Parallelized-Background-Subtraction
Parallelized background subtraction for videos written in python using mpi4py numpy and cv2.


# Output
### Input Frame
![Input Example](https://user-images.githubusercontent.com/24472871/71265157-4decb080-234e-11ea-9fbc-91c65d3331c4.jpg)

### Output Image
![Output Example](https://user-images.githubusercontent.com/24472871/71265168-547b2800-234e-11ea-99cc-a5a1ce33b14e.jpg)


### How it works
The way it does the background subtraction is it uses median filtering technique to find the median in every frame.
median filtering can be expensive so we parallelized it to be faster and efficient.

Compared to other approaches mean filtering or frame subtraction this gives the best results

To parallelize this approach we split the image into "n" parts and process each part indvidualy, then we collect the result from each part and put them together to form the background image.

### How to use it

1) put your images in the Images folder and run the renaming.sh file (make sure to run it once as it will overwrite images in the second run)

2) pip3 install -r requirements.txt to install the dependcies

3) in the constants.py modify the value to the number of images you have

4) mpiexec -n "number of nodes" python3 main.py
