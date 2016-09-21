########################################
########## START DEPENDENCIES ##########
########################################

FROM tleyden5iwx/ubuntu-cuda

ENV PYTHONPATH /opt/caffe/python

# Add caffe binaries to path
#
ENV PATH $PATH:/opt/caffe/.build_release/tools

# Get dependencies
RUN apt-get update && apt-get install -y \
  bc \
  cmake \
  curl \
  gcc-4.6 \
  g++-4.6 \
  gcc-4.6-multilib \
  g++-4.6-multilib \
  gfortran \
  git \
  libprotobuf-dev \
  libleveldb-dev \
  libsnappy-dev \
  libopencv-dev \
  libboost-all-dev \
  libhdf5-serial-dev \
  liblmdb-dev \
  libjpeg62 \
  libfreeimage-dev \
  libatlas-base-dev \
  pkgconf \
  protobuf-compiler \
  python-dev \
  python-pip \
  unzip \
  wget
# Use gcc 4.6
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.6 30 && \
  update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.6 30 && \
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 30 && \
  update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.6 30

# Allow it to find CUDA libs
#RUN echo "/usr/local/cuda/lib64" > /etc/ld.so.conf.d/cuda.conf && \
RUN echo "/usr/lib/x86_64-linux-gnu" > /etc/ld.so.conf.d/cuda.conf && \
  ldconfig

RUN echo "nameserver 208.67.222.222" >/etc/resolv.conf

RUN apt-get install automake 1.14 -y

# Clone the Caffe repo
RUN cd /opt && git clone https://github.com/BVLC/caffe.git
# Glog
#RUN cd /opt && wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz && \
RUN cd /opt && wget http://pkgs.fedoraproject.org/lookaside/pkgs/glog/glog-0.3.3.tar.gz/a6fd2c22f8996846e34c763422717c18/glog-0.3.3.tar.gz && \
#RUN cd /opt && git clone https://github.com/google/glog glog && \
  tar zxvf glog-0.3.3.tar.gz && \
  cd /opt/glog-0.3.3 && \
  ./configure && \
  make && \
  make install
# Workaround for error loading libglog:
#   error while loading shared libraries: libglog.so.0: cannot open shared object file
# The system already has /usr/local/lib listed in /etc/ld.so.conf.d/libc.conf, so
# running `ldconfig` fixes the problem (which is simpler than using $LD_LIBRARY_PATH)
# TODO: looks like this needs to be run _every_ time a new docker instance is run,
#        so maybe LD_LIBRARY_PATh is a better approach (or add call to ldconfig in ~/.bashrc)
RUN ldconfig

# Gflags
RUN cd /opt && \
  wget https://github.com/schuhschuh/gflags/archive/master.zip && \
  unzip master.zip && \
  cd /opt/gflags-master && \
  mkdir build && \
  cd /opt/gflags-master/build && \
  export CXXFLAGS="-fPIC" && \
  cmake .. && \
  make VERBOSE=1 && \
  make && \
  make install
# Build Caffe core
RUN cd /opt/caffe && \
  cp Makefile.config.example Makefile.config && \
   \
echo "CXX := /usr/bin/g++-4.6" >> Makefile.config && \
sed -i 's/CXX :=/CXX ?=/' Makefile && \
make all
# Add ld-so.conf so it can find libcaffe.so
ADD caffe-ld-so.conf /etc/ld.so.conf.d/
# Run ldconfig again (not sure if needed)
RUN ldconfig
# Install python deps
RUN cd /opt/caffe && \
  cat python/requirements.txt | xargs -L 1 sudo pip install
# Numpy include path hack - github.com/BVLC/caffe/wiki/Ubuntu-14.04-VirtualBox-VM
RUN ln -s /usr/include/python2.7/ /usr/local/include/python2.7 && \
  ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy/ /usr/local/include/python2.7/numpy
# Build Caffe python bindings
RUN cd /opt/caffe && make pycaffe

# Check how to test caffe - RUN make test
RUN pip install pydicom
RUN apt-get build-dep -y python-matplotlib
RUN pip install synapseclient
RUN pip install lmdb
RUN apt-get install python-opencv
# needed to avoid issues with cv2
RUN ln /dev/null /dev/raw1394
RUN pip install sklearn

######################################
########## END DEPENDENCIES ##########
######################################

#################################################
########## START PREPROCESSING ROUTINE ##########
#################################################

# The following volumes are mounted when the preprocessing container is run:
# - /trainingData (read-only)
# - /metadata (read-only)
# - /preprocessedData (writable)
# furthermore, /metadata contains the following files:
# - /metadata/exams_metadata.tsv
# - /metadata/images_crosswalk.tsv
# - /metadata/subjects_metadata.tsv
# NOTE: The format and content matches that of the pilot metadata

# Copy files

RUN echo "Copying files..."
COPY dicom_to_jpeg.py /dicom_to_jpeg.py
COPY generate_labels.py /generate_labels.py
COPY generate_label_files.py /generate_label_files.py
COPY create_lmdb.sh /create_lmdb.sh
COPY create_mean_image.sh /create_mean_image.sh
COPY preprocess.sh /preprocess.sh
COPY bashrc /.bashrc
COPY caffe-ld-so.conf /caffe-ld-so.conf
RUN echo "Files copied."

# Set permissions so server can execute within Docker container

RUN echo "Setting file permissions..."
RUN chmod 777 /dicom_to_jpeg.py
RUN chmod 777 /generate_labels.py
RUN chmod 777 /generate_label_files.py
RUN chmod 777 /create_lmdb.sh
RUN chmod 777 /create_mean_image.sh
RUN chmod 777 /preprocess.sh
RUN chmod 777 /.bashrc
RUN chmod 777 /caffe-ld-so.conf
RUN echo "File permissions set."

