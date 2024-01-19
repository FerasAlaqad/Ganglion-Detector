# utils/load_model.py
import torch.nn as nn
from torchvision import models
import torch
import yaml

def load_model(model_config_path):
    with open(model_config_path, 'r') as file:
        model_config = yaml.safe_load(file)

    model_path = model_config['model_path']
    dropout = model_config['model_parameters']['dropout']
    linear_units = model_config['model_parameters']['linear_units']

    base_model = models.resnet50(pretrained=True)
    base_model.fc = nn.Identity()


    model = nn.Sequential(
        base_model,
        nn.Flatten(),
        nn.Dropout(dropout),
        nn.Linear(linear_units, 2),
        nn.Softmax(dim=1)  
    )

    model.load_state_dict(torch.load(model_path))

    return model
