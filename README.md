# The Future of Surgical Diagnostics: AI-Enhanced Detection of Ganglion Cells for Hirschsprung Disease 
<img src="images/overview.png" width="800px"/>

### [Paper]() | [Train Dataset](https://portal.gdc.cancer.gov/projects/TCGA-LUAD) |  [Test Datasets](https://portal.gdc.cancer.gov/projects/TCGA-LUSC) | [Pretrained Model](https://www.dropbox.com/sh/x7fvxx1fiohxwb4/AAAObJJTJpIHHi-s2UafrKeea?dl=0) 

## Prerequisites
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

### Getting started

- Clone this repo:
```bash
git clone https://github.com/FerasAlaqad/Ganglion-Detector
cd Ganglion-Detector
pip install -r requirements.txt
```


### Training and Test

- The slide identity numbers which were used in train, validation and test sets are given as .txt files in [docs/](https://github.com/DeepMIALab/AI-FFPE/tree/main/docs) for both Brain and Lung dataset. To replicate the results, you may download [GBM](https://portal.gdc.cancer.gov/projects/TCGA-GBM) and [LGG](https://portal.gdc.cancer.gov/projects/TCGA-LGG) projects for Brain, [LUAD](https://portal.gdc.cancer.gov/projects/TCGA-LUAD) and [LUSC](https://portal.gdc.cancer.gov/projects/TCGA-LUSC) projects for Lung from TCGA Data Portal and create a subset using these .txt files.
- To extract the patches from WSIs and create PNG files, please follow the instructions given in [AI-FFPE/Data_preprocess](https://github.com/DeepMIALab/AI-FFPE/tree/main/Data_preprocess) section. 

The data used for training and testing expected to be organized as follows:
```bash
Data_Path                # DIR_TO_TRAIN_DATASET
 ├──  Ege_Hospital_Train
 |   ├── P
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png
 |   ├── n
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png
 ├──  Ege_Hospital_Internal_Test
 |   ├── P
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png
 |   ├── n
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png 
 ├──  Behcet_Hospital_External_Test
 |   ├── P
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png
 |   ├── n
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png 
 ├──  Medipol_Hospital_External_Test
 |   ├── P
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png
 |   ├── n
 |      ├── 1.png     
 |      ├── ...
 |      └── n.png


```


- Train the AI-FFPE model:
```bash
python train.py --dataroot ./datasets/Frozen/${dataroot_train_dir_name} --name ${model_results_dir_name} --CUT_mode CUT --batch_size 1
```

- Test the AI-FFPE  model:
```bash
python test.py --dataroot ./datasets/Frozen/${dataroot_test_dir_name}  --name ${result_dir_name} --CUT_mode CUT --phase test --epoch ${epoch_number} --num_test ${number_of_test_images}
```

The test results will be saved to a html file here: ``` ./results/${result_dir_name}/latest_train/index.html ``` 


