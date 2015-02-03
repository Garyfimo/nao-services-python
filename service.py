from xml.dom import minidom
from urllib2 import urlopen
from flask import Flask, make_response
from json import dumps

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
	categorias = ["futbol", "cine", "tecnologia", "ciencia", "latinoamerica"]
	return make_response(dumps(categorias))

@app.route("/news/<news_type>")
def news(news_type):
	hola = get_news(news_type)
	return make_response(dumps(hola, ensure_ascii=False).encode("utf-8"))


def get_news(news_type):
	xml = minidom.parse(urlopen(urls[news_type]))
	items = xml.getElementsByTagName('item')	
	
	news = []
	for item in items:
		titles = item.getElementsByTagName('title')
		for title in titles:
			print title.childNodes[0].nodeValue				
			news.append(title.childNodes[0].nodeValue)		
	return news

if __name__ == "__main__":
	app.run()

#print titles


