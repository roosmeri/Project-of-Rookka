from urllib.request import urlopen

def process_query(query):
    """
    Turns the query words to a form that solr can understand.
    Words are searched both in the text and in the title, and
    the resulting query is formed like (text:(A AND B AND C)
    OR title:(A OR B OR C)).
    """
    words = query.split()
    if len(words) == 1:
        return "(text:" + words[0] + "%20OR%20title:" + words[0] + ")"
    else:
        #(text:(juusto AND pitsa) OR title:(juusto OR pitsa))
        returned = "(text:("
        for word in words[:len(words)-1]:
            returned = returned + word + "%20AND%20"
        returned += words[len(words)-1] + ")%20OR%20title:("
        for word in words[:len(words)-1]:
            returned = returned + word + "%20OR%20"
        returned = returned + words[len(words)-1] + "))"
        return returned

query = "pitsa"

url_start = "http://localhost:8983/solr/finwiki/select?q="
url_middle = process_query(query)
url_end = "&wt=python"

url = url_start + url_middle + url_end
print(url)

connection = urlopen(url)
response = eval(connection.read())

print(response['response']['numFound'], "documents found.")

# Print the name of each document (for some reason prints only 10 names).

for document in response['response']['docs']:
  print("Title =", document['title'])
