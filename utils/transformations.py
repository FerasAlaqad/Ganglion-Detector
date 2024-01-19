import torchvision.transforms as transforms
import yaml

def load_transformations(config_path, train=True):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    if train:
        config = config['train_config']
    else:
        config = config['evaluation_config']

    resize_height = config['input_size']['height']
    resize_width = config['input_size']['width']
    normalization_mean = config['normalization_mean']
    normalization_std = config['normalization_std']

    transformations = transforms.Compose([
        transforms.Resize((resize_height, resize_width)),
        transforms.ToTensor(),
        transforms.Normalize(mean=normalization_mean, std=normalization_std)
    ])

    return transformations
