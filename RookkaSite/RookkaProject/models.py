
from django.db import models


class Result(models.Model):
    query_text = ''
    result_texts = []

    def setQueryText(self, query_text):
        query_text = self.query_text

    def addToResult(self, article):
        self.result_texts.append(article)

    def clearResult(self):
        self.result_texts.clear()



class Article(models.Model):
    result = models.ForeignKey(Result)

    def __init__(self, title, text, id): #,time):
        self.title = title
        self.text = text
        self.id = id
        self.url = "http://fi.wikipedia.org/?curid=" + self.id
        #self.time = time