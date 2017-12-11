#coding=UTF-8
from django.shortcuts import render
import re
from django.http import HttpResponse
from urllib.request import urlopen
import urllib.parse

from .models import Result, Article
from .forms import QueryForm

def index(request):
    if request.GET.get('query') is not None:
        result = Result()
        query_text = request.GET.get('query')
        if query_text and check_query(query_text):
            result.setQueryText(query_text)
            result = query(query_text, result)
            article_list = result.result_texts[:10]
            context = {'article_list': article_list}
            return render(request, 'RookkaProject/index.html', context)
    article_list = []
    context = {'article_list': article_list}
    return render(request, 'RookkaProject/index.html', context)


def query(query_text,result):
    #here give query text to solr and return cleaned list of articles
    result.clearResult()
    contact_solr(query_text, result)
    return result

def check_query(query_text):
    #here check if input has unaccepted characters
    if re.match(r'\w+', query_text):
        return True
    return False

def form_article(document, result, highlighting):
    #here insert the query results to the Result object and article objects

    article = Article(document['title'], highlighting, document['id'])
    #article.cleanText()
    result.addToResult(article)
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
        for word in words[:len(words) - 1]:
            returned = returned + word + "%20AND%20"
        returned += words[len(words) - 1] + ")%20OR%20title:("
        for word in words[:len(words) - 1]:
            returned = returned + word + "%20OR%20"
        returned = returned + words[len(words) - 1] + "))"
        return returned


def contact_solr(query_text, result):
    url_start = "http://localhost:8983/solr/fiwiki/select?hl.fl=text&hl=on&q="
    url_middle = process_query(query_text)
    #below in the comment a first try to fix the scandic character problem - does not work!
    #url_middle = urllib.parse.quote(url_middle)
    url_end = "&wt=python"

    url = url_start + url_middle + url_end

    connection = urlopen(url)
    response = eval(connection.read())

    for document in response['response']['docs']:
    #use the function form_article to, well, form an Article object
    #highlightings can be found in response['highlighting'][document['id']]
        highlighting = response['highlighting'][document['id']]
        form_article(document, result, highlighting)

    return