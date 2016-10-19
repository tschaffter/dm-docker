# matlab-runtime-gpu
## Overview
This Docker image has Matlab Runtime v9.1 (2016b) installed and has access to available NVIDIA GPUs.

The Matlab Runtime is a standalone set of shared libraries that enables the execution of compiled Matlab applications or components on computers that do not have Matlab installed. To test the installation of Matlab runtime, we compiled an Hello World example using Matlab R2106b Compiler as described [here](https://support.opensciencegrid.org/support/solutions/articles/5000660751-basics-of-compiled-matlab-applications-hello-world-example). To run the standalone application `hello_world` included in this Docker image: 

```
# docker run -it tschaffter/matlab-runtime-gpu ./hello_world

=============
Hello, World!
=============
```

The example Hello World doesn't require access to the GPU and so `docker run` can be used to run it. This Docker image includes a second application that prints the output of the Matlab command [gpuDevice](https://www.mathworks.com/help/distcomp/gpudevice.html) on each GPU detected. Here the command [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) must be used instead of `docker run` to give the Docker container access to the GPUs.

```
# nvidia-docker run -it --rm tschaffter/matlab-runtime-gpu ./gpu_devices

ans = 

  CUDADevice with properties:

                      Name: 'Tesla K80'
                     Index: 1
         ComputeCapability: '3.7'
            SupportsDouble: 1
             DriverVersion: 7.5000
            ToolkitVersion: 7.5000
        MaxThreadsPerBlock: 1024
          MaxShmemPerBlock: 49152
        MaxThreadBlockSize: [1024 1024 64]
               MaxGridSize: [2.1475e+09 65535 65535]
                 SIMDWidth: 32
               TotalMemory: 1.2079e+10
           AvailableMemory: 1.1884e+10
       MultiprocessorCount: 13
              ClockRateKHz: 823500
               ComputeMode: 'Default'
      GPUOverlapsTransfers: 1
    KernelExecutionTimeout: 0
          CanMapHostMemory: 1
           DeviceSupported: 1
            DeviceSelected: 1


ans = 

  CUDADevice with properties:

                      Name: 'Tesla K80'
                     Index: 2
         ComputeCapability: '3.7'
            SupportsDouble: 1
             DriverVersion: 7.5000
            ToolkitVersion: 7.5000
        MaxThreadsPerBlock: 1024
          MaxShmemPerBlock: 49152
        MaxThreadBlockSize: [1024 1024 64]
               MaxGridSize: [2.1475e+09 65535 65535]
                 SIMDWidth: 32
               TotalMemory: 1.2079e+10
           AvailableMemory: 1.1884e+10
       MultiprocessorCount: 13
              ClockRateKHz: 823500
               ComputeMode: 'Default'
      GPUOverlapsTransfers: 1
    KernelExecutionTimeout: 0
          CanMapHostMemory: 1
           DeviceSupported: 1
            DeviceSelected: 1

...
```

## Build your own Docker image

```
# docker build -t <name> .
```
where `<name>` is the name that you want to give to the image.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)
