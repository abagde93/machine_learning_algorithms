import numpy
import PIL
from PIL import Image

#To get images from path
from scipy import misc
import glob

import matplotlib.pyplot as plt

#Create array to store individual image matrixes in
test_set = []
training_set = []

#Defining labels for training images

label_train = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
               4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
               6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
               7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
               8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
               9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
              

#Defining labels for test images

label_test = [0,1,2,3,4,5,6,7,8,9]

def image2Matrix(image, image_array):


    #Open image as greyscale
    img = PIL.Image.open(image).convert("L")
    #print(img.size)

    #Convert image to numpy array.
    arr = numpy.array(img)
    #print(arr.shape)

    #Append "numpy image" to image_array
    image_array.append(arr)
    #print("images in array: %s" % len(image_array))

def nearest_neighbor(test_image_array, training_image_array, labels, test_set_names):

    
    calculated_labels= []

    for i in range(0, len(test_image_array)):
        print("Processing test image: %s" % test_set_names[i])
        current_test_image = test_image_array[i]
	#print(sum(sum(current_test_image)))
        current = 10000000
        for j in range(0, len(training_image_array)):
            diff = current_test_image - training_image_array[j]
            #print diff
            diff = diff.sum()
            #print(diff)
            if(diff < current):
                current = diff
                index = j
	    

        calculated_labels.append(labels[index])
    #print(calculated_labels)
        #img = training_image_array[index]
        plt.imshow(training_image_array[index])
        plt.show()



def main():

    test_names = []

    for image_path in glob.glob("/home/abagde/machine_learning_algorithms/Test/*.png"):

        #Convert image to matrix, and add to image_array
        image2Matrix(image_path, test_set)
	test_names.append(image_path)
        

    for image_path in glob.glob("/home/abagde/machine_learning_algorithms/TrainingSet/*.png"):

        #Convert image to matrix, and add to image_array
        image2Matrix(image_path, training_set)

    
    nearest_neighbor(test_set, training_set, label_train, test_names)

    #output = label_test(calculated_labels.flatten(1))
    #print(output)
if __name__ == '__main__':
    main()



