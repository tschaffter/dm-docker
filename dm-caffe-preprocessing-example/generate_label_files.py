#!/usr/bin/env

#################################################################################
# This script generates train.txt and val.txt from labels.txt			#
# Partition the data into train and validation sets. Equal number of images are	#
# are used from both the positive and negative images.				#
#################################################################################

import random

LABELS_FILE = '/preprocessedData/labels/labels.txt'
TRAIN_LABELS_FILE = '/preprocessedData/labels/train.txt'
VAL_LABELS_FILE = '/preprocessedData/labels/val.txt'

print("Generating Train/Val data...")
pos = []
neg = []
with open(LABELS_FILE) as f:
    content_labels = f.readlines()   
    for i in range(0,len(content_labels)):
        nm = content_labels[i]
        nm = nm[:-1]
        label = int(nm[-1:])   
        if label == 1:
            pos.append(nm)
        else:
            neg.append(nm)    

random.shuffle(pos)
random.shuffle(neg)

neg_train = neg[:len(neg)-int(round(len(neg)/4))]
neg_test = neg[len(neg)-int(round(len(neg)/4)):]

pos_train = pos[:len(pos)-int(round(len(pos)/4))]
pos_test = pos[len(pos)-int(round(len(pos)/4)):]

train_file = open(TRAIN_LABELS_FILE, 'w')

for item in neg_train:
  train_file.write("%s\n" % item)

for item in pos_train:
  train_file.write("%s\n" % item)

train_file.close()

val_file = open(VAL_LABELS_FILE, 'w')

for item in neg_test:
  val_file.write("%s\n" % item)

for item in pos_test:
  val_file.write("%s\n" % item)

val_file.close()

print("Train/Val data generated.")
