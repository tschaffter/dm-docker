# dm-preprocess-png
## Overview
Generates a Lightning Memory-Mapped Database (LMDB) that includes all the training images.

Here, the LMDB is generated using a modified version of the tool provided by Caffe, `convert_imageset`. The argument `--rmi` enables to remove an image file that has just beed added to the database. Specifying `--rmi` is required to generate LMDB file when the disk space avaiable is not enough to host two copies of the dataset (the image files and the LMDB).

This script can also be used to generate a LevelDB instead of LMDB. Simply specify `convert_imageset --backend=leveldb  ...`.

## Input
Please refer to the Wiki of the [Digital Mammography DREAM Challenge](https://www.synapse.org/#!Synapse:syn4224222) for additional information about the inputs listed below.

- /trainingData: directory that contains the DICOM images (.dcm)
- /metadata/exams\_metadata.tsv
- /metadata/images\_crosswalk.tsv

## Output
- /preprocessedData/metadata/image_labels.txt
- /preprocessedData/lmdb/mylmdb: the LMDB file

## License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contacts
Thomas Schaffter (thomas.schaffter@gmail.com)

Please direct your questions to the Discussion forum of the DM Challenge.
