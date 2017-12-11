
from django.db import models
#import mwparserfromhell


class Result(models.Model):
    query_text = ''
    result_texts = []

    def setQueryText(self, query_text):
        self.query_text = query_text

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

    #def cleanText(self):
        #clean the text from wikitext to plain text
        #parsed_wikicode = mwparserfromhell.parse(self.text)
        #self.text = str(parsed_wikicode.strip_code())