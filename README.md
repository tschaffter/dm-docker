# Docker template images for the Digital Mammography (DM) DREAM Challenge
## Overview
This repository contains the Dockerfiles required to build the example images provided for the [Digital Mammography DREAM Challenge](https://www.synapse.org/#!Synapse:syn4224222/). 

## Docker images
### Frameworks
- [x] caffe-gpu ([Repository](https://hub.docker.com/r/tschaffter/caffe-gpu/), [Website](http://caffe.berkeleyvision.org/))
- [x] tensorflow-gpu ([Repository](https://hub.docker.com/r/tschaffter/tensorflow-gpu/), [Website](https://www.tensorflow.org/))
- [x] theano-gp ([Repository](https://hub.docker.com/r/tschaffter/theano-gpu/), [Website](http://deeplearning.net/software/theano/))
- [x] keras-gpu ([Repository](https://hub.docker.com/r/tschaffter/keras-gpu/), [Website](https://keras.io/))
- [x] matlab-runtime-gpu ([Repository](https://hub.docker.com/r/tschaffter/matlab-runtime-gpu/), [Website](https://www.mathworks.com/products/compiler/mcr/))

### Pre-processing
- [x] dm-preprocess-png: resizes and converts the images to PNG ([Repository](https://www.synapse.org/#!Synapse:syn7497584))
- [x] dm-preprocess-lmdb: resizes and saves the images to a Lightning Memory-mapped Database ([Repository](https://www.synapse.org/#!Synapse:syn7498267))
- [x] dm-preprocess-caffe: prepares the data before training a Caffe model ([Repository](https://www.synapse.org/#!Synapse:syn7498325))

### Training
- [x] dm-train-caffe: trains an AlexNet or GoogLeNet model using Caffe ([Repository](https://www.synapse.org/#!Synapse:syn7498338))
- [ ] dm-train-tensorflow
- [ ] dm-train-keras

## Set Environment Variables
TODO: Add description on how to set environment variables (e.g. RANDOM_SEED)
