import sys
import os
from tqdm.notebook import tqdm   
import torch   
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms    
from torch.utils.data import DataLoader
import torchvision
import argparse
import yaml
from utils.transformations import load_transformations
from utils.dataset_loader import load_dataset
from utils.create_model import create_model
from utils.train_utils import train_epoch, evaluate_epoch, save_model
from utils.transformations import load_transformations
from utils.dataset_loader import load_dataset
from utils.create_model import create_model
from datetime import datetime



def main(config_path, device):

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    config= config['train_config']
    train_loader, test_loader = load_dataset(config_path, train=True)
    model, criterion, optimizer = create_model(config)

    current_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    save_path = os.path.join(config['save_dir'], current_datetime )
    os.makedirs(save_path, exist_ok=True)

    for epoch in range(config['epochs']):
        
        train_loss, train_accuracy = train_epoch(model, train_loader, criterion, optimizer, device)

        val_loss, val_accuracy, true_labels, predicted_labels = evaluate_epoch(model, test_loader, criterion, device)

        model_path= os.path.join(save_path, f'model_epoch_{epoch}_val_acc_{val_accuracy:.4f}.pth')
        
        save_model(model, model_path)

        output_info = (f"Epoch {epoch + 1}/{config['epochs']} - "
                        f"Train Loss: {train_loss:.4f} - Train Accuracy: {train_accuracy:.4f} - "
                        f"Validation Loss: {val_loss:.4f} - Validation Accuracy: {val_accuracy:.4f}")

        with open(os.path.join(save_path, 'output.txt'), 'a') as output_file:
            output_file.write('\n' + output_info)

    print("Training completed.")



if __name__ == "__main__":

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model_config_path = 'parameters/model_config_train.yaml'
    main(model_config_path , device)



