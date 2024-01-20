import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models

def create_model(config):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    linear_units = config['linear_units']
    num_classes = config['num_classes']
    dropout = config['dropout']

    base_model = models.resnet50(pretrained=True)
    base_model.fc = nn.Identity()  

    model = nn.Sequential(
        base_model,
        nn.Flatten(),
        nn.Dropout(dropout),
        nn.Linear(linear_units, num_classes),
        nn.Softmax(dim=1)  
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['lr'], weight_decay=config['weight_decay'])

    return model, criterion, optimizer
