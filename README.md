# Project of Rookka
Course LG211 fall 2017, Building NLP Applications

## 

Riikka Raatikainen and Roosa Meriläinen

## How to use

The project is a Django application using Solr. Solr must be running on the fiwiki (Finnish wikipedia) core for the app to work. Also the app uses [mwparserfromhell](https://github.com/earwig/mwparserfromhell) and installing it on one's machine or then commenting out the parts where it is imported or used is necessary. 

One must clone this repo and run the application with the command:

$python3 manage.py runserver 

from the upper RookkaSite directory.
 
Then navigate to http://localhost:8000/RookkaProject/ with one's browser. The site should show an input box and search button. Write your query words to the box and "Try your luck!". The titles and a tiny caption(if found) of the articles that contain the query words in title or text will show on the site.

##

[Class diagram](https://yuml.me/5d159b11.png) (updated)

[Backlog](https://docs.google.com/spreadsheets/d/1yEiY5XAZVYa8lysPCjB2HH348Lml4YFK3AXYPf9ejOQ/edit?usp=sharing)

