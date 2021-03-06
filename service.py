# -*- coding: utf-8 -*-

from xml.dom import minidom
from urllib2 import urlopen
from flask import Flask, make_response
from json import dumps
import unicodedata

urls = {
	'futbol' : "http://elpais.com/tag/rss/futbol/a/", \
	'tecnologia' : "http://ep00.epimg.net/rss/tecnologia/portada.xml" , \
	'cine' : "http://elpais.com/tag/rss/cine/a/", \
	'ciencia' : "http://ep00.epimg.net/rss/elpais/ciencia.xml", 
	'latinoamerica' : "http://elpais.com/tag/rss/latinoamerica/a/",
}

#url = "http://elpais.com/tag/rss/futbol/a/"
#url = "http://ep00.epimg.net/rss/tecnologia/portada.xml"

app = Flask(__name__)



@app.route("/categorias")
def index():
	categorias = ["fútbol", "cine", "tecnología", "ciencia", "latinoamérica"]
	return make_response(dumps(categorias))

@app.route("/news/<news_type>")
def news(news_type):
	hola = get_news(news_type)
	return make_response(dumps(hola, ensure_ascii=False).encode("utf-8"))


def delete_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 
def delete_unicode(s):
	return s.encode("ascii", "ignore")

def get_news(news_type):
	xml = minidom.parse(urlopen(urls[news_type]))
	items = xml.getElementsByTagName('item')	
	
	news = []
	for item in items:
		titles = item.getElementsByTagName('title')
		for title in titles:
			#print (title.childNodes[0].nodeValue).encode("ascii", "ignore")
			#print type(str(title.childNodes[0].nodeValue))
			tildes = title.childNodes[0].nodeValue
			no_tildes = delete_tildes(tildes)
			no_unicode = delete_unicode(no_tildes)
			news.append(no_unicode)
	return news

if __name__ == "__main__":
	app.run()

#print titles


