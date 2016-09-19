#!/usr/bin/env sh

###########################################
########## Create the mean image ##########
###########################################

export LD_LIBRARY_PATH=/usr/local/cuda-6.5/lib64:/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

export LMDBS=/preprocessedData/lmdbs/
export TOOLS=/opt/caffe/.build_release/tools

$TOOLS/compute_image_mean $LMDBS/dcom_train_lmdb $LMDBS/dm_mean.binaryproto
echo "Mean image creation Done".
