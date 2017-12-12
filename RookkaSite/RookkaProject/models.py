
from django.db import models
import mwparserfromhell


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

    def __init__(self, title, text, id):
        self.title = title
        self.text = self.cleanText(str(text))
        self.id = id
        self.url = "http://fi.wikipedia.org/?curid=" + self.id

    def cleanText(self, text):
        #clean the text from wikitext to plain text
        parsed_wikicode = mwparserfromhell.parse(text)
        returnable_string = str(parsed_wikicode.strip_code())
        #do more cleaning to the returnable_string!
        return returnable_string