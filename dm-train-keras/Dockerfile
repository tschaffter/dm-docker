FROM tschaffter/keras-gpu

RUN pip install pillow h5py
RUN pip install -U scikit-learn 

ENV KERAS_BACKEND theano
WORKDIR /root
RUN echo '{"epsilon":1e-07,"floatx":"float32","backend":"'${KERAS_BACKEND}'", "image_dim_ordering": "th"}' > .keras/keras.json

WORKDIR /
COPY KerasExample.py .
COPY train.sh .
RUN chmod a+x train.sh
