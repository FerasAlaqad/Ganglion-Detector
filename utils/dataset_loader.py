# utils/dataset_loader.py
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
from utils.transformations import load_transformations
import yaml

def load_dataset(config_path, train=True):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    if train:
        config = config['train_config']
        train_dir = config['train_dir']
        test_dir = config['test_dir']
        batch_size = config['batch_size']
        transformations, transformations_jitter = load_transformations(config_path, train=True)
        train_ds = datasets.ImageFolder(train_dir, transform=transformations_jitter)
        test_ds = datasets.ImageFolder(test_dir, transform=transformations)
        train_loader = DataLoader(dataset=train_ds, batch_size=batch_size, shuffle=True)
        test_loader = DataLoader(dataset=test_ds, batch_size=batch_size, shuffle=True)
        
        return train_loader , test_loader

    else:
        config = config['evaluation_parameters']

        data_dir = config['test_dir']
        batch_size = config['batch_size']

        transformations = load_transformations(config_path, train)

        dataset = datasets.ImageFolder(data_dir, transform=transformations)

        data_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=train)

        return data_loader