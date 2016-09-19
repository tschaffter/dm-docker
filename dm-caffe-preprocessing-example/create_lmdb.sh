#!/usr/bin/env sh

#################################################
########## Create the dcom lmdb inputs ##########
#################################################

# the following volumes are mounted when the preprocessing container is run:
# - /trainingData (read-only)
# - /metadata (read-only)
# - /preprocessedData (writable)

# training and validation data stored in same folder
export TRAIN_DATA_ROOT=/preprocessedData/data/
export VAL_DATA_ROOT=/preprocessedData/data/

export LABELS=/preprocessedData/labels
export LMDBS=/preprocessedData/lmdbs
export TOOLS=/opt/caffe/.build_release/tools

RESIZE=false

if $RESIZE; then
  RESIZE_HEIGHT=227
  RESIZE_WIDTH=227
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --gray=true \
    $TRAIN_DATA_ROOT \
    $LABELS/train.txt \
    $LMDBS/dcom_train_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --gray=true \
    $VAL_DATA_ROOT \
    $LABELS/val.txt \
    $LMDBS/dcom_val_lmdb

echo "LMDB creation Done."
