from django.shortcuts import render
import re
from django.http import HttpResponse

from .models import Query, Result, Article

def index(request):
    article_list = Result.result_texts[:5]
    context = {'article_list': article_list}
    return render(request, 'RookkaProject/index.html', context)

def query(query_text):
    #here give query text to solr and return cleaned list of articles
    return Result.result_texts

def clean_query(query_text):
    #here clean input from user, if has unaccepted characters, reject.
    if re.match('^\w+$',query_text):
        return True
    return False

def form_result(query_text):
    #here insert the query results to the Result object
    return