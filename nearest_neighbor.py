import numpy
import PIL
from PIL import Image

#To get images from path
from scipy import misc
import glob

#To save images
import webbrowser

#Create array to store individual image arrays in 
image_array = []

#Convert individual images to arrays and store in image_array
for image_path in glob.glob("/home/pi/machine_learning_algorithms/Sample011/*.png"):
   
    #Open image as greyscale
    img = PIL.Image.open(image_path).convert("L")
    print(img.size)

    #Convert image to numpy array. 
    arr = numpy.array(img)
    print(arr.shape)

    #Append "numpy image" to image_array
    image_array.append(arr)
    print("images in array: %s" % len(image_array))

#Take first matrix from image_array, to make sure image is correct
back_to_image = PIL.Image.fromarray(image_array[1])
back_to_image.format = "PNG"

filename = "test_pic.png"
back_to_image.save(filename)
webbrowser.open('back_to_image')



