"""
Generates a labels file at the image level.

Args:
   examsMetadataFilename: the filename of the exams metadata file
   imagesCrosswalkFilename: the filename of the images crosswalk file
   labelsFilename: where the labels file will be saved

The space-separated labels file saved includes two columns: 1) the column 
"filename" from the images crosswalk file without the extension and 2) for 
each image, the label is set to 1 if the image features a breast that has 
been diagnosed with cancer (confirmed with tissue diagnosis) within 12 months 
of the given screening mammography exam (see Challenge Questions), otherwise 0.

Author: Thomas Schaffter (thomas.schaff...@gmail.com)
Last update: 2016-11-02
"""

import numpy as np
import pandas as pd
import sys
import os

def generateImageLabels(images, metadata):
	"""
	Generates the cancer label for every image listed in the images
	crosswalk table using cancerL and cancerR from the exams metadata table.

	Args:
	    images: images crosswalk table
	    metadata: exams metadata table
	Returns:
	    a table with the columns image 'filename' and 'cancer'.
	"""
	metadata['examId'] = metadata.subjectId+("_")+metadata.examIndex.astype(str)
        images['examId'] = images.subjectId+("_")+images.examIndex.astype(str)
        examIdsCancerL = metadata.examId[metadata.cancerL == 1]
        examIdsCancerR = metadata.examId[metadata.cancerR == 1]
        images['cancer'] = 0
        images.loc[(images.examId.isin(examIdsCancerL)) & (images.laterality == "L"), 'cancer'] = 1
        images.loc[(images.examId.isin(examIdsCancerR)) & (images.laterality == "R"), 'cancer'] = 1
	
	return images[['filename', 'cancer']].copy()


if __name__ == '__main__':
        examsMetadataFilename = sys.argv[1]
	imagesCrosswalkFilename = sys.argv[2]
	labelsFilename = sys.argv[3]

	# Read the label from the exams metadata
	fields = ['subjectId', 'examIndex', 'cancerL', 'cancerR']
	metadata = pd.read_csv(examsMetadataFilename, sep="\t", na_values='.',usecols=fields)

	# Read the data from the images crosswalk file
	fields = ['subjectId', 'examIndex', 'filename', 'laterality']
	images = pd.read_csv(imagesCrosswalkFilename, sep="\t", na_values='.', usecols=fields)

	# Convert subjectId to string
	metadata.subjectId = metadata.subjectId.astype(str)
	images.subjectId = images.subjectId.astype(str)

	labels = generateImageLabels(images, metadata)
	#labels['key'] = labels.filename.str.replace('.dcm', '')
	#labels.loc[:,'filename'] = labels.filename.str.replace('.dcm', '.png')
	#labels.loc[:,'filename'] = labels.filename.str.replace('.dcm', '')

	# Export the labels to file
	directory = os.path.dirname(labelsFilename)
	if not os.path.isdir(directory):
		os.makedirs(directory)
	labels.to_csv(labelsFilename, sep=' ', index=False, header=False)
