from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from nltk.translate.bleu_score import sentence_bleu

def calculate_classification_metrics(true_labels, predictions):
    accuracy = accuracy_score(true_labels, predictions)
    f1 = f1_score(true_labels, predictions, average='weighted')
    precision = precision_score(true_labels, predictions, average='weighted')
    recall = recall_score(true_labels, predictions, average='weighted')
    return {
        'accuracy': accuracy,
        'f1_score': f1,
        'precision': precision,
        'recall': recall
    }

def calculate_ner_metrics(true_labels, predictions):
    # Implement NER specific metrics if needed, otherwise use classification metrics
    return calculate_classification_metrics(true_labels, predictions)

def calculate_qa_metrics(true_labels, predictions):
    # For QA, we might use different metrics such as exact match and F1 score.
    # Here we use a simple accuracy metric for illustration.
    exact_matches = sum(1 for true, pred in zip(true_labels, predictions) if true == pred)
    accuracy = exact_matches / len(true_labels)
    return {'accuracy': accuracy}

def calculate_summarization_metrics(true_labels, predictions):
    bleu_scores = [sentence_bleu([ref], pred) for ref, pred in zip(true_labels, predictions)]
    average_bleu = sum(bleu_scores) / len(bleu_scores)
    return {'average_bleu_score': average_bleu}
