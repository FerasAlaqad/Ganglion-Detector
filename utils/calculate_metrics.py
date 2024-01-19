import os
from datetime import datetime
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def calculate_metrics(true_labels, predicted_labels):
    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)
    accuracy = accuracy_score(true_labels, predicted_labels)
    return precision, recall, f1, accuracy

def save_results(true_labels, predicted_labels, test_dir):
    precision, recall, f1, accuracy = calculate_metrics(true_labels, predicted_labels)

    results_folder = 'results'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_file = os.path.join(results_folder, f"results_{current_time}.txt")

    with open(result_file, 'w') as f:
        f.write(f"Test Directory: {test_dir}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall: {recall:.4f}\n")
        f.write(f"F1 Score: {f1:.4f}\n")
        f.write(f"Accuracy: {accuracy:.4f}\n")

    print(f"Results saved to: {result_file}")
