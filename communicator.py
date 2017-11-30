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
        return "(text:" + words[0] + " OR title:" + words[0] + ")"
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

query = "juusto pitsa kissa"
# multiple word queries don't work yet 

url_start = "http://localhost:8983/solr/finwiki/select?q="
url_middle = process_query(query)
url_end = "&wt=python"

url = url_start + url_middle + url_end

connection = urlopen(url)
response = eval(connection.read())

print(response['response']['numFound'], "documents found.")

# Print the name of each document.

for document in response['response']['docs']:
  print("Title =", document['title'])



##import urllib3, simplejson
##
##http = urllib3.PoolManager()
##response =  http.request('GET','http://localhost:8983/solr/finwiki/select?indent=on&q=juusto&wt=json')
##print(response.status)
##json = simplejson.loads(response.data.decode('utf-8'))
##print(json['response']['numFound'], "documents found.")
##
### Print the fields of each document.
##
##for document in json['response']['docs']:
##    for doc_key in document:
##        print(doc_key, "=", document[doc_key])
