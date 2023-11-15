#here we will test the model
import digit_identify as di

#take input an image and identify the digit in it
img_path = input('Enter the path of the image: ')

#identify the digit

#find the dot product of the input image with each digit data (3 line per digit in csv file)
#and store the dot product in a list
dot_products = di.dot_prod_list(img_path)

print('The digit is: ', di.identify_digit(dot_products))



