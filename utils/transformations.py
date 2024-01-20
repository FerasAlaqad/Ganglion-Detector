import torchvision.transforms as transforms
import yaml

def load_transformations(config_path, train=True):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    if train:
        config_1 = config['train_config']['transformations']
    
        transformations = transforms.Compose([
        transforms.Resize(config_1['resize']),
        transforms.ToTensor(),
        transforms.Normalize(mean=config_1['normalize_mean'], std=config_1['normalize_std'])
        ])

        config_2 = config['train_config']['transformations_jitter']
        transformations_jitter =  transforms.Compose([
            transforms.Resize(config_2['resize']),
            transforms.RandomHorizontalFlip() if config_2['random_horizontal_flip'] else transforms.RandomHorizontalFlip(0),
            transforms.RandomVerticalFlip() if config_2['random_vertical_flip'] else transforms.RandomVerticalFlip(0),
            transforms.RandomRotation(degrees=config_2['random_rotation']),
            transforms.ColorJitter(brightness=config_2['color_jitter']['brightness'],
                                    contrast=config_2['color_jitter']['contrast'],
                                    saturation=config_2['color_jitter']['saturation'],
                                    hue=config_2['color_jitter']['hue']),
            transforms.RandomCrop(size=config_2['random_crop']['size'], padding=config_2['random_crop']['padding']),
            transforms.ToTensor() if config_2['to_tensor'] else transforms.ToTensor(),
            transforms.Normalize(mean=config_2['normalize_mean'], std=config_2['normalize_std'])
        ])

        return transformations , transformations_jitter

        
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