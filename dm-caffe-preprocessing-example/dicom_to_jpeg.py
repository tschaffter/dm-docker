#!/usr/bin/env

# Raw DICOM images are located in /trainingData (read-only)
# Converted JPEGs are output to /preprocessedData/data

import dicom
import os
import numpy as np
from scipy.misc import imsave
from scipy.misc import bytescale
import shutil
from skimage.transform import resize

DICOM_PATH = '/trainingData/'
JPEG_PATH = '/preprocessedData/data/'
LABELS_FILE = '/preprocessedData/labels/labels.txt'

# Helper functions

def dcm_to_jpg(dcm_file, jpg_file):
	"""
	This function converts DICOM to JPEG and resizes to 227x227
	"""
	IM_SIZE = 227
	ds = dicom.read_file(dcm_file)
        a1 = ds.pixel_array
        im = resize(a1, (IM_SIZE, IM_SIZE))
        im = bytescale(im)
	imsave(jpg_file, im)

# Main function

print('Converting DICOM data to JPEGs...')
with open(LABELS_FILE) as f:
    content_labels = f.readlines()
    for i in range(0,len(content_labels)):
        nm = content_labels[i] 
        nm2 = nm[:-1]
        nm = nm[:-8]
        dcm_file = DICOM_PATH + nm + '.dcm'
	jpg_file = JPEG_PATH + nm + '.jpeg'
	try:
        	dcm_to_jpg(dcm_file, jpg_file)
	except: pass
        print('Image...' + nm + '.jpeg       ...Done.')

