# TensorFlow Models

This repository was forked from the original [tensorflow/models](https://github.com/tensorflow/models) so that we can make various research models pip-installable and pin their versions.

Each model that we want to support is on a different branch that includes a version tag (e.g. `deeplab-0.0.1`). Whenever we want to pull in upstream changes to a model, those changes should be pulled into a new branch with the version tag incremented.

Making a model pip-installable is just a matter of adding a `setup.py` file into its corresponding directory. See `research/deeplab/setup.py` and `research/object_detection/setup.py` for examples. A model's `setup.py` should only be added to its corresponding branch(es) in order to prevent accidentally installing a model from the wrong branch.

Once a valid `setup.py` exists, the model can be installed using the following syntax (using deeplab as an example):
```
pip install git+https://github.com/autognc/models@deeplab-0.0.1#egg=deeplab&subdirectory=research/deeplab
```
This syntax will also work as a dependency in `requirements.txt` or `environment.yml` files.
