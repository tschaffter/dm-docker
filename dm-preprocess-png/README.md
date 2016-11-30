# dm-preprocess-png
## Overview
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

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the [Discussion forum of the DM Challenge](https://www.synapse.org/#!Synapse:syn4224222/discussion/default).
