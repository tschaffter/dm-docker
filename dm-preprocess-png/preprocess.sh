# Resizes all the training images to the same size and 
# saves them to PNG format using ImageMagick.
#
# Tasks:
# - resize the images
# - save to PNG format
#
# In addition, a labels file at the images levels is generated
# using information from the exams metadata table (see generate_labels.py).
#
# Author: Thomas Schaffter (thomas.schaff...@gmail.com)
# Last update: 2016-09-27
#!/bin/bash

IMAGES_DIRECTORY="/trainingData"
EXAMS_METADATA_FILENAME="/metadata/exams_metadata.tsv"
IMAGES_CROSSWALK_FILENAME="/metadata/images_crosswalk.tsv"

PREPROCESS_DIRECTORY="/preprocessedData"
PREPROCESS_IMAGES_DIRECTORY="$PREPROCESS_DIRECTORY/images"
IMAGE_LABESL_FILENAME="$PREPROCESS_DIRECTORY/metadata/image_labels.txt"

mkdir -p $PREPROCESS_IMAGES_DIRECTORY

echo "Resizing and converting $(find $IMAGES_DIRECTORY -name "*.dcm" | wc -l) DICOM images to PNG format"
find $IMAGES_DIRECTORY/ -name "*.dcm" | parallel --will-cite "convert {} -resize 500x500! $PREPROCESS_IMAGES_DIRECTORY/{/.}.png" # faster than mogrify
echo "PNG images have been successfully saved to $PREPROCESS_IMAGES_DIRECTORY/."

echo "Generating image labels to $IMAGE_LABESL_FILENAME"
python generate_image_labels.py $EXAMS_METADATA_FILENAME $IMAGES_CROSSWALK_FILENAME $IMAGE_LABESL_FILENAME
