# How Neighborhood Exploration influences Novelty and Diversity in Graph Collaborative Filtering

This is the official implementation of the paper _How Neighborhood Exploration influences Novelty and Diversity in Graph Collaborative Filtering_, accepted as short paper at MORS@RecSys2022.

This repository is heavily dependent on the framework **Elliot**, so we suggest you refer to the official GitHub [page](https://github.com/sisinflab/elliot) and [documentation](https://elliot.readthedocs.io/en/latest/).

All graph models are implemented in `PyTorch Geometric` using the version `1.10.2`, with CUDA `10.2` and cuDNN `8.0`.

### Installation guidelines: scenario #1
If you have the possibility to install CUDA on your workstation (i.e., `10.2`), you may create the virtual environment with the requirements files we included in the repository, as follows:

```
# PYTORCH ENVIRONMENT (CUDA 10.2, cuDNN 8.0)

$ python3 -m venv venv_pt
$ source venv_pt/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements_pt.txt
$ pip install torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric -f https://data.pyg.org/whl/torch-1.10.0+cu102.html
```

### Installation guidelines: scenario #2
A more convenient way of running experiments is to instantiate a docker container having CUDA `10.2` already installed.

Make sure you have Docker and NVIDIA Container Toolkit installed on your machine (you may refer to this [guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)).

Then, you may use the following Docker image to instantiate the container equipped with CUDA `10.2`:

Container Docker with CUDA `10.2` and cuDNN `8.0` (the environment for `PyTorch`): [link](https://hub.docker.com/layers/nvidia/cuda/10.2-cudnn8-devel-ubuntu18.04/images/sha256-3d1aefa978b106e8cbe50743bba8c4ddadacf13fe3165dd67a35e4d904f3aabe?context=explore)

After the setup of your Docker containers, you may follow the exact same guidelines as scenario #1.

### Datasets
At `./data/` you may find all tsv files for the datasets, i.e., training, validation, and test sets. 

### Training and testing models
To train and evaluate models an all considered metrics, you may run the following command:

```
$ python -u start_experiments.py --model <model-name> --dataset <dataset-name>
```

where `<model-name>` and `<dataset-name>` refer to the name of the model to be run and the dataset on which to run the experiment, respectively.

You may find all configutation files at `./config_files/<model-name>/<dataset-name>.yml`, where all hyperparameter spaces and the exploration strategies are reported.

**[IMPORTANT]** for graph models with explicit message-passing, you may refer to configuration files contained in the folder pattern `./config_files/<layer-n>/<dataset-name>.yml`, where `n` is the number of explored hops. In this way, you will run all graph models with exploration at `n` hops. Conversely, models without explicit message-passing follow the usual notation as explained above.

Results about calculated metrics are available in the folder `./results/<dataset-name>/performance/`. Specifically, you need to access the tsv file having the following name pattern: `rec_cutoff_<cutoff>_relthreshold_0_<datetime-experiment-end>.tsv`.
