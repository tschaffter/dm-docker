import argparse
import csv
import dicom
import gzip
from os import listdir, remove, mkdir
from os.path import isfile, join, isdir
import scipy.misc
from sklearn.cross_validation import train_test_split
import sys
import time
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.constraints import maxnorm
from keras.utils import np_utils
from keras import backend as K
from keras.optimizers import SGD
np.random.seed(1337)  # for reproducibility

def super_print(statement, f):
    """
    This basically prints everything in statement.
    We'll add a new line character for the output file.
    We'll just use print for the output.
    INPUTS:
    - statement: (string) the string to print.
    - f: (opened file) this is the output file object to print to
    """
    sys.stdout.write(statement + '\n')
    sys.stdout.flush()
    f.write(statement + '\n')
    return 0

def create_data_splits(path_csv_crosswalk, path_csv_metadata):
    """
    Goes through data folder and divides train/val.
    INPUTS:
    - path_csv_crosswalk: (string) path to first csv file
    - path_csv_metadata: (string) path to second csv file
    """
    # First, let's map the .dcm.gz file to a (patientID, examIndex, imageView) tuple.
    dict_img_to_patside = {}
    counter = 0
    with open(path_csv_crosswalk, 'r') as file_crosswalk:
        reader_crosswalk = csv.reader(file_crosswalk, delimiter='\t')
        for row in reader_crosswalk:
            if counter == 0:
                counter += 1
                continue
            dict_img_to_patside[row[5].strip()] = (row[0].strip(), row[4].strip())
    # Now, let's map the tuple to cancer or non-cancer.
    dict_tuple_to_cancer = {}
    counter = 0
    with open(path_csv_metadata, 'r') as file_metadata:
        reader_metadata = csv.reader(file_metadata, delimiter='\t')
        for row in reader_metadata:
            if counter == 0:
                counter += 1
                continue
            if row[3] == ".":
                dict_tuple_to_cancer[(row[0].strip(), 'L')] = 0
            else:
                dict_tuple_to_cancer[(row[0].strip(), 'L')] = int(row[3])
            if row[4] == ".":
                dict_tuple_to_cancer[(row[0].strip(), 'R')] = 0
            else:
                dict_tuple_to_cancer[(row[0].strip(), 'R')] = int(row[4])


    # Alright, now, let's connect those dictionaries together...
    X_tot = []
    Y_tot = []
    idx = 0
    for img_name in dict_img_to_patside:
        print idx
        idx = idx + 1
        X_tot.append(img_name)
        Y_tot.append(dict_tuple_to_cancer[dict_img_to_patside[img_name]])
    # Making train/val split and returning.
    X_tr, X_te, Y_tr, Y_te = train_test_split(X_tot, Y_tot, test_size=0.1)
    return X_tr, X_te, Y_tr, Y_te


def read_in_one_image(path_img, name_img, matrix_size, data_aug=False):
    """
    Load dicoms.
    INPUTS:
    - path_img: (string) path to the data
    - name_img: (string) name of the image e.g. '123456.dcm'
    - matrix_size: (int) one dimension of the square image e.g. 224
    """
    filepath_img = join(path_img, name_img)
    dicom_content = dicom.read_file(filepath_img)
    img = dicom_content.pixel_array
    img = scipy.misc.imresize(img, (1, matrix_size, matrix_size), interp='cubic')
    img = img.astype(np.float32)
    img -= np.mean(img)
    img /= np.std(img)
	
    return img	
	
def GenerateDataSet(X_tr, X_te, opts):
    """
    Load Dicom images.
        INPUTS:
        - X_tr: (list of strings) training image names
        - X_te: (list of strings) validation image names
        - opts: parsed argument thing
    """

    X_trainResized = np.empty((len(X_tr), 1, opts.matrix_size, opts.matrix_size))
    X_testResized = np.empty((len(X_te), 1, opts.matrix_size, opts.matrix_size))

    for idxTr,dicomImageTr in enumerate(X_tr):
        X_trainResized[idxTr] = read_in_one_image("trainingData", dicomImageTr, opts.matrix_size, data_aug=False)
        print idxTr

    for idxTe, dicomImageTe in enumerate(X_te):
        X_testResized[idxTe] = read_in_one_image("trainingData", dicomImageTe, opts.matrix_size, data_aug=False)
        print idxTe

    return X_trainResized, X_testResized


def train_net(X_tr, X_te, Y_tr, Y_te, opts,f):
    """
    Training of the net.  All we need is data names and parameters.
    INPUTS:
    - X_tr: (list of strings) training image names
    - X_te: (list of strings) validation image names
    - Y_tr: (list of ints) training labels
    - Y_te: (list of ints) validation labels
    - opts: parsed argument thing
    f: (opened file) for output writing
    """
    # Setting the size and number of channels of input.
    matrix_size = opts.matrix_size

    model = Sequential()
    model.add(ZeroPadding2D((1,1),input_shape=(1,matrix_size,matrix_size)))
    model.add(Convolution2D(64, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(64, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(128, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(256, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Convolution2D(512, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(opts.dropout))
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(opts.dropout))
    model.add(Dense(opts.nClasses, activation='softmax'))
	
    sgd = SGD(lr=opts.lr, decay=opts.decay , momentum=opts.momentum, nesterov=True)
    model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])
    model.fit(X_tr, Y_tr, batch_size=opts.batchSize, nb_epoch=opts.nEpochs, verbose=1, validation_data=(X_te, Y_te))
    score = model.evaluate(X_te, Y_te, verbose=0)

    statement = "Best you could do: " + str(score[1])
    super_print(statement, f)

    model.save(opts.model)
    return 0

def main(args):
    """
    Main Function to do deep learning using tensorflow on pilot.
    INPUTS:
    - args: (list of strings) command line arguments
    """
    # Setting up reading of command line options, storing defaults if not provided.
    pathPrefix = ""
    # Change back to .
    parser = argparse.ArgumentParser(description = "Do deep learning!")
    parser.add_argument("--pf", dest="path_data", type=str, default=pathPrefix + "/trainingData")
    parser.add_argument("--csv1", dest="csv1", type=str, default=pathPrefix + "metadata/images_crosswalk.tsv")
    parser.add_argument("--csv2", dest="csv2", type=str, default=pathPrefix + "metadata/exams_metadata.tsv")
    parser.add_argument("--model", dest="model", type=str, default=pathPrefix + "modelState/model.h5")
    parser.add_argument("--lr", dest="lr", type=float, default=0.001)
    parser.add_argument("--reg", dest="reg", type=float, default=0.00001)
    parser.add_argument("--outtxt", dest="outtxt", type=str, default=pathPrefix + "output/out.txt")
    parser.add_argument("--decay", dest="decay", type=float, default=1.0)
    parser.add_argument("--momentum", dest="momentum", type=float, default=0.9)
    parser.add_argument("--dropout", dest="dropout", type=float, default=0.5)
    parser.add_argument("--ms", dest="matrix_size", type=int, default=224)
    parser.add_argument("--nClasses", dest="nClasses", type=int, default=2)
    parser.add_argument("--batchSize", dest="batchSize", type=int, default=128)
    parser.add_argument("--nEpochs", dest="nEpochs", type=int, default=1)
    parser.add_argument("--out", dest="output", type=str, default=pathPrefix + "modelState/out_train.txt")

    opts = parser.parse_args(args[1:])
    # Setting up the output file.
    if isfile(opts.output):
        remove(opts.output)
    f = open(opts.output, 'w')
    path_csv_crosswalk = opts.csv1
    path_csv_metadata = opts.csv2
    path_csv_test = opts.csv1

    X_train, X_test, y_train, y_test = create_data_splits(path_csv_crosswalk, path_csv_metadata)
    y_train = np.asarray(y_train).reshape(len(y_train),1)
    y_test = np.asarray(y_test).reshape(len(y_test),1)
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)

    X_train,X_test =  GenerateDataSet(X_train, X_test, opts)

    train_net(X_train, X_test, y_train, y_test, opts, f)
    f.close()
    return 0

if __name__ == '__main__':
    main(sys.argv)
	
