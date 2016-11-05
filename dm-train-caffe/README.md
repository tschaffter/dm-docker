# dm-train-caffe
Trains an off-the-shelf AlexNet convolution neural network (CNN) using [Caffe](http://caffe.berkeleyvision.org/).

This example train an AlexNet model using the output of the pre-processing Docker image `dm-preprocess-caffe`. The required files to train a GoogLeNet model are also provided. The training is performed on one epoch (40,000 iterations) of the effective training set.

## Input
- the output of the pre-processing Docker image `dm-preprocess-caffe`

## Output
- /modelState/train_googlenet_iter40000.caffemodel

## Contacts
Shivanthan Yohanandan (shivy.yohanandan@gmail.com)   
Umar Asif (umarasif@au1.ibm.com)   
Antonio Jose Jimeno Yepes (antonio.jimeno@au1.ibm.com)   

Please direct your questions to the Discussion forum of the DM Challenge.
