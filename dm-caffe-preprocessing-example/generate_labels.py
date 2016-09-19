#!/usr/bin/env

#################################################################################
# This script generates labels.txt from the metadata and crosswalk files	#
#################################################################################

import csv
import os
import numpy as np

LABELS_PATH = '/preprocessedData/labels/'
IMAGES_CROSSWALK = '/metadata/images_crosswalk.tsv'
EXAMS_METADATA = '/metadata/exams_metadata.tsv'

print("Creating labels.txt...")

labels_file = open(LABELS_PATH + 'labels.txt', 'w')
images = open(IMAGES_CROSSWALK, 'rb')
images = csv.reader(images, delimiter = '\t') 
p_ids = []    
filenames = []    
for line in images:
    if line[0] == 'patientId':
        continue
    else:
        p_ids.append(int(line[0]))
        filename = line[4]
        filenames.append(filename[:-7])
p_ids1 = []
labels = []
exams = open(EXAMS_METADATA, 'rb')
exams = csv.reader(exams, delimiter = '\t')
for line in exams:
    if line[0] == 'patientId':
        continue # ignore the headers
    else:
        p_ids1.append(int(line[0]))
        label = int(line[3]) or int(line[4])
        labels.append(int(label))
 
for i in range(0, len(p_ids)):
    p_id = p_ids[i]    
    filename = filenames[i]        
    indices = [j for j, x in enumerate(p_ids1) if x == p_id]
    label = [labels[k] for k in indices]
    if np.sum(label) > 0:
        lbl = '1'
    else:
        lbl = '0'
    item = filename + '.jpeg\t' + lbl
    labels_file.write('%s\n' % item)
labels_file.close() 
print("labels.txt generated.")   

