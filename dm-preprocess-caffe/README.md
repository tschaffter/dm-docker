# dm-preprocess-caffe
## Overview
Splits the Challenge training set into a training and validation sets in a format that can directly be used by the deep learning framework [Caffe](http://caffe.berkeleyvision.org/).

Tasks:
- resize the training images and saves them in PNG format
- split the exams metadata and images crosswalk tables into a training and validation sets (default: 70% of the cancer positive and negative subjects are in the training set)
- generate image labels
- generate train and val LMDB
- generate mean image for background substraction

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)
Shivanthan Yohanandan (syohan@au1.ibm.com)
