from django.shortcuts import render
import re
from django.http import HttpResponse
from urllib.request import urlopen

from .models import Result, Article
from .forms import QueryForm

def index(request):
    result = Result()
    if request.GET.get('query') is not None:
        query_text = request.GET.get('query')
        result.setQueryText(query_text)
        query(query_text, result)
    article_list = result.result_texts[:5]
    context = {'article_list': article_list}
    return render(request, 'RookkaProject/index.html', context)


def query(query_text,result):
    #here give query text to solr and return cleaned list of articles
    result.clearResult()
    contact_solr(query_text, result)
    return result

def clean_query(query_text):
    #here clean input from user, if has unaccepted characters, reject.
    if re.match('^\w+$',query_text):
        return True
    return False

def form_article(document, result):
    #here insert the query results to the Result object and article objects
    article = Article(document['title'], document['text'])
    result.addToResult(document)
    return

def process_query(query_text):
    """
    Turns the query words to a form that solr can understand.
    Words are searched both in the text and in the title, and
    the resulting query is formed like (text:(A AND B AND C)
    OR title:(A OR B OR C)).
    """
    words = query_text.split()
    if len(words) == 1:
        return "(text:" + words[0] + "%20OR%20title:" + words[0] + ")"
    else:
        #(text:(juusto AND pitsa) OR title:(juusto OR pitsa))
        returned = "(text:("
        for word in words[:len(words)-1]:
            returned = returned + word + " AND "
        returned += words[len(words)-1] + ") OR title:("
        for word in words[:len(words)-1]:
            returned = returned + word + " OR "
        returned = returned + words[len(words)-1] + "))"
        return returned

    # multiple word queries don't work yet!!!!!


def contact_solr(query_text, result):
    url_start = "http://localhost:8983/solr/fiwiki/select?q="
    url_middle = process_query(query_text)
    url_end = "&wt=python"

    url = url_start + url_middle + url_end

    connection = urlopen(url)
    response = eval(connection.read())

    for document in response['response']['docs']:
    #use the function form_article to, well, form an Article object
        form_article(document, result)

    return