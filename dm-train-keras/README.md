# dm-train-keras
## Overview
Trains an off-the-shelf VGG convolution neural network (CNN) using [Keras](https://keras.io/) and [Theano](http://deeplearning.net/software/theano/) as backend.

## Input
- /trainingData/\*.dcm
- /metadata/images\_crosswalk.tsv

Note that the IT infrastructure of the Digital Mammography DREAM Challenge enable to pre-process the data separatedly from the effective training phase. Pre-processed data are cached and can then be reused for multiple training runs, thus saving the computational time alloted to each team.

For an example on how to separate pre-processing and training, please check out the example [dm-train-caffe](https://github.com/tschaffter/dm-docker/tree/master/dm-train-caffe).

## Output
TODO: Generate prediction file

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contacts
