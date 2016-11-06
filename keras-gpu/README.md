# keras-gpu
## Overview
This Docker image provides the deep learning framework [Keras](https://keras.io/).

Keras is a high-level neural networks library, written in Python and capable of running on top of either [TensorFlow](https://www.tensorflow.org/) or [Theano](http://deeplearning.net/software/theano/). It was developed with a focus on enabling fast experimentation. 

Backends installed:
- TensorFlow (default)
- Theano

## Test the Docker image locally
Here the command [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) must be used instead of `docker run` to give the Docker container access to the GPUs.

```
# nvidia-docker run -it --rm tschaffter/keras-gpu /usr/bin/python -c "from keras import backend; print backend._BACKEND"
Using TensorFlow backend.
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcurand.so locally
tensorflow
```

## Build your own Docker image
Create a Dockerfile with the following content.

```
FROM tschaffter/keras-gpu

# Insert below the instructions to install your inference method.
```

Then build your Docker image.

```
# docker build -t <name> .
```
where `<name>` is the name that you want to give to the image.

## Set the backend to Theano
Here, Tensorflow is used as the default backend for Keras. To set the backend to Theano, add the following line to your Dockerfile.

```
RUN echo '{"epsilon":1e-07,"floatx":"float32","backend":"theano"}' > .keras/keras.json
```

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the Discussion forum of the DM Challenge.
