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
    else:
        config = config['evaluation_parameters']

    data_dir = config['train_dir'] if train else config['test_dir']
    batch_size = config['batch_size']

    transformations = load_transformations(config_path, train)

    dataset = datasets.ImageFolder(data_dir, transform=transformations)

    data_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=train)

    return data_loader