# theano-gpu
## Overview
This Docker image provides the deep learning framework [Theano](http://deeplearning.net/software/theano/).

## Test the Docker image locally
To see if your GPU is being used, you can run the following command. Here the command [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) must be used instead of `docker run` to give the Docker container access to the GPUs.

```
# nvidia-docker run -it --rm -e THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 tschaffter/theano-gpu /usr/bin/python ./check1.py
Using gpu device 0: Tesla K80 (CNMeM is enabled with initial size: 10.0% of memory, cuDNN 5103)
[GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>), HostFromGpu(GpuElemwise{exp,no_inplace}.0)]
Looping 1000 times took 0.313817 seconds
Result is [ 1.23178029  1.61879349  1.52278066 ...,  2.20771813  2.29967761
  1.62323296]
Used the gpu
```

The script `check1.py` can run using the CPU instead of the GPU (note the `device=cpu`):

```
# nvidia-docker run -it --rm -e THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 tschaffter/theano-gpu /usr/bin/python ./check1.py
[Elemwise{exp,no_inplace}(<TensorType(float32, vector)>)]
Looping 1000 times took 2.954500 seconds
Result is [ 1.23178029  1.61879337  1.52278066 ...,  2.20771813  2.29967761
  1.62323284]
Used the cpu
```

By default, the Docker image is configured to run using the GPU insteadn of the CPU (see `/root/.theanorc`).

## Build your own Docker image
Create a Dockerfile with the following content.

```
FROM tschaffter/theano-gpu

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
