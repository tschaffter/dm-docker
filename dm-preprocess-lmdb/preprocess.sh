# Generates a Lightning Memory-Mapped Database (LMDB).
#
# Tasks:
# - resize the images (saved in PNG format)
# - generate the image labels
# - generate the LMDB file
#
# Here, The LMDB is generated using a modified version of the tool 
# provided by Caffe, convert_imageset. The argument "--rmi" can
# be used to remove an image file that has just beed added to
# the database. This step is required to generate the DB when
# the disk space avaiable is not enough to how two copies of
# the dataset (the image files and the LMDB).
#
# This script can also be used to generate a LevelDB instead
# of LMDB. Simply specify "convert_imageset --backend=leveldb 
# ...".
#
# Author: Thomas Schaffter (thomas.schaff...@gmail.com)
# Last update: 2016-09-27
#!/bin/bash

IMAGES_DIRECTORY="/trainingData"
EXAMS_METADATA_FILENAME="/metadata/exams_metadata.tsv"
IMAGES_CROSSWALK_FILENAME="/metadata/images_crosswalk.tsv"

PREPROCESS_DIRECTORY="/preprocessedData"
PREPROCESS_IMAGES_DIRECTORY="$PREPROCESS_DIRECTORY/images"
IMAGE_LABELS_FILENAME="$PREPROCESS_DIRECTORY/metadata/image_labels.txt"
LMDB_FILENAME="$PREPROCESS_DIRECTORY/lmdb/mylmdb"

mkdir -p $PREPROCESS_IMAGES_DIRECTORY
mkdir -p ${LMDB_FILENAME%/*}

echo "Resizing and converting $(find $IMAGES_DIRECTORY -name "*.dcm" | wc -l) DICOM images to PNG format"
find $IMAGES_DIRECTORY/ -name "*.dcm" | parallel --will-cite "convert {} -resize 500x500! $PREPROCESS_IMAGES_DIRECTORY/{/.}.png" # faster than mogrify
echo "PNG images have been successfully saved to $PREPROCESS_IMAGES_DIRECTORY/."

echo "Generating image labels to $IMAGE_LABELS_FILENAME"
python generate_image_labels.py $EXAMS_METADATA_FILENAME $IMAGES_CROSSWALK_FILENAME $IMAGE_LABELS_FILENAME
sed -i 's/.dcm/.png/g' $IMAGE_LABELS_FILENAME

echo "Generating LMDB $LMDB_FILENAME"
convert_imageset --backend=lmdb \
    --shuffle \
    --gray=true \
    --rmi=true \
    $PREPROCESS_IMAGES_DIRECTORY/ \
    $IMAGE_LABELS_FILENAME \
    $LMDB_FILENAME
