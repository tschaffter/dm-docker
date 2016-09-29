#!/usr/bin/env sh

###################################################
########## RUN THE PREPROCESSING ROUTINE ##########
###################################################

# Create sub directories

mkdir -p /preprocessedData/data
mkdir -p /preprocessedData/labels
mkdir -p /preprocessedData/lmdbs

# Generate labels.txt (from exams_metadata.tsv and images_crosswalk.tsv)

python generate_labels.py

# Generate train.txt and val.txt (from labels.txt)

python generate_label_files.py

# Convert DICOMs to JPEGs

python dicom_to_jpeg.py

# Generate train_lmdb and test_lmdb

./create_lmdb.sh

# Generate mean_image file

./create_mean_image.sh

