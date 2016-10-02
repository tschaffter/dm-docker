# keras-gpu
## Overview
TODO

```bash
$ nvidia-docker run -it --rm -v /preprocessedData/:/preprocessedData/ -v /metadata/:/metadata/ -v /trainingData/:/trainingData/ -v /modelState/:/modelState/ keras-gpu /usr/bin/python -c "from keras import backend; print backend._BACKEND"
```

## Contacts
