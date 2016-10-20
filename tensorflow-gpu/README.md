# tensorflow-gpu
This Docker image provides the deep learning framework [TensorFlow](https://www.tensorflow.org/).

## Test the Docker image locally
Here the command [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) must be used instead of `docker run` to give the Docker container access to the GPUs.

```
# nvidia-docker run -it --rm tschaffter/tensorflow-gpu /usr/bin/python -m tensorflow.models.image.mnist.convolutional
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcurand.so locally
Successfully downloaded train-images-idx3-ubyte.gz 9912422 bytes.
Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes.
Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
Extracting data/train-images-idx3-ubyte.gz
Extracting data/train-labels-idx1-ubyte.gz
Extracting data/t10k-images-idx3-ubyte.gz
Extracting data/t10k-labels-idx1-ubyte.gz
I tensorflow/core/common_runtime/gpu/gpu_device.cc:951] Found device 0 with properties: 
name: Tesla K80
major: 3 minor: 7 memoryClockRate (GHz) 0.8235
pciBusID 0000:83:00.0
Total memory: 11.25GiB
Free memory: 11.13GiB
W tensorflow/stream_executor/cuda/cuda_driver.cc:572] creating context when one is currently active; existing: 0x5102fb0
I tensorflow/core/common_runtime/gpu/gpu_device.cc:951] Found device 1 with properties: 
name: Tesla K80
major: 3 minor: 7 memoryClockRate (GHz) 0.8235
pciBusID 0000:84:00.0
Total memory: 11.25GiB
Free memory: 11.13GiB
...
```

## Build your own Docker image

```
# docker build -t <name> .
```
where `<name>` is the name that you want to give to the image.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)
