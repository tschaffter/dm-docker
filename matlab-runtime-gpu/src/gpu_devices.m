function gpu_devices
    for i = 1:gpuDeviceCount
        gpuDevice(i)
    end
end
