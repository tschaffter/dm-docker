# dm-preprocess-caffe
## Overview
Splits the Challenge training set into a training and validation sets in a format that can directly be used by the deep learning framework [Caffe](http://caffe.berkeleyvision.org/).

Tasks:
- resize the training images and saves them in PNG format
- split the exams metadata and images crosswalk tables into a training and validation sets (default: 70% of the cancer positive and negative subjects are in the training set)
- generate image labels
- generate train and val LMDB
- generate mean image for background substraction

## Output
- /preprocessedData/metadata/exams_metadata_train.tsv
- /preprocessedData/metadata/exams_metadata_val.tsv
- /preprocessedData/metadata/images_crosswalk_train.tsv
- /preprocessedData/metadata/images_crosswalk_val.tsv
- /preprocessedData/metadata/image_labels_train.txt
- /preprocessedData/metadata/image_labels_val.txt
- /preprocessedData/lmdb/train
- /preprocessedData/lmdb/val
- /preprocessedData/lmdb/train_mean.binaryproto

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)  
Shivanthan Yohanandan (syohan@au1.ibm.com)
