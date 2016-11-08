# tensorflow-gpu
## Overview
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
Create a Dockerfile with the following content.

```
FROM tschaffter/tensorflow-gpu

# Insert below the instructions to install your inference method.
```

Then build your Docker image.

```
# docker build -t <name> .
```
where `<name>` is the name that you want to give to the image.

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the Discussion forum of the DM Challenge.
