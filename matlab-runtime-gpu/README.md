# matlab-runtime-gpu
## Overview
This Docker image has Matlab Runtime v9.1 (2016b) installed and has access to available NVIDIA GPUs.

The Matlab Runtime is a standalone set of shared libraries that enables the execution of compiled Matlab applications or components on computers that do not have Matlab installed. To test the installation of Matlab runtime, we compiled an Hello World example using Matlab R2106b Compiler as described [here](Hello World example). To run the standalone application `hello_world` included in this Docker image: 

```
docker run -it tschaffter/matlab-runtime-gpu ./hello_world
```

## Contacts
Thomas Schaffter (thomas.schaff...@gmail.com)
