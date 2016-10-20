# dm-docker
Add general information and a brief description of each Docker image.

## Docker images
### Base
- [x] caffe-gpu
- [ ] keras-gpu
- [x] tensorflow-gpu
- [x] theano-gp
- [x] matlab-runtime-gpu

### Pre-processing
- [x] dm-preprocess-png
- [x] dm-preprocess-lmdb
- [x] dm-preprocess-caffe

### Training
- [x] dm-train-caffe
- [ ] dm-train-tensorflow
- [ ] dm-train-keras
- [ ] dm-train-theano (optional if we already have Keras)

## TODO
- Find bash/python logging system
- What is the user that executes the script (root? check with .theanorc)
- Use environmental variables
	- RANDOM_SEED
- Update scripts if we are allowed to pass arguments to {preprocess,train,test}.sh via the submission file
