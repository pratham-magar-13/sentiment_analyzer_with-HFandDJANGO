# classifier/apps.py
from django.apps import AppConfig
from transformers import pipeline

class ClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classifier'
    
    # Class variables to hold the model persistently in memory
    classifier_pipeline = None

    def ready(self):
        # This runs once when Django starts
        print("Loading Hugging Face Model...")
        ClassifierConfig.classifier_pipeline = pipeline("sentiment-analysis")
        print("Model loaded successfully!")