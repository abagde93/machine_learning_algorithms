import numpy
import PIL
from PIL import Image

#To get images from path
from scipy import misc
import glob

#To deal with filepath/filename manipulation, will be useful later
import os.path

#Create array to store individual image matrixes in 
image_array = []


def image2Array(image):
   
    #Get name of image from path
    #name = os.path.basename(image)
    #name_array.append(name)
    #print(name)
    
    #Open image as greyscale
    img = PIL.Image.open(image).convert("L")
    print(img.size)

    #Convert image to numpy array. 
    arr = numpy.array(img)
    print(arr.shape)

    #Append "numpy image" to image_array
    image_array.append(arr)
    print("images in array: %s" % len(image_array))


def reconstructImage(matrix_image,i):
    back_to_image = PIL.Image.fromarray(matrix_image)
    back_to_image.format = "PNG"

    filename = "%d.png" % i
    print(filename)
    back_to_image.save(filename)

def main():
    for image_path in glob.glob("/home/pi/machine_learning_algorithms/Sample011/*.png"):
        
        #Convert image to matrix, and add to image_array
        image2Array(image_path)
    
    #########################################################################################
    # Make indivdual functions for each classifier and use image2Array and reconstructImage #
    # This is simply a proof of concept for a possible modular structure                    #
    #########################################################################################



    for i in range(0,len(image_array)):
        #Convert individual matrixes in image_array back to images, and save accordingly
        reconstructImage(image_array[i],i)

if __name__ == '__main__':
    main()
