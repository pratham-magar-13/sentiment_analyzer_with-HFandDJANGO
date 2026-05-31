# classifier/views.py
from django.shortcuts import render
from .apps import ClassifierConfig

def index(request):
    context = {}
    
    if request.method == "POST":
        user_text = request.POST.get("user_text", "")
        
        if user_text:
            # Call our pre-loaded pipeline
            result = ClassifierConfig.classifier_pipeline(user_text)[0]
            
            context = {
                "user_text": user_text,
                "label": result['label'],
                "score": round(result['score'] * 100, 2)
            }
            
    return render(request, "classifier/index.html", context)