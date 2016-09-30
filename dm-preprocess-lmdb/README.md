# dm-preprocess-png
## Overview
Generates a Lightning Memory-Mapped Database (LMDB) using all the training images.

Here, The LMDB is generated using a modified version of the tool provided by Caffe, `convert_imageset`. The argument `--rmi` enables to remove an image file that has just beed added to the database. This step is required to generate the database when the disk space avaiable is not enough to host two copies of the dataset (the image files and the LMDB).

This script can also be used to generate a LevelDB instead of LMDB. Simply specify `convert_imageset --backend=leveldb  ...`.

## Authors
Thomas Schaffter (thomas.schaffter@gmail.com)
