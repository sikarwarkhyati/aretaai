from django.shortcuts import render
from django.http import HttpResponse
from .models import Query
import spacy

nlp = spacy.load("en_core_web_sm")

def query_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        doc = nlp(query)
        # Process the query using spaCy
        # ...
        return render(request, 'result.html', {'result': 'Result'})
    return render(request, 'query.html')

def result_view(request):
    return render(request, 'result.html')