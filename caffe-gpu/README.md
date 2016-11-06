# caffe-gpu
## Overview
This Docker image has the deep learning framework [Caffe](http://caffe.berkeleyvision.org/) installed and has access to available NVIDIA GPUs.

## Build your own Docker image
Create a Dockerfile with the following content.

```
FROM tschaffter/caffe-gpu

# Insert below the instructions to install your inference method.
```

Then build your Docker image.

```
# docker build -t <name> .
```
where `<name>` is the name that you want to give to the image.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the Discussion forum of the DM Challenge.
