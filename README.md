Digital Mammography DREAM Challenge Caffe Example Docker Container Images
===================
This repository contains example **preprocessing** and **training** Docker container images for a basic Caffe AlexNet model. It also includes a short tutorial on how to build and submit these images to the Synapse cloud.


----------
[TOC]


----------


## Docker Image Contents ##
#### Preprocessing Container Image
The preprocessing Docker container image contains the following files:

 - **Dockerfile**: a special script which instructs the host machine what base image (e.g. Ubuntu installation) and dependencies need to be installed, and how to combine all the files within the folder into a Docker image.
 - **bashrc**: you put commands here to set up the shell for use in your particular (Docker container) environment, or to customize things to your preferences. A common thing to put in .bashrc are aliases that you want to always be available.
 - **caffe-ld-so.conf**: specifies the location for `/opt/caffe/.build_release/lib`
 - **create_lmdb.sh**: a shell script for creating the training and validation LMDB files (using image data and ground-truth labels) that are used to train and validate your Caffe model.
 - **create_mean_image.sh**: a shell script for creating the mean image file (created using your input image data) that is used by your Caffe model.
 - **dicom_to_jpeg.py**: a Python script that converts batches of DICOM images to JPEGs
 - **generate_label_files.py**: a Python script that generates ground-truth labels (1s and 0s) from the metadata and crosswalk files, which are available in `/metadata` when your container is run on the host machine. The output file is `labels.txt`.
 - **generate_labels.py**: a Python script that partitions the `labels.txt` file into `train.txt` and `val.txt` for training and validation, respectively. These two files are used, together with the image data, to create your training and validation LMDB files.
 - **preprocess.sh**: a script file and entry point (once the host runs your container it will look for this file and execute it) that runs the preprocessing routine you have defined. ***Please examine this file carefully since it specifies which volumes are mounted and how to access the challenge data.***

#### Training Container Image
The training Docker container image contains the following files:

 - **Dockerfile**: see above
 - **bashrc**: see above
 - **caffe-ld-so.conf**: see above
 - **deploy.prototxt**: CNN network definition that Caffe uses to test your trained model. Visit the [Caffe homepage](http://caffe.berkeleyvision.org/) for more information.
 - **solver.prototxt**: a configuration file used to tell Caffe how you want the network trained and to set your model's hyperparameters. Visit the [Caffe homepage](http://caffe.berkeleyvision.org/) for more information.
 - **train.sh**: a shell script the starts the training process. ***Please examine this file carefully since it specifies which volumes are mounted and how to access the challenge data.***
 - **train_val.prototxt**: your model's network definition. Visit the [Caffe homepage](http://caffe.berkeleyvision.org/) for more information.

----------

Building the Docker Container Images
-------------

This is intended to be a quick guide to build and submit your Docker container images. For a more comprehensive tutorial on how to do this, please visit [Submitting Models](https://www.synapse.org/#!Synapse:syn4224222/wiki/401759) on Synapse.

 1. Create two separate local folders (e.g. `~/preprocessing` and `~/training`)
 2. Place all your **preprocessing** files (should be similar to the contents describes above) inside `~/preprocessing` (use `git clone` if the files already reside on a GitHub repository)
 3. Place all your **training** files (should be similar to the contents describes above) inside `~/training` (use `git clone` if the files already reside on a GitHub repository)
 4. Create a project in Synapse, noting the Synapse ID (e.g. `syn123456`).
 5. On a machine having the docker tools installed, run the following commands:

> `cd ~/preprocessing`

> `docker build -t docker.synapse.org/syn123456/preprocessing .`

> `cd ~/training`

> `docker build -t docker.synapse.org/syn123456/training .` # Replace ‘syn123456' with your own project Id

> `docker login docker.synapse.org` # You will be prompted for your Synapse user name and password

> `docker push docker.synapse.org/syn123456/preprocessing`

> `docker push docker.synapse.org/syn123456/training`

You now have Docker container images in Synapse to use in the challenge. To learn more about Docker, including how to install the necessary tools on your machine, see [https://docs.docker.com](https://docs.docker.com). We provide 'dockerized' models in various frameworks along with links to source code [here](https://www.synapse.org/#!Synapse:syn4224222/docker/).

----------

Submitting the Docker Container Images
-------------

For a more comprehensive tutorial on how to do this, please visit [Submitting Models](https://www.synapse.org/#!Synapse:syn4224222/wiki/401759) on Synapse.

Once your preprocessing and training images are pushed to Synapse, create a file (e.g. `submission`) of this form:

> `preprocessing=docker.synapse.org/syn5644795/preprocessing@sha256:da27f973e4a85ceb59d8d79f3a50ef6a804ab2d3c00a5c1d26ec9e7893a2241f`
> `training=docker.synapse.org/syn5644795/training@sha256:da27f973e4a85ceb59d8d79f3a50ef6a804ab2d3c00a5c1d26ec9e7893a2241f`

Note there are two rows, one specifying the processing image and the other specifying the training image. If there is no separate preprocessing phase, then the first line may be omitted. Note that the image digest (sha256:...) is required. This ensures that the submission refers to a specific version of your Docker repository, which you are then free to update while your submission is processed.

To get the digest of your Docker repository visit the Docker tab of your project, click on the repository of interest, and select the digest at the right hand side. (Note that Docker allows multiple tags for a repository. If you use this feature you must select the digest for the chosen tag.)

While you are on the page, click “Share” and share your repository with the service account “dmchallengeit”. ***This step is required to allow the execution pipeline to access your repository***.

Click on the Files tab and click “Upload or Link to File”. Select the file (e.g. `submission`) you’ve prepared and upload it.

Now submit to the challenge as described earlier. Note that in this case you are not submitting a Docker image but rather the file referencing the two images.

That's all there's to it. If you get stuck, you can refer to the more comprehensive tutorial [here](https://www.synapse.org/#!Synapse:syn4224222/wiki/401759). If you're still stuck, you can post a message on the discussion forum.
