"""
Splits the exams metadata and images crosswalk tables into two sets
(train and val) that include the same proportion of cancer positive
and negative subjects.

Args:i
   examsMetadataFilename: the filename of the exams metadata file
   imagesCrosswalkFilename: the filename of the images crosswalk file
   outputDir: the directory where the files exams_metadata_train.tsv,
       exams_metadata_val.tsv, images_crosswalk_train.tsv and
       images_crosswalk_val.tsv are saved.
   trainSize: the proportion of subjects in the train set (in [0,1])
       while the remaining subjects are included in the val set.
   seed: the random seed

Author: Thomas Schaffter (thomas.schaff...@gmail.com)
Last update: 2016-11-02
"""

import numpy as np
import pandas as pd
import sys
import os
import random

if __name__ == '__main__':
        examsMetadataFilename = sys.argv[1]
	imagesCrosswalkFilename = sys.argv[2]
	outputDir = sys.argv[3]
	trainSize = float(sys.argv[4])
	random.seed(sys.argv[5])

	if trainSize < 0 or trainSize > 1:
		print "trainSize must be in [0,1]."
		sys.exit(1)

	# Pandas converts columns that have missing values to double
	metadata = pd.read_csv(examsMetadataFilename, sep="\t", na_values='.')
	images = pd.read_csv(imagesCrosswalkFilename, sep="\t", na_values='.')

	# Convert subjectId to string
        metadata.subjectId = metadata.subjectId.astype(str)
        images.subjectId = images.subjectId.astype(str)

	# Split the exams metadata and images crosswalk file at the subject level
	subjectIds = set(metadata.subjectId)
	subjectIdsPos = set(metadata.subjectId[(metadata.cancerL == 1) | (metadata.cancerR == 1)])
	subjectIdsNeg = subjectIds.difference(subjectIdsPos)
	subjectIdsPosTrain = set(random.sample(subjectIdsPos, int(trainSize * len(subjectIdsPos))))
	subjectIdsNegTrain = set(random.sample(subjectIdsNeg, int(trainSize * len(subjectIdsNeg))))
	subjectIdsTrain = subjectIdsPosTrain.union(subjectIdsNegTrain)

	# Split the exams metadata and images crosswalk files into
	# training and validation set.
	metadataTrain = metadata.loc[metadata.subjectId.isin(subjectIdsTrain),]
	metadataVal = metadata.loc[~metadata.subjectId.isin(subjectIdsTrain),]
	imagesTrain = images.loc[images.subjectId.isin(subjectIdsTrain),]
	imagesVal = images.loc[~images.subjectId.isin(subjectIdsTrain),]

	# Export the files
	if not os.path.isdir(outputDir):
		os.makedirs(outputDir)
	metadataTrain.to_csv(os.path.join(outputDir, "exams_metadata_train.tsv"), sep="\t", na_rep='.', index=False, header=True)
	metadataVal.to_csv(os.path.join(outputDir, "exams_metadata_val.tsv"), sep="\t", na_rep='.', index=False, header=True)
	imagesTrain.to_csv(os.path.join(outputDir, "images_crosswalk_train.tsv"), sep="\t", na_rep='.', index=False, header=True)
	imagesVal.to_csv(os.path.join(outputDir, "images_crosswalk_val.tsv"), sep="\t", na_rep='.', index=False, header=True)
