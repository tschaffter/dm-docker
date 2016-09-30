# Splits the Challenge training set into a training and
# validation sets in a format that can directly be used
# by the deep learning framework Caffe.
#
# Tasks:
# - resize the training images and saves them in PNG format
# - split the exams metadata and images crosswalk tables into
#   a training and validation sets (70% of the cancer positive
#   and negative subjects are in the training set)
# - generate image labels
# - generate train and val LMDB
# - generate mean image for background substraction
#
# Author: Thomas Schaffter (thomas.schaff...@gmail.com)
# Last update: 2016-09-29
#!/bin/bash

IMAGES_DIRECTORY="/trainingData"
EXAMS_METADATA_FILENAME="/metadata/exams_metadata.tsv"
IMAGES_CROSSWALK_FILENAME="/metadata/images_crosswalk.tsv"
RAND_SEED=123456

PREPROCESS_DIRECTORY="/preprocessedData"
PREPROCESS_IMAGES_DIRECTORY="$PREPROCESS_DIRECTORY/images"
PREPROCESS_METADATA_DIRECTORY="$PREPROCESS_DIRECTORY/metadata"
LMDB_DIRECTORY="$PREPROCESS_DIRECTORY/lmdb"
TRAIN_SIZE=0.7

mkdir -p $PREPROCESS_IMAGES_DIRECTORY
mkdir -p $PREPROCESS_METADATA_DIRECTORY
mkdir -p $LMDB_DIRECTORY

echo "Resizing and converting $(find $IMAGES_DIRECTORY -name "*.dcm" | wc -l) DICOM images to PNG format"
find $IMAGES_DIRECTORY/ -name "*.dcm" | parallel --will-cite "convert {} -resize 500x500! $PREPROCESS_IMAGES_DIRECTORY/{/.}.png" # faster than mogrify
echo "PNG images have been successfully saved to $PREPROCESS_IMAGES_DIRECTORY/."

echo "Splitting the challenge training set into training and validation sets"
python generate_train_val_sets.py $EXAMS_METADATA_FILENAME \
	$IMAGES_CROSSWALK_FILENAME \
	$PREPROCESS_METADATA_DIRECTORY \
	$TRAIN_SIZE \
	$RAND_SEED

echo "Generating image labels for train"
python generate_image_labels.py $PREPROCESS_METADATA_DIRECTORY/exams_metadata_train.tsv \
	$PREPROCESS_METADATA_DIRECTORY/images_crosswalk_train.tsv \
	$PREPROCESS_METADATA_DIRECTORY/image_labels_train.txt
echo "Generating image labels for val"
python generate_image_labels.py $PREPROCESS_METADATA_DIRECTORY/exams_metadata_val.tsv \
        $PREPROCESS_METADATA_DIRECTORY/images_crosswalk_val.tsv \
        $PREPROCESS_METADATA_DIRECTORY/image_labels_val.txt
sed -i 's/.dcm/.png/g' $PREPROCESS_METADATA_DIRECTORY/image_labels_train.txt
sed -i 's/.dcm/.png/g' $PREPROCESS_METADATA_DIRECTORY/image_labels_val.txt

echo "Generating LMDB train"
convert_imageset --backend=lmdb \
    --shuffle \
    --gray=true \
    --rmi=true \
    $PREPROCESS_IMAGES_DIRECTORY/ \
    $PREPROCESS_METADATA_DIRECTORY/image_labels_train.txt \
    $LMDB_DIRECTORY/train
echo "Generating LMDB val"
convert_imageset --backend=lmdb \
    --shuffle \
    --gray=true \
    --rmi=true \
    $PREPROCESS_IMAGES_DIRECTORY/ \
    $PREPROCESS_METADATA_DIRECTORY/image_labels_val.txt \
    $LMDB_DIRECTORY/val

echo "Generating mean image for backgroud substraction"
compute_image_mean $LMDB_DIRECTORY/train $LMDB_DIRECTORY/mean_train.binaryproto
