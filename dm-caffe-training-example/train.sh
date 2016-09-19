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

export TOOLS=./build/tools
export LOG=/modelState/train.log
export MODEL=/solver.prototxt

$TOOLS/caffe train --solver=$MODEL 2>&1 | tee $LOG &

