from transformers import pipeline

class ModelService:
    def __init__(self):
        self.models = {
            'bert_base': pipeline('text-classification', model='nlptown/bert-base-multilingual-uncased-sentiment'),
            'roberta_base': pipeline('text-classification', model='cardiffnlp/twitter-roberta-base-sentiment'),
            'distilbert_base': pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english'),
            'albert_base': pipeline('text-classification', model='textattack/albert-base-v2-yelp-polarity'),
            'xlnet_base': pipeline('text-classification', model='xlnet-base-cased'),
            'bert_qa': pipeline('question-answering', model='bert-large-uncased-whole-word-masking-finetuned-squad'),
            't5_small': pipeline('summarization', model='t5-small'),
            't5_base': pipeline('summarization', model='t5-base')
        }

    def classify_text(self, text):
        results = {}
        for model_name, model in self.models.items():
            if 'text-classification' in model.task:
                results[model_name] = model(text)
        return results

    def ner(self, text):
        results = {}
        for model_name, model in self.models.items():
            if 'ner' in model.task:
                results[model_name] = model(text)
        return results

    def answer_question(self, question):
        results = {}
        for model_name, model in self.models.items():
            if 'question-answering' in model.task:
                results[model_name] = model(question)
        return results

    def summarize_text(self, text):
        results = {}
        for model_name, model in self.models.items():
            if 'summarization' in model.task:
                results[model_name] = model(text)
        return results

model_service = ModelService()
