from django.test import TestCase

from RookkaProject.models import Article, Result
from RookkaProject import views

class TestResult(TestCase):

    def test_query_word_in_article_list(self):
        result = Result()
        query_text = "juusto"
        result.setQueryText(query_text)
        result = views.query(query_text, result)
        article_list = result.result_texts[:10]

        for article in article_list:
            self.assertIn(query_text, (article.text.lower() or article.title.lower()))
            #query word should appear in the returned article's text or title

    def test_multiple_query_words_in_article_list(self):
        result = Result()
        query_text = "avara luonto"
        result.setQueryText(query_text)
        result = views.query(query_text, result)
        article_list = result.result_texts[:10]

        for article in article_list:
            count = 0
            for word in query_text.split():
                if word in article.text.lower() or article.title.lower():
                    count += 1
            self.assertGreaterEqual(count, 1)
            #at least one query word must appear in the returned article's text or title

