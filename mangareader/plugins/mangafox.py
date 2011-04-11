import urllib, urllib2, re

class Mangafox(Websupport):
    
    DIRECTORY = "http://www.mangafox.com/directory/all"
    def syncTitles():
        #
        response = urllib2.urlopen(DIRECTORY)
        data = response.read()
        numberpattern = re.search('Prev([<>a-z0-9/=". ])*', data).group(0)
        lastNumber = re.findall('>([0-9]+)<',numberpattern)[-1]

    for i in range(lastNumber):
        response = urllib2.urlopen(DIRECTORY + i + ".htm")
        data = response.read()
        titles = re.findall('', data)
        self.mangaList.append()
