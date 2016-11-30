FROM tschaffter/keras-gpu

RUN pip install pillow h5py
RUN pip install -U scikit-learn 

WORKDIR /
COPY KerasExample.py .
COPY train.sh .

RUN chmod a+x train.sh
