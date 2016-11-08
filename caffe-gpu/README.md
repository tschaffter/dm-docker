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

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the Discussion forum of the DM Challenge.
