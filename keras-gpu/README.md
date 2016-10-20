# keras-gpu
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

```
# docker build -t <name> .
```
where `<name>` is the name that you want to give to the image.

## Switch the backend to Theano
In the Dockerfile, replace `ENV KERAS_BACKEND tensorflow` by `ENV KERAS_BACKEND theano`. After building the image:

```
# nvidia-docker run -it --rm tschaffter/keras-gpu /usr/bin/python -c "from keras import backend; print backend._BACKEND"
Using Theano backend.
Using gpu device 0: Tesla K80 (CNMeM is enabled with initial size: 10.0% of memory, cuDNN 5103)
theano
```

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)
