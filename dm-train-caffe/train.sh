#!/usr/bin/env sh

##############################################
########## RUN THE TRAINING ROUTINE ##########
##############################################

# /modelState (writable) volume has been mounted
# /preprocessedData (writable) already mounted
# /trainingData (read-only) already mounted
# /metadata (read-only) already mounted

# Train an AlexNet model using preprocessed data (available in /preprocessedData)
# and pipe training output to a log file

LOG=/modelState/train.log
MODEL=/solver_alexnet.prototxt
GPUS="all"

caffe train --solver=$MODEL -gpu $GPUS #2>&1 | tee $LOG &
