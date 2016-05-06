from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import os.path
import urllib2

class myContentHandler(ContentHandler):

    # Guarda en un fichero html la lista de los titulares de las noticias
    # donde cada titulo es un link a su respectiva noticia
    # USAGE: ./xml-parser-barrapunto.py barrapunto.rss

    title = ""
    link = ""

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.linesHTML = []
        self.linesDic = {}

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                # To avoid Unicode trouble
                self.title = self.theContent.encode('utf-8')
                print self.title
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.link = self.theContent.encode('utf-8')
                print self.link
                newline = '<li><a href="'+ self.link + '">' + self.title + '</a></li>' + '\n'
                self.linesHTML.append(newline)
                self.linesDic[self.title] = self.link
                self.inContent = False
                self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


def obtenerFich():
    if os.path.exists("barrapunto/bp.html"):
        fichHTML = open("barrapunto/bp.html", "w")
    else:
        fichHTML = open("barrapunto/bp.html", "a")
    # Load parser and driver
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    # Ready, set, go!
    xmlFile = urllib2.urlopen('http://barrapunto.com/index.rss')
    theParser.parse(xmlFile)
    for line in theHandler.linesHTML:
        fichHTML.write(line)
    return theHandler.linesDic

    print "Parse complete"
