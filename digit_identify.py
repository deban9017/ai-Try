#take input an image and identify the digit in it

#to do so, we will be making a list of all the pixels of 28*28 image

from PIL import Image

#function to convert image to list of pixels
    #we would take black and white image
    #each pixel may have illumination value from 0 to 255

def image_to_list(image_path):
    img = Image.open(image_path)
    #given image is 28*28 and black and white, no need to resize or convert to black and white
    pixels = list(img.getdata())
    return pixels

#now we will be giving input of image path and corresponding digit, for training the model
#we will be using a csv file to store the data
# 3 lines per digit 0-9 in csv file

def add_to_csv(image_path, digit):
    #open csv file in append mode
    with open('C:/Users/deban\OneDrive - Indian Institute of Science/coding/Python project demo/ai Try/train_data.csv', 'a') as f:
        #convert image to list of pixels
        pixels = image_to_list(image_path)
        #write the digit and pixels to csv file
        f.write(str(digit) + ',')
        for pixel in pixels:
            f.write(str(pixel) + ',')
        f.write('\n')

#so each pixel value will be treated like a unit vector in 784 dimensional space
#we will be using dot product to find the most similar digit, taking dot product with each digit data with the input image data
#the digit with highest dot product will be the most similar digit
#(the 1st line of data of each digit in csv file will be the ideal digit, and rest two will be of some variation of that digit)

#function to find dot product of two vectors
# 1st vector is the input image vector
# 2nd vector is the ideal digit vector
def dot_product(v1, v2):
    #check if the vectors are of same length
    if len(v1) != len(v2):
        return 0
    #return the dot product
    return sum([i * j for i, j in zip(v1, v2)]) #zip function returns a tuple of corresponding elements of two lists

def dot_prod_list(image_path):
    #convert image to list of pixels
    pixels = image_to_list(image_path)
    #find the dot product of the input image with each digit data (3 line per digit in csv file)
    #and store the dot product in a list
    dot_products = []
    #open csv file in read mode
    with open('C:/Users/deban\OneDrive - Indian Institute of Science/coding/Python project demo/ai Try/train_data.csv', 'r') as f:
        #read the data, except 1st element of each line (which is the digit)
        for line in f.readlines():
            data = line.split(',')[1:]
            #convert data to int
            data = [int(i) for i in data if i != '\n']
            data=normalize(data)
            #find dot product of input image and data
            dot_products.append(dot_product(pixels, data))
    return dot_products

#function to normalize the data
def normalize(data):
    #find magnitude of data
    mag = sum([i**2 for i in data])**0.5
    #divide each element of data by the magnitude
    data = [i/mag for i in data]
    return data

#function to identify the digit by max value of sum of dot products (3 for each digits 0-9)
def identify_digit(dot_product_list):
    #list to store the sum of dot products of each digit
    sum_dot_products = []
    #iterate over the dot product list
    for i in range(0, len(dot_product_list), 3):
        #sum the dot products of 3 lines of each digit
        sum_dot_products.append(sum(dot_product_list[i:i+3]))
    #return the index of the max value of sum of dot products
    return sum_dot_products.index(max(sum_dot_products))

