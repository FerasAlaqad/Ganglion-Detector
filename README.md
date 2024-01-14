# The Future of Surgical Diagnostics: AI-Enhanced Detection of Ganglion Cells for Hirschsprung Disease 
<img src="images/overview.png" width="800px"/>

### [Paper]() | [Train Dataset](https://portal.gdc.cancer.gov/projects/TCGA-LUAD) |  [Test Datasets](https://portal.gdc.cancer.gov/projects/TCGA-LUSC) | [Pretrained Model](https://www.dropbox.com/sh/x7fvxx1fiohxwb4/AAAObJJTJpIHHi-s2UafrKeea?dl=0) 

### Getting started

- Clone this repo:
```bash
git clone https://github.com/DeepMIALab/AI-FFPE
cd AI-FFPE
```

- Install PyTorch 1.1 and other dependencies (e.g., torchvision, visdom, dominate, gputil).

- For pip users, please type the command `pip install -r requirements.txt`.

- For Conda users,  you can create a new Conda environment using `conda env create -f environment.yml`.


### Training and Test

- The slide identity numbers which were used in train, validation and test sets are given as .txt files in [docs/](https://github.com/DeepMIALab/AI-FFPE/tree/main/docs) for both Brain and Lung dataset. To replicate the results, you may download [GBM](https://portal.gdc.cancer.gov/projects/TCGA-GBM) and [LGG](https://portal.gdc.cancer.gov/projects/TCGA-LGG) projects for Brain, [LUAD](https://portal.gdc.cancer.gov/projects/TCGA-LUAD) and [LUSC](https://portal.gdc.cancer.gov/projects/TCGA-LUSC) projects for Lung from TCGA Data Portal and create a subset using these .txt files.
- To extract the patches from WSIs and create PNG files, please follow the instructions given in [AI-FFPE/Data_preprocess](https://github.com/DeepMIALab/AI-FFPE/tree/main/Data_preprocess) section. 

The data used for training are expected to be organized as follows:
```bash
Data_Path                # DIR_TO_TRAIN_DATASET
 ├──  trainA
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png
 ├──  trainB     
 |      ├── 1.png     
 |      ├── ...
 |      └── m.png
 ├──  valA
 |      ├── 1.png     
 |      ├── ...
 |      └── j.png
 └──  valB     
        ├── 1.png     
        ├── ...
        └── k.png
