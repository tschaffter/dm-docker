# tensorflow-gpu

## Test
nvidia-docker run -it --rm -v /preprocessedData/:/preprocessedData/ -v /metadata/:/metadata/ -v /trainingData/:/trainingData/ -v /modelState/:/modelState/ keras-gpu /usr/bin/python -m tensorflow.models.image.mnist.convolutional
