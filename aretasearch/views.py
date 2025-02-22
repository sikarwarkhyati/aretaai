from django.shortcuts import render
from django.http import HttpResponse
from .models import SearchQuery
import spacy

nlp = spacy.load("en_core_web_sm")

def search_query_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        doc = nlp(query)
        # Process the query using spaCy
        # ...
        return render(request, 'search_result.html', {'result': 'Result'})
    return render(request, 'search_query.html')

def search_result_view(request):
    return render(request, 'search_result.html')
