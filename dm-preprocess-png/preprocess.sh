# Resizes all the training images to the same size and 
# saves them to PNG format using ImageMagick.
#
# Tasks:
# - resize the images
# - save to PNG format
#
# In addition, a labels file at the images levels is generated
# using information from the exams metadata table (see generate_labels.py)
#
# Author: Thomas Schaffter (thomas.schaff...@gmail.com)
# Last update: 2016-09-27
#!/bin/bash

TRAIN_DIRECTORY="/trainingData"
PP_DIRECTORY="/preprocessedData"
PP_IMAGES_DIRECTORY="$PP_DIRECTORY/images"

mkdir -p $PP_IMAGES_DIRECTORY

echo "Resizing and converting DICOM images to PNG format."
find $TRAIN_DIRECTORY/ -name "*.dcm" | parallel --will-cite "convert {} -resize 500x500! $PP_IMAGES_DIRECTORY/{/.}.png" # faster than mogrify
echo "$(find $PP_IMAGES_DIRECTORY -name "*.png" | wc -l) PNG images have been successfully saved to $PP_IMAGES_DIRECTORY/."
