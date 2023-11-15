import digit_identify as di

#here will will use the above functions to train the model
#we will be taking input of image path and corresponding digit
#we will be adding the image data to csv file


digit = input('Digit: ')
img_path_main = input('Image path:(ideal) ')
di.add_to_csv(img_path_main, digit)
img_path_1 = input('Image path:(variation 1) ')
di.add_to_csv(img_path_1, digit)
img_path_2 = input('Image path:(variation 2) ')
di.add_to_csv(img_path_2, digit)

#Done

