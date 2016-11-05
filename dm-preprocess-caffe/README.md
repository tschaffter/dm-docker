# dm-preprocess-caffe
Splits the Challenge training set into a training and validation sets in a format that can be used directly by the deep learning framework [Caffe](http://caffe.berkeleyvision.org/).

Here, the Challenge training set is split into an effective training set (train) and validation set (val). The size of the effective training set can be specified in `generate_train_val_sets.py` (default: 70% of the input data). Half of the subjects included in the train set are cancer positive subjects (idem for the val set).

The LMDB is generated using a modified version of the tool provided by Caffe, `convert_imageset`. The argument `--rmi` enables to remove an image file that has just beed added to the database. Specifying `--rmi` is required to generate LMDB file when the disk space avaiable is not enough to host two copies of the dataset (the image files and the LMDB).

## Input
Please refer to the Wiki of the [Digital Mammography DREAM Challenge](https://www.synapse.org/#!Synapse:syn4224222) for additional information about the inputs listed below.

- /trainingData: directory that contains the DICOM images (.dcm)
- /metadata/exams\_metadata.tsv
- /metadata/images\_crosswalk.tsv

## Output
- /preprocessedData/metadata/exams_metadata_train.tsv
- /preprocessedData/metadata/exams_metadata_val.tsv
- /preprocessedData/metadata/images_crosswalk_train.tsv
- /preprocessedData/metadata/images_crosswalk_val.tsv
- /preprocessedData/metadata/image_labels_train.txt
- /preprocessedData/metadata/image_labels_val.txt
- /preprocessedData/lmdb/train: training set
- /preprocessedData/lmdb/val: validation set
- /preprocessedData/mean_train.binaryproto: mean image for background substraction

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)  
Shivanthan Yohanandan (syohan@au1.ibm.com)

Please direct your questions to the Discussion forum of the DM Challenge.
