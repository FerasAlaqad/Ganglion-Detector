import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def train_epoch(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0.0
    total_accuracy = 0.0

    for data, label in tqdm(train_loader, desc="Training", leave=False):
        data = data.to(device)
        label = label.to(device)

        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, label)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        total_accuracy += (output.argmax(dim=1) == label).float().mean().item()

    avg_loss = total_loss / len(train_loader)
    avg_accuracy = total_accuracy / len(train_loader)

    return avg_loss, avg_accuracy

def evaluate_epoch(model, test_loader, criterion, device):
    model.eval()
    total_loss = 0.0
    total_accuracy = 0.0
    true_labels = []
    predicted_labels = []

    with torch.no_grad():
        for data, label in tqdm(test_loader, desc="Evaluating", leave=False):
            data = data.to(device)
            label = label.to(device)

            output = model(data)
            loss = criterion(output, label)

            total_loss += loss.item()
            total_accuracy += (output.argmax(dim=1) == label).float().mean().item()

            true_labels.extend(label.cpu().numpy())
            predicted_labels.extend(output.argmax(dim=1).cpu().numpy())

    avg_loss = total_loss / len(test_loader)
    avg_accuracy = total_accuracy / len(test_loader)

    return avg_loss, avg_accuracy, true_labels, predicted_labels

def save_model(model,save_path):
    torch.save(model.state_dict(), save_path)
