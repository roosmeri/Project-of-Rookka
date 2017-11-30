
from django.db import models


class Query(models.Model):
    query_text = models.CharField(max_length=200) #queryObject for solr

    def __str__(self):
        return self.name


class Result(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    result_texts = [] #a collection of articles from solr


    def __str__(self):
        return self.name


class Article(models.Model):
    result = models.ForeignKey(Result)
    article_wantedinfo = "" #what is wanted from the article JSON?


    def __str__(self):
        return self.article_wantedinfo