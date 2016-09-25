#!/usr/bin/env

#################################################################################
# This script generates labels.tsv from the metadata and crosswalk files.	#
# Ground truth labels (1=cancer, 0=no cancer) are breast level labels.          #
# Author:       syohan@au1.ibm.com                                              #
# Last updated: 25SEP16                                                         #
#################################################################################

import csv

CROSSWALK_FILE = '/metadata/images_crosswalk.tsv'
METADATA_FILE = '/metadata/exams_metadata.tsv'
LABELS_FILE = '/preprocessedData/labels/labels.tsv'
SPLIT_DELIMITER = '\t'
metadata_ht = {}

print 'Generating labels.tsv...'
# load metadata_ht
with open(METADATA_FILE, 'rb') as metadata_f:
    reader = csv.DictReader(metadata_f, delimiter = SPLIT_DELIMITER)
    for row in reader:
        keyL = row['subjectId'] + '_' + \
               row['examIndex'] + '_L'
        keyR = row['subjectId'] + '_' + \
               row['examIndex'] + '_R'
        if keyL not in metadata_ht:
            metadata_ht[keyL] = row['cancerL']
        if keyR not in metadata_ht:
            metadata_ht[keyR] = row['cancerR']

# generate labels
with open(CROSSWALK_FILE, 'rb') as crosswalk_f, \
     open(LABELS_FILE, 'wb') as labels_f:
    reader = csv.DictReader(crosswalk_f, delimiter = SPLIT_DELIMITER)
    writer = csv.writer(labels_f, delimiter = SPLIT_DELIMITER)
    for row in reader:
        key = row['subjectId'] + '_' + \
              row['examIndex'] + '_' + \
              row['laterality']
        label = metadata_ht[key]
        writer.writerow((row['filename'], label))

print 'labels.tsv generated.'
    
