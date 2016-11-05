# dm-preprocess-png
Resizes all the training images to the same size and saves them to PNG.

The images are processed using all the CPU cores available using [GNU Parallel](https://www.gnu.org/software/parallel/) and [ImageMagick](http://www.imagemagick.org/script/index.php). Moreover, a label file at the image level is generated using information from the exams metadata table (see `generate_labels.py`).

## Input
Please refer to the Wiki of the [Digital Mammography DREAM Challenge](https://www.synapse.org/#!Synapse:syn4224222) for additional information about the inputs listed below. 

- /trainingData: directory that contains the DICOM images (.dcm)
- /metadata/exams\_metadata.tsv
- /metadata/images\_crosswalk.tsv

## Output
- /preprocessedData/images/*.png
- /preprocessedData/metadata/image_labels.txt

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the Discussion forum of the DM Challenge.
