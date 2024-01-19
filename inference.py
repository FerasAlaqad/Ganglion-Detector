import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from utils.load_model import load_model
from utils.transformations import load_transformations
from utils.dataset_loader import load_dataset
from utils.calculate_metrics import calculate_metrics, save_results
import yaml
from datetime import datetime

def inference(model_config_path):
    with open(model_config_path, 'r') as file:
        model_config = yaml.safe_load(file)

    model = load_model(model_config_path)
    model.eval()

    test_loader = load_dataset(model_config_path, train=False)

    predictions = []

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    with torch.no_grad():
        for inputs, _ in test_loader:
            inputs = inputs.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            predictions.extend(predicted.cpu().numpy().tolist())


    true_labels = [label for _, label in test_loader.dataset.samples]
    test_dir = model_config['evaluation_parameters']['test_dir']
    save_results(true_labels, predictions, test_dir)

if __name__ == "__main__":
    model_config_path = 'parameters/model_config_eval.yaml'

    inference(model_config_path)
