# dm-train-caffe
## Overview
Trains an off-the-shelf AlexNet convolution neural network (CNN) using [Caffe](http://caffe.berkeleyvision.org/).

This example train an AlexNet model using the output of the pre-processing Docker image `dm-preprocess-caffe`. The required files to train a GoogLeNet model are also provided. The training is performed on one epoch (40,000 iterations) of the effective training set.

## Input
- the output of the pre-processing Docker image `dm-preprocess-caffe`

## Output
- /modelState/train_googlenet_iter40000.caffemodel

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contacts
Shivanthan Yohanandan (shivy.yohanandan@gmail.com)   
Umar Asif (umarasif@au1.ibm.com)   
Antonio Jose Jimeno Yepes (antonio.jimeno@au1.ibm.com)   

Please direct your questions to the Discussion forum of the DM Challenge.
